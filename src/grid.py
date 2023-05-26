import pygame


class Ground:
    def __init__(self, surface, size=500, color='GREEN', color_grid='BLACK', grid=True):
        self.grid = grid
        self.color = color
        self.surface = surface
        self.size = size
        self.scale = 1
        self.color_grid = color_grid
        self.w = pygame.display.get_surface().get_width()
        self.h = pygame.display.get_surface().get_height()

    def set_scale(self, s):
        self.size += s

    def draw(self, coord):
        x, y = coord
        rect = pygame.Rect((x,y, self.size, self.size))
        rect.center = (self.w//2+x, self.h//2 + y)
        pygame.draw.rect(self.surface, self.color, rect)

        if self.grid:
            self.draw_grid((rect.x, rect.y), self.size)

    def draw_grid(self, coord, size):
        x, y = coord
        color = self.color_grid
        n = 25 # number of lines
        for row in range(n+1):
            for column in range(n+1):
                pygame.draw.line(self.surface, color, (x + column * (size / n), y), \
                                 (x + column * (size / n), y + size))
                pygame.draw.line(self.surface, color, (x, y + row * (size / n)), \
                                 (x + size, y + row * (size / n)))





