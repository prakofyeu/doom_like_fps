class Hud:
    def __init__(self, screen, weapon_image):
        self.screen = screen
        self.weapon_image = weapon_image
        self.offset_y = 0
        self.recoil = 0

    def shoot(self):
        self.recoil = 20

    def update(self):
        if self.recoil > 0:
            self.offset_y = self.recoil
            self.recoil -= 1
        else:
            self.offset_y = 0


    def draw(self):
        self.update()
        weapon_rect = self.weapon_image.get_rect()
        weapon_rect.midbottom = (self.screen.get_width()//2, self.screen.get_height()-self.offset_y)
        self.screen.blit(self.weapon_image, weapon_rect)

