import pygame

class BulletEffect:
    def __init__(self, image):
        self.effects = []
        self.image = image

    def add_effect(self, x, y):
        self.effects.append([x, y, pygame.time.get_ticks()])

    def draw(self, screen):
        current_time = pygame.time.get_ticks()
        for effect in self.effects[:]:
            x, y, effect_time = effect
            if current_time - effect_time > 120:
                self.effects.remove(effect)
                continue
            screen.blit(self.image, (int(x) - self.image.get_width()//2, int(y)- self.image.get_height()//2))