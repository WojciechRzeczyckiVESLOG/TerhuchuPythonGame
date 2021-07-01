import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GREY, BLACK

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        #self.selected = False

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        pass

    def make_king(self):
        pass
        #self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        # pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        if self.color == RED:
            return "RED"
        elif self.color == BLACK:
            return "BLACK"
        else:
            return str(self.color)
