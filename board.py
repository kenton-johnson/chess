import pygame
from square import Square

class Board:
    COLUMNS = 'abcdefgh'
    WHITE = (255, 255, 255)
    BLACK = (100, 100, 100)

    def __init__(self, size):
        self.size = size
        self.board = self.create_board()
        self.font = pygame.font.SysFont(None, size // 4)


    def create_board(self):
        board = {}
        for row in range(1, 9):  # ranks
            for col in Board.COLUMNS:  # files
                color = 'white' if (row + Board.COLUMNS.index(col)) % 2 == 0 else 'black'
                square = Square(row, col, color)
                board[square.name] = square
        return board

    def draw(self, screen):
        for square in self.board.values():
            # Place the position of the square based off of file and rank
            x = (ord(square.file) - ord('a')) * self.size
            y = (8 - square.rank) * self.size
            rect = pygame.Rect(x, y, self.size, self.size)

            # Draws the square with the appropriate color
            color = Board.WHITE if square.color == 'white' else Board.BLACK
            pygame.draw.rect(screen, color, rect)

            # Choose text color based on opposite square color
            text_color = Board.BLACK if square.color == 'white' else Board.WHITE

            # Draw file letter (bottom-right corner) only on rank 1
            if square.rank == 1:
                file_label = self.font.render(square.file, True, text_color)
                fx = x + self.size - file_label.get_width() - 2
                fy = y + self.size - file_label.get_height() - 2
                screen.blit(file_label, (fx, fy))

            # Draw rank number (top-left corner) only on file 'a'
            if square.file == 'a':
                rank_label = self.font.render(str(square.rank), True, text_color)
                rx = x + 2
                ry = y + 2
                screen.blit(rank_label, (rx, ry))

