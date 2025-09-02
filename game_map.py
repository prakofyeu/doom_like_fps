from settings import *


class Map:
    def __init__(self):
        self.grid = [
                "########",
                "#......#",
                "#..RR#.#",
                "#..R...#",
                "########"
                ]
        self.tile_size = 100
        self.scale = 0.1
        self.big = False



    def mapping(self, x, y):
        return int(x) // self.tile_size, int(y) // self.tile_size

    def is_wall(self, x, y):
        i, j = self.mapping(x, y)
        if 0 <= j < len(self.grid) and 0 <= i < len(self.grid[0]):
            return self.grid[j][i] == "#" or self.grid[j][i] == "R"  #ПОменял индексы
        return True

    def can_move(self, x, y):
        return not self.is_wall(x, y)

    def draw_map(self, screen, player, enemies):
        self.scale = 0.7 if self.big else 0.1
        map_tile_size = int(self.tile_size*self.scale)
        for j, row in enumerate(self.grid):
            for i, tile in enumerate(row):
                if tile == ".":
                    tile_color = (200, 200, 200)
                else:
                    tile_color = (30, 30, 30)

                pygame.draw.rect(screen, tile_color, (j*map_tile_size, i*map_tile_size, map_tile_size, map_tile_size))

        map_player_x = int(player.x * self.scale)
        map_player_y = int(player.y * self.scale)
        pygame.draw.circle(screen, (0, 255, 0), (map_player_y, map_player_x), 50*self.scale)

        target_x = int(math.cos(player.angle) * 200 * self.scale)
        target_y = int(math.sin(player.angle) * 200 * self.scale)
        pygame.draw.line(screen, (0, 200, 0), (map_player_y, map_player_x), (map_player_y+target_y, map_player_x+target_x))

        for enemy in enemies:
            map_enemy_x = int(enemy.x * self.scale)
            map_enemy_y = int(enemy.y * self.scale)
            pygame.draw.circle(screen, (255, 0, 0), (map_enemy_y, map_enemy_x), 30 * self.scale)

