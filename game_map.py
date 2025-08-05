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

    def mapping(self, x, y):
        return int(x) // self.tile_size, int(y) // self.tile_size

    def is_wall(self, x, y):
        i, j = self.mapping(x, y)
        if 0 <= j < len(self.grid) and 0 <= i < len(self.grid[0]):
            return self.grid[j][i] == "#" or self.grid[j][i] == "R"  #ПОменял индексы
        return True

    def can_move(self, x, y):
        return not self.is_wall(x, y)


