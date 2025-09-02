import pygame
from settings import *


class Raycaster:
    def __init__(self, screen, game_map, texture):
        self.screen = screen
        self.map = game_map
        self.texture = texture
        self.tex_width = self.texture.get_width()
        self.tex_height = self.texture.get_height()
        self.tile_size = self.map.tile_size
        self.depth = [float("inf")]*NUM_RAYS

    def cast_ray(self, px, py, angle):
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)

        # --- Вертикальные линии ---
        x_vert, dx = (px // self.tile_size + 1) * self.tile_size, 1
        if cos_a < 0:
            x_vert = (px // self.tile_size) * self.tile_size - 0.0001
            dx = -1
        depth_v = (x_vert - px) / cos_a
        y_vert = py + depth_v * sin_a

        delta_depth = self.tile_size / abs(cos_a)
        dy = self.tile_size * sin_a / abs(cos_a)

        for _ in range(0, MAX_DEPTH, self.tile_size):
            tile_x = int(x_vert // self.tile_size)
            tile_y = int(y_vert // self.tile_size)
            if self.map.is_wall(tile_x * self.tile_size, tile_y * self.tile_size):
                texture_x_v = int(y_vert % self.tile_size / self.tile_size * self.tex_width)
                vert_hit = True
                break
            x_vert += dx * self.tile_size
            y_vert += dy
            depth_v += delta_depth
        else:
            depth_v = float('inf')
            texture_x_v = 0
            vert_hit = False

        # --- Горизонтальные линии ---
        y_hor, dy = (py // self.tile_size + 1) * self.tile_size, 1
        if sin_a < 0:
            y_hor = (py // self.tile_size) * self.tile_size - 0.0001
            dy = -1
        depth_h = (y_hor - py) / sin_a
        x_hor = px + depth_h * cos_a

        delta_depth = self.tile_size / abs(sin_a)
        dx = self.tile_size * cos_a / abs(sin_a)

        for _ in range(0, MAX_DEPTH, self.tile_size):
            tile_x = int(x_hor // self.tile_size)
            tile_y = int(y_hor // self.tile_size)
            if self.map.is_wall(tile_x * self.tile_size, tile_y * self.tile_size):
                texture_x_h = int(x_hor % self.tile_size / self.tile_size * self.tex_width)
                hor_hit = True
                break
            y_hor += dy * self.tile_size
            x_hor += dx
            depth_h += delta_depth
        else:
            depth_h = float('inf')
            texture_x_h = 0
            hor_hit = False

        # --- Выбор ближней стены ---
        if depth_v < depth_h:
            depth = depth_v
            texture_x = texture_x_v
            hit_vertical = True
        else:
            depth = depth_h
            texture_x = texture_x_h
            hit_vertical = False

        return depth, texture_x, hit_vertical

    def raycasting(self, player):
        self.depth = [float("inf")] * NUM_RAYS
        px, py = player.x, player.y
        cur_angle = player.angle - HALF_FOV

        for ray in range(NUM_RAYS):
            depth, texture_x, hit_vertical = self.cast_ray(px, py, cur_angle)

            # коррекция рыбьего глаза
            depth *= math.cos(player.angle - cur_angle)

            # проекция
            proj_height = int(PROJ_COEF / (depth + 0.0001))

            # выбор колонки из текстуры
            texture_x = max(0, min(self.tex_width - 1, int(texture_x)))
            column = self.texture.subsurface(texture_x, 0, 1, self.tex_height)
            column = pygame.transform.scale(column, (SCALE, proj_height))

            # затемнение горизонтальных стен (эффект света)
            if not hit_vertical:
                dark = pygame.Surface((SCALE, proj_height))
                dark.fill((0, 0, 0))
                dark.set_alpha(80)
                column.blit(dark, (0, 0))

            # отрисовка
            self.screen.blit(column, (ray * SCALE, HEIGHT // 2 - proj_height // 2))
            self.depth[ray] = depth
            cur_angle += DELTA_ANGLE
