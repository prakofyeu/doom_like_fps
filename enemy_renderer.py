import pygame
from settings import SCALE, NUM_RAYS


class EnemyRenderer:
    def __init__(self, screen, raycaster):
        self.screen = screen
        self.raycaster = raycaster

    def draw(self, enemies, player):
        sprites = []
        for enemy in enemies:
            data = enemy.get_sprite(player)
            if data and enemy.alive:
                full_distance, screen_x, screen_y, proj_height = data
                sprites.append((full_distance, enemy, screen_x, screen_y, proj_height))

        # сортировка по реальной дистанции (дальние первыми)
        sprites.sort(key=lambda d: d[0], reverse=True)

        for full_distance, enemy, screen_x, screen_y, proj_height in sprites:
            # масштабируем с сохранением пропорций
            w, h = enemy.texture.get_size()
            scale = proj_height / h
            sprite = pygame.transform.scale(enemy.texture, (int(w * scale), int(proj_height)))

            sprite_half_width = sprite.get_width() // 2
            left = int((screen_x - sprite_half_width) / SCALE)
            right = int((screen_x + sprite_half_width) / SCALE)

            # проверка по z-buffer (чтобы враг не лез сквозь стены)
            visible = False
            for ray in range(max(0, left), min(NUM_RAYS, right)):
                if full_distance < self.raycaster.depth[ray]:
                    visible = True
                    break

            if visible:
                # рисуем так, чтобы низ врага стоял "на земле"
                self.screen.blit(sprite, (screen_x - sprite_half_width, screen_y))
