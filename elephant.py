"""
elephant.py
contains all code for the elephant
"""
import pieces
from board import board_arr

class Elephant(pieces.Piece):
    """ elephant piece """
    def __init__(self, x, y, piece_name, c):
        pieces.Piece.__init__(self, x, y, piece_name, c)
    def get_available_moves(self):
        if self.x_coord + 2 <= 8:
            if self.color: # blue
                if self.y_coord + 2 <= 4:
                    # check if nothing is blocking elephant's path
                    if board_arr[self.x_coord+1][self.y_coord+1].is_occupied_none():
                        self.add_move(self.x_coord + 2, self.y_coord + 2)
                if self.y_coord - 2 >= 0:
                    if board_arr[self.x_coord+1][self.y_coord-1].is_occupied_none():
                        self.add_move(self.x_coord + 2, self.y_coord - 2)
            else: #red
                if self.y_coord + 2 <= 9:
                    if board_arr[self.x_coord+1][self.y_coord+1].is_occupied_none():
                        self.add_move(self.x_coord + 2, self.y_coord + 2)
                if self.y_coord - 2 >= 5:
                    if board_arr[self.x_coord+1][self.y_coord-1].is_occupied_none():
                        self.add_move(self.x_coord + 2, self.y_coord - 2)
        if self.x_coord - 2 >= 0:
            if self.color: # blue
                if self.y_coord + 2 <= 4:
                    # check if nothing is blocking elephant's path
                    if board_arr[self.x_coord-1][self.y_coord+1].is_occupied_none():
                        self.add_move(self.x_coord - 2, self.y_coord + 2)
                if self.y_coord - 2 >= 0:
                    if board_arr[self.x_coord-1][self.y_coord-1].is_occupied_none():
                        self.add_move(self.x_coord - 2, self.y_coord - 2)
            else: #red
                if self.y_coord + 2 <= 9:
                    if board_arr[self.x_coord-1][self.y_coord+1].is_occupied_none():
                        self.add_move(self.x_coord - 2, self.y_coord + 2)
                if self.y_coord - 2 >= 5:
                    if board_arr[self.x_coord-1][self.y_coord-1].is_occupied_none():
                        self.add_move(self.x_coord - 2, self.y_coord - 2)
