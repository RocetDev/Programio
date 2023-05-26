import pygame
from src.grid import Ground
from src.keyboard import KeyInterface
import src.colors as colors
from src.rover import Rover

pygame.init()

# CONSTANTS
FPS = 60
WIDTH = 800
HEIGHT = 600

# PYGAME MOMENTS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Programio")

# OTHER VARIABLE
game_zone = Ground(screen, grid=1, size=800, color=colors.GROUND, color_grid=colors.GRID_LINE)
keyInterface = KeyInterface()
rover1 = Rover(screen)


def update():
    keyInterface.moving_keys(speed=15)
    keyInterface.moving_mouse()
    keyInterface.change_scale_scroll()
    game_zone.set_scale(0)
    coord = keyInterface.get_xy()
    game_zone.draw(coord)

    rover1.draw(coord)
    rover1.go()
    rover1.left(1/8)

def main():
    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

        screen.fill(colors.DEFAULT_BACKGROUND)
        update()
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)


if __name__ == "__main__":
    main()

