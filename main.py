import pygame
from board import Board

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 480, 480
SQUARE_SIZE = WIDTH // 8
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Clock to control frame rate
clock = pygame.time.Clock()

# Create the chess board
board = Board(SQUARE_SIZE)

def main():
    running = True
    while running:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # TODO: Add mouse click logic here

        # Draw everything
        board.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
