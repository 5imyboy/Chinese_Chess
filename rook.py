"""
rook.py
contains all code for the rook
"""
import pieces
from board import board_arr

class Rook(pieces.Piece):
    """ rook piece """
    def __init__(self, x, y, piece_name, c):
        pieces.Piece.__init__(self, x, y, piece_name, c)
    def get_available_moves(self):
        for i in range(self.x_coord + 1, 9):
            # if no piece is here, add to coords
            if board_arr[i][self.y_coord].is_occupied_none():
                self.add_move(i, self.y_coord)
            # if there is a piece here, add if its enemy, and stop
            else:
                self.add_move(i, self.y_coord)
                break
        for i in range(self.x_coord - 1, -1, -1):
            if board_arr[i][self.y_coord].is_occupied_none():
                self.add_move(i, self.y_coord)
            else:
                self.add_move(i, self.y_coord)
                break
        for i in range(self.y_coord + 1, 10):
            if board_arr[self.x_coord][i].is_occupied_none():
                self.add_move(self.x_coord, i)
            else:
                self.add_move(self.x_coord, i)
                break
        for i in range(self.y_coord - 1, -1, -1):
            if board_arr[self.x_coord][i].is_occupied_none():
                self.add_move(self.x_coord, i)
            else:
                self.add_move(self.x_coord, i)
                break
            