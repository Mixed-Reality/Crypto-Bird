import pygame
import sys
from crypto import get_data
from objects import Colliders


W, H = 1000, 600
FPS = 60


def main():
    btc_data = get_data('BTC-USD')
    eth_data = get_data('ETH-USD')
    # print(btc_data)

    # Game
    pygame.init()

    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()

    bg_surface = pygame.image.load('assets/bg.jpg').convert()
    bg_surface = pygame.transform.scale(bg_surface, (W, H))

    bars = Colliders('btc', btc_data)
    bars.normalize()

    bars_up = Colliders('eth', eth_data)
    bars_up.normalize()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg_surface, (0, 0))

        bars.render(screen, H, W)
        bars_up.render(screen, H, W)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
