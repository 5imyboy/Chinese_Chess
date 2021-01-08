"""
knight.py
contains all code for the kinght
"""
import pieces
from board import board_arr

class Knight(pieces.Piece):
    """ knight piece """
    def __init__(self, x, y, piece_name, c):
        pieces.Piece.__init__(self, x, y, piece_name, c)
    def get_available_moves(self):
        if self.x_coord + 1 <= 8:
            if board_arr[self.x_coord+1][self.y_coord].is_occupied_none():
                self.add_move(self.x_coord + 2, self.y_coord + 1)
                self.add_move(self.x_coord + 2, self.y_coord - 1)
        if self.x_coord - 1 >= 0:
            if board_arr[self.x_coord-1][self.y_coord].is_occupied_none():
                self.add_move(self.x_coord - 2, self.y_coord + 1)
                self.add_move(self.x_coord - 2, self.y_coord - 1)
        if self.y_coord + 1 <= 9:
            if board_arr[self.x_coord][self.y_coord+1].is_occupied_none():
                self.add_move(self.x_coord + 1, self.y_coord + 2)
                self.add_move(self.x_coord - 1, self.y_coord + 2)
        if self.y_coord - 1 >= 0:
            if board_arr[self.x_coord][self.y_coord-1].is_occupied_none():
                self.add_move(self.x_coord + 1, self.y_coord - 2)
                self.add_move(self.x_coord - 1, self.y_coord - 2)
                    