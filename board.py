"""
board.py
draws the board
"""

import pygame

BOX_SIZE = 60
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
board_arr = []

class BoardPos:
    """ object in board array """
    def __init__(self):
        self.is_occupied_red = False
        self.is_occupied_blue = False

    def is_occupied_none(self):
        """ true iff no piece is on this square """
        return not self.is_occupied_blue and not self.is_occupied_red

    def occupy_red(self):
        """ red piece occupies this position """
        self.is_occupied_red = True
        self.is_occupied_blue = False

    def occupy_blue(self):
        """ blue piece occupies this position """
        self.is_occupied_red = False
        self.is_occupied_blue = True

    def occupy_none(self):
        """ no piece occupies this position """
        self.is_occupied_red = False
        self.is_occupied_blue = False

for j in range(9): # x_coord
    board_arr.append([])
    for k in range(10): # y_coord
        board_arr[j].append(BoardPos())

def draw_board(screen, color, box_size, x_center, y_center):
    """
    this function draws the board
    """
    #initialize border values
    top_border = box_size * (-4.5) + y_center
    bot_border = box_size * 4.5 + y_center
    left_border = box_size * (-4) + x_center
    right_border = box_size * 4 + x_center
    #draw left and right border
    pygame.draw.line(screen, color, [box_size*(-4) + x_center, bot_border],
    [box_size*(-4) + x_center, top_border], width = 1)
    pygame.draw.line(screen, color, [box_size*4 + x_center, bot_border],
    [box_size*4 + x_center, top_border], width = 1)
    #draw all other vertial lines
    for i in range(1, 8):
        river_north = top_border + (box_size * 4)
        river_south = bot_border - (box_size * 4)
        pygame.draw.line(screen, color, [box_size*(i-4) + x_center, bot_border],
        [box_size*(i-4) + x_center, river_south], width = 1)
        pygame.draw.line(screen, color, [box_size*(i-4) + x_center, top_border],
        [box_size*(i-4) + x_center, river_north], width = 1)
    #draw horizontal lines
    for i in range(0, 10):
        pygame.draw.line(screen, color, [left_border, box_size*(i-4.5) + y_center],
        [right_border, box_size*(i-4.5) + y_center], width = 1)
    #draw 'X's
    pygame.draw.line(screen, color, [-box_size + x_center, top_border],
    [box_size + x_center, top_border + (2*box_size)], width = 1)
    pygame.draw.line(screen, color, [box_size + x_center, top_border],
    [-box_size + x_center, top_border + (2*box_size)], width = 1)
    pygame.draw.line(screen, color, [-box_size + x_center, bot_border],
    [box_size + x_center, bot_border - (2*box_size)], width = 1)
    pygame.draw.line(screen, color, [box_size + x_center, bot_border],
    [-box_size + x_center, bot_border - (2*box_size)], width = 1)

def reset_board():
    """ empties board """
    for i in range(9):
        for x in range(10):
            board_arr[i][x].occupy_none()

def add_piece_to_board(piece):
    """ updates board coordiantes with piece """
    if piece.color == 0:
        board_arr[piece.y_coord][piece.x_coord].occupy_red()
    if piece.color == 1:
        board_arr[piece.y_coord][piece.x_coord].occupy_blue()

def board_to_actual(x_coord, y_coord):
    """ converts board coordinate to screen coordinates """
    return (int(BOX_SIZE*(x_coord - 4) + SCREEN_WIDTH / 2),\
        int(BOX_SIZE*(y_coord - 4.5) + SCREEN_HEIGHT / 2))

def actual_to_board(x_coord, y_coord):
    """ converts screen coordinates to board coordinates """
    return (int((x_coord - SCREEN_WIDTH/2) / BOX_SIZE) + 4,
            int(((y_coord - SCREEN_HEIGHT/2) / BOX_SIZE) + 4.5))
