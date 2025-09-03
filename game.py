import pygame
from player import Player
from raycaster import Raycaster
from game_map import Map
from weapon import Weapon
from bullet_effect import BulletEffect
from hud import Hud
from settings import WIDTH, HEIGHT
from enemy import  Enemy
from enemy_renderer import  EnemyRenderer

brick_texture = pygame.transform.scale(pygame.image.load("images/brciks.png"), (1024, 1024))
wood_texture = pygame.transform.scale(pygame.image.load("images/wood.png"), (1024, 1024))
sky_texture = pygame.transform.scale(pygame.image.load("images/sky.png"), (WIDTH, HEIGHT//2))
weapon_texture = pygame.transform.scale(pygame.image.load("images/shotgun.png"), (WIDTH//5, HEIGHT//5))
effect_texture = pygame.transform.scale(pygame.image.load("images/hit.png"), (70, 70))
enemy_texture = pygame.transform.scale(pygame.image.load("images/enemy.png"), (100, 100))


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)

        self.map = Map()
        self.player = Player(self.map.tile_size*3/2, self.map.tile_size*3/2)
        self.raycaster = Raycaster(self.screen, self.map, brick_texture)
        self.effects = BulletEffect(effect_texture)
        self.hud = Hud(self.screen, weapon_texture)

        self.enemy_renderer = EnemyRenderer(self.screen, self.raycaster)

        self.enemies = [
            Enemy(100, 200, enemy_texture, 100),
            Enemy(400, 200, enemy_texture, 100),
            Enemy(800, 800, enemy_texture, 100),
        ]

        self.weapon = Weapon(self.player, self.map, self.effects, self.enemies)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.weapon.shoot()
                    self.hud.shoot()
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    exit()
                if pygame.key.get_pressed()[pygame.K_m]:
                    self.map.big = True if not self.map.big else False


            self.player.move(self.map)

            self.screen.fill((25, 50, 50), (0, HEIGHT // 2, WIDTH, HEIGHT))
            self.screen.blit(sky_texture, (0, 0))




            self.raycaster.raycasting(self.player)
            self.enemy_renderer.draw(self.enemies, self.player)

            self.effects.draw(self.screen)
            self.hud.draw()
            self.map.draw_map(self.screen, self.player, self.enemies)

            pygame.display.flip()
            pygame.time.Clock().tick(30)