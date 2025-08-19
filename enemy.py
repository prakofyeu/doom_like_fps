from settings import *


class Enemy:
    def __init__(self, x, y, texture):
        self.x = x
        self.y = y
        self.texture = texture

    def get_sprite(self, player):
        dx = self.x - player.x
        dy = self.y - player.y
        distance = math.hypot(dx, dy)
        angle_to_enemy = math.atan2(dy, dx)
        delta_angle = angle_to_enemy - player.angle
        if delta_angle > math.pi:
            delta_angle -= 2*math.pi
        if delta_angle < -math.pi:
            delta_angle += 2*math.pi

        if -HALF_FOV < delta_angle < HALF_FOV:
            distance *= math.cos(delta_angle)
            proj_height = PROJ_COEF/(distance+0.0001)
            screen_x = WIDTH//2 + (delta_angle*DIST)
            screen_y = HEIGHT//2 - proj_height//2
            return distance, screen_x, screen_y, proj_height

        return None