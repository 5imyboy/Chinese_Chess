"""
general.py
contains all code for the general
"""
import pieces

class General(pieces.Piece):
    """ general piece """
    def __init__(self, x, y, piece_name, c):
        pieces.Piece.__init__(self, x, y, piece_name, c)
    def get_available_moves(self):
        """ make a list of available moves """
        if self.x_coord + 1 <= 5:
            self.add_move(self.x_coord + 1, self.y_coord)
        if self.x_coord - 1 >= 3:
            self.add_move(self.x_coord - 1, self.y_coord)
        if self.color: # if blue
            if self.y_coord + 1 <= 2:
                self.add_move(self.x_coord, self.y_coord + 1)
            if self.y_coord - 1 >= 0:
                self.add_move(self.x_coord, self.y_coord - 1)
        else:
            if self.y_coord + 1 <= 9:
                self.add_move(self.x_coord, self.y_coord + 1)
            if self.y_coord - 1 >= 7:
                self.add_move(self.x_coord, self.y_coord - 1)
