"""
cannon.py
contains all code for the cannon
"""
import pieces
from board import board_arr

class Cannon(pieces.Piece):
    """ cannon piece """
    def __init__(self, x, y, piece_name, c):
        pieces.Piece.__init__(self, x, y, piece_name, c)
    def get_available_moves(self):
        has_jumped = False
        end = False
        for i in range(self.x_coord + 1, 9):
            # if no piece is on this square
            if board_arr[i][self.y_coord].is_occupied_none():
                # if we haven't skipped a piece, add this coord to available moves
                if not has_jumped:
                    self.add_move(i, self.y_coord)
            else:
                # if there is a piece here, and we've skipped a piece already, add this coord
                if has_jumped:
                    self.add_move(i, self.y_coord)
                    end = True
                # if there is a piece here and we haven't skipped a piece, skip
                else:
                    has_jumped = True
            if end:
                break
        has_jumped = False
        end = False
        for i in range(self.x_coord - 1, -1, -1):
            if board_arr[i][self.y_coord].is_occupied_none():
                if not has_jumped:
                    self.add_move(i, self.y_coord)
            else:
                if has_jumped:
                    self.add_move(i, self.y_coord)
                    end = True
                else:
                    has_jumped = True
            if end:
                break
        has_jumped = False
        end = False
        for i in range(self.y_coord + 1, 10):
            if board_arr[self.x_coord][i].is_occupied_none():
                if not has_jumped:
                    self.add_move(self.x_coord, i)
            else:
                if has_jumped:
                    self.add_move(self.x_coord, i)
                    end = True
                else:
                    has_jumped = True
            if end:
                break
        has_jumped = False
        end = False
        for i in range(self.y_coord - 1, -1, -1):
            if board_arr[self.x_coord][i].is_occupied_none():
                if not has_jumped:
                    self.add_move(self.x_coord, i)
            else:
                if has_jumped:
                    self.add_move(self.x_coord, i)
                    end = True
                else:
                    has_jumped = True
            if end:
                break
