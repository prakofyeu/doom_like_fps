import math
from settings import WIDTH, HEIGHT, HALF_FOV, PROJ_COEF, DIST


class Enemy:
    def __init__(self, x, y, texture):
        self.x = x
        self.y = y
        self.texture = texture

    def get_sprite(self, player):
        dx = self.x - player.x
        dy = self.y - player.y
        full_distance = math.hypot(dx, dy)   # реальная дистанция (для сортировки)
        angle_to_enemy = math.atan2(dy, dx)

        # угол относительно взгляда игрока
        delta_angle = angle_to_enemy - player.angle
        delta_angle = (delta_angle + math.pi) % (2 * math.pi) - math.pi  # нормализация (-π, π)

        # враг в поле зрения?
        if -HALF_FOV < delta_angle < HALF_FOV:
            # коррекция fish-eye
            distance = full_distance * math.cos(delta_angle)
            if distance <= 0:
                return None

            proj_height = PROJ_COEF / distance
            screen_x = WIDTH // 2 + (delta_angle * DIST)
            screen_y = HEIGHT // 2 - proj_height//2  # верхняя точка спрайта

            return full_distance, screen_x, screen_y, proj_height

        return None
