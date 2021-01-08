"""
pieces.py
initialize each piece object
"""
from board import board_to_actual
from board import actual_to_board
from board import board_arr

class Piece:
    """
    piece object
    """
    def __init__(self, x, y, piece_name, c):
        """ create a piece """
        self.x_coord = x
        self.y_coord = y
        self.name = piece_name
        self.rect = piece_name.get_rect()
        self.rect.centerx, self.rect.centery = board_to_actual(x, y)
        self.color = c # 0 for red, 1 for blue
        self.available_moves = [[self.x_coord, self.y_coord]]
        if self.color:
            board_arr[x][y].occupy_blue()
        else:
            board_arr[x][y].occupy_red()

    def coords(self):
        """ print out piece's coordinates """
        return (self.x_coord, self.y_coord)

    def draw(self, screen):
        """ draws piece onto board """
        screen.blit(self.name, (self.rect.x, self.rect.y))

    def update_coord(self):
        """ updates coordinates with what's shown on board """
        (self.x_coord, self.y_coord) = actual_to_board(self.rect.centerx, self.rect.centery)

    def move(self, x_c, y_c, x_old, y_old):
        """ moves the piece to new coords and update board """
        # set old coordinates to none
        board_arr[x_old][y_old].occupy_none()
        # move
        (self.rect.centerx, self.rect.centery) = board_to_actual(x_c, y_c)
        # update coords
        self.update_coord()
        # update board
        if self.color: #blue
            board_arr[x_c][y_c].occupy_blue()
        else:
            board_arr[x_c][y_c].occupy_red()


    def get_available_moves(self):
        """ abstract function where a piece gets its available moves """
        pass

    def add_move(self, x_c, y_c):
        """ adds potential move to available moves, checks for friendly piece in the way, and for borders """
        if x_c < 0 or x_c > 8 or y_c < 0 or y_c > 9:
            return
        if self.color: # blue
            if not board_arr[x_c][y_c].is_occupied_blue:
                self.available_moves.append([x_c, y_c])
        else: # red
            if not board_arr[x_c][y_c].is_occupied_red:
                self.available_moves.append([x_c, y_c])

    def reset_moves(self):
        """ reset moves to none """
        self.available_moves = [[self.x_coord, self.y_coord]]
