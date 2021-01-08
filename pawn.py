"""
pawn.py
contains all code for the pawn
"""
import pieces

class Pawn(pieces.Piece):
    """ pawn piece """
    def __init__(self, x, y, piece_name, c):
        pieces.Piece.__init__(self, x, y, piece_name, c)
    def get_available_moves(self):
        if self.color: # blue
            self.add_move(self.x_coord, self.y_coord + 1)
            if self.y_coord >= 5:
                self.add_move(self.x_coord - 1, self.y_coord)
                self.add_move(self.x_coord + 1, self.y_coord)
        else:
            self.add_move(self.x_coord, self.y_coord - 1)
            if self.y_coord <= 4:
                self.add_move(self.x_coord - 1, self.y_coord)
                self.add_move(self.x_coord + 1, self.y_coord)
                