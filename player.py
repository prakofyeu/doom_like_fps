import pygame
import math

class Player:
    def __init__(self, x, y, angle=0, speed=5):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.sensitivity = 0.003

    def move(self, game_map):
        dx, dy = 0, 0
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            dx += self.speed * cos_a
            dy += self.speed * sin_a
        if keys[pygame.K_s]:
            dx -= self.speed * cos_a
            dy -= self.speed * sin_a


        if game_map.can_move(self.x + dx, self.y + dy): #заменил х
            self.x += dx
            self.y += dy
        else:
            self.x -= dx
            self.y -= dy

        self.angle += pygame.mouse.get_rel()[0]*self.sensitivity

