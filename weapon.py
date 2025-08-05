from settings import *


class Weapon:
    def __init__(self, player, game_map, effects):
        self.player = player
        self.game_map = game_map
        self.effects = effects

    def shoot(self):
        angle = self.player.angle
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)
        for depth in range(1, MAX_DEPTH):
            target_x = self.player.x + depth * cos_a
            target_y = self.player.y + depth * sin_a
            if self.game_map.is_wall(target_x, target_y):
                proj_height = PROJ_COEF/(depth + 0.0001)
                screen_x = WIDTH//2
                screen_y = HEIGHT//2 - proj_height//2 + int(proj_height*0.5)
                self.effects.add_effect(screen_x, screen_y)
                break