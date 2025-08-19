import pygame.transform

from settings import SCALE, NUM_RAYS


class EnemyRenderer:
    def __init__(self, screen, raycaster):
        self.screen = screen
        self.raycaster = raycaster

    def draw(self, enemies, player):
        sprites = []
        for enemy in enemies:
            data = enemy.get_sprite(player)
            if data:
                distance, screen_x, screen_y, proj_height = data
                sprites.append((distance, enemy, screen_x, screen_y, proj_height))

        sprites.sort(key=lambda d: d[0], reverse=True)
        for distance, enemy, screen_x, screen_y, proj_height in sprites:
            sprite = pygame.transform.scale(enemy.texture, (int(proj_height), int(proj_height)))
            ray_index = int(screen_x/SCALE)
            if 0 <= ray_index < NUM_RAYS:
                if distance < self.raycaster.depth[ray_index]:
                    self.screen.blit(sprite, (screen_x-proj_height//2, screen_y-proj_height//2))

