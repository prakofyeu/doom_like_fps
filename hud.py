class Hud:
    def __init__(self, screen, weapon_image):
        self.screen = screen
        self.weapon_image = weapon_image

    def draw(self):
        weapon_rect = self.weapon_image.get_rect()
        weapon_rect.midbottom = (self.screen.get_width()//2, self.screen.get_height())
        self.screen.blit(self.weapon_image, weapon_rect)