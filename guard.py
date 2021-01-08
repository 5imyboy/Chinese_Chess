"""
guard.py
contains all code for the guards
"""
import pieces

class Guard(pieces.Piece):
    """ guard piece """
    def __init__(self, x, y, piece_name, c):
        pieces.Piece.__init__(self, x, y, piece_name, c)
    def get_available_moves(self):
        if self.x_coord + 1 <= 5:
            if self.color: # blue
                if self.y_coord + 1 <= 2:
                    self.add_move(self.x_coord + 1, self.y_coord + 1)
                if self.y_coord - 1 >= 0:
                    self.add_move(self.x_coord + 1, self.y_coord - 1)
            else: # red
                if self.y_coord + 1 <= 9:
                    self.add_move(self.x_coord + 1, self.y_coord + 1)
                if self.y_coord - 1 >= 7:
                    self.add_move(self.x_coord + 1, self.y_coord - 1)
        if self.x_coord - 1 >= 3:
            if self.color: # blue
                if self.y_coord + 1 <= 2:
                    self.add_move(self.x_coord - 1, self.y_coord + 1)
                if self.y_coord - 1 >= 0:
                    self.add_move(self.x_coord - 1, self.y_coord - 1)
            else: # red
                if self.y_coord + 1 <= 9:
                    self.add_move(self.x_coord - 1, self.y_coord + 1)
                if self.y_coord - 1 >= 7:
                    self.add_move(self.x_coord - 1, self.y_coord - 1)
