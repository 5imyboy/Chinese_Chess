"""
main.py
where the main game is coded

image of pieces:
https://image.slidesharecdn.com/playchinesechess-100804063853-phpapp01/95/play-chinese-chess-5-728.jpg?cb=1280903983
"""

import os
import pygame
import board
import general
import guard
import elephant
import knight
import rook
import pawn
import cannon

def make_pieces():
    """ adds all pieces to a single array """
    # path is the path to the main file
    path = os.path.dirname(os.path.realpath(__file__))
    return {
        "red_general": general.General(4, 9, pygame.image.load(path + '/Pieces/red_general.png'), 0),
        "red_guard_one": guard.Guard(3, 9, pygame.image.load(path + '/Pieces/red_guard.png'), 0),
        "red_guard_two": guard.Guard(5, 9, pygame.image.load(path + '/Pieces/red_guard.png'), 0),
        "red_elephant_one": elephant.Elephant(2, 9, pygame.image.load(path + '/Pieces/red_elephant.png'), 0),
        "red_elephant_two": elephant.Elephant(6, 9, pygame.image.load(path + '/Pieces/red_elephant.png'), 0),
        "red_knight_one": knight.Knight(1, 9, pygame.image.load(path + '/Pieces/red_knight.png'), 0),
        "red_knight_two": knight.Knight(7, 9, pygame.image.load(path + '/Pieces/red_knight.png'), 0),
        "red_rook_one": rook.Rook(0, 9, pygame.image.load(path + '/Pieces/red_rook.png'), 0),
        "red_rook_two": rook.Rook(8, 9, pygame.image.load(path + '/Pieces/red_rook.png'), 0),
        "red_pawn_one": pawn.Pawn(0, 6, pygame.image.load(path + '/Pieces/red_pawn.png'), 0),
        "red_pawn_two": pawn.Pawn(2, 6, pygame.image.load(path + '/Pieces/red_pawn.png'), 0),
        "red_pawn_three": pawn.Pawn(4, 6, pygame.image.load(path + '/Pieces/red_pawn.png'), 0),
        "red_pawn_four": pawn.Pawn(6, 6, pygame.image.load(path + '/Pieces/red_pawn.png'), 0),
        "red_pawn_five": pawn.Pawn(8, 6, pygame.image.load(path + '/Pieces/red_pawn.png'), 0),
        "red_cannon_one": cannon.Cannon(1, 7, pygame.image.load(path + '/Pieces/red_cannon.png'), 0),
        "red_cannon_two": cannon.Cannon(7, 7, pygame.image.load(path + '/Pieces/red_cannon.png'), 0),

        "blue_general": general.General(4, 0, pygame.image.load(path + '/Pieces/blue_general.png'), 1),
        "blue_guard_one": guard.Guard(3, 0, pygame.image.load(path + '/Pieces/blue_guard.png'), 1),
        "blue_guard_two": guard.Guard(5, 0, pygame.image.load(path + '/Pieces/blue_guard.png'), 1),
        "blue_elephant_one": elephant.Elephant(2, 0, pygame.image.load(path + '/Pieces/blue_elephant.png'), 1),
        "blue_elephant_two": elephant.Elephant(6, 0, pygame.image.load(path + '/Pieces/blue_elephant.png'), 1),
        "blue_knight_one": knight.Knight(1, 0, pygame.image.load(path + '/Pieces/blue_knight.png'), 1),
        "blue_knight_two": knight.Knight(7, 0, pygame.image.load(path + '/Pieces/blue_knight.png'), 1),
        "blue_rook_one": rook.Rook(0, 0, pygame.image.load(path + '/Pieces/blue_rook.png'), 1),
        "blue_rook_two": rook.Rook(8, 0, pygame.image.load(path + '/Pieces/blue_rook.png'), 1),
        "blue_pawn_one": pawn.Pawn(0, 3, pygame.image.load(path + '/Pieces/blue_pawn.png'), 1),
        "blue_pawn_two": pawn.Pawn(2, 3, pygame.image.load(path + '/Pieces/blue_pawn.png'), 1),
        "blue_pawn_three": pawn.Pawn(4, 3, pygame.image.load(path + '/Pieces/blue_pawn.png'), 1),
        "blue_pawn_four": pawn.Pawn(6, 3, pygame.image.load(path + '/Pieces/blue_pawn.png'), 1),
        "blue_pawn_five": pawn.Pawn(8, 3, pygame.image.load(path + '/Pieces/blue_pawn.png'), 1),
        "blue_cannon_one": cannon.Cannon(1, 2, pygame.image.load(path + '/Pieces/blue_cannon.png'), 1),
        "blue_cannon_two": cannon.Cannon(7, 2, pygame.image.load(path + '/Pieces/blue_cannon.png'), 1)

    }

def draw_pieces(p_dict, screen):
    """ draws pieces, couldn't put this in another file """
    for piece in p_dict:
        p_dict[piece].draw(screen)

def remove_piece(x_c, y_c, p_dict):
    """ removes the piece at the specified coordinates """
    if board.board_arr[x_c][y_c].is_occupied_none():
        return
    for piece in p_dict:
        if p_dict[piece].x_coord == x_c and p_dict[piece].y_coord == y_c:
            del p_dict[piece]
            board.board_arr[x_c][y_c].occupy_none()
            break



def main():
    """
    main function
    """

    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)

    screen = pygame.display.set_mode((board.SCREEN_WIDTH, board.SCREEN_HEIGHT))
    pygame.display.set_caption("Chinese Chess")
    screen.fill(white)

    # draw board
    board.draw_board(screen, black, board.BOX_SIZE, board.SCREEN_WIDTH / 2, board.SCREEN_HEIGHT / 2)
    pygame.display.update()

    def game_loop():
        game_over = False
        game_close = False
        piece_selected = False
        red_turn = True

        # initialize and draw pieces
        pieces_dict = make_pieces()
        draw_pieces(pieces_dict, screen)
        pygame.display.update()

        sel_p = "red_general"

        while not game_over:

            screen.fill(white)
            board.draw_board(screen, black, board.BOX_SIZE, board.SCREEN_WIDTH/2,
                board.SCREEN_HEIGHT/2)

            draw_pieces(pieces_dict, screen)

            # display who's turn it is
            font_style = pygame.font.SysFont("bahnschrift", 30)
            red_turn_msg = font_style.render("red's turn", True, black)
            blue_turn_msg = font_style.render("blue's turn", True, black)
            if red_turn:
                screen.blit(red_turn_msg, [int(board.SCREEN_WIDTH * .04), int(board.SCREEN_HEIGHT * .5)])
            else:
                screen.blit(blue_turn_msg, [int(board.SCREEN_WIDTH * .04), int(board.SCREEN_HEIGHT * .5)])

            while game_close:
                # adjust display appropriately
                draw_pieces(pieces_dict, screen)
                r_temp = "red_general"
                red_win_msg = font_style.render("red wins!", True, black)
                blue_win_msg = font_style.render("blue wins!", True, black)
                new_game_msg1 = font_style.render("Press q to quit,", True, black)
                new_game_msg2 = font_style.render("space to restart", True, black)

                if r_temp not in pieces_dict:
                    screen.blit(red_win_msg, [int(board.SCREEN_WIDTH * .5), int(board.SCREEN_HEIGHT * .5)])
                else:
                    screen.blit(blue_win_msg, [int(board.SCREEN_WIDTH * .5), int(board.SCREEN_HEIGHT * .5)])
                screen.blit(new_game_msg1, [int(board.SCREEN_WIDTH * .81), int(board.SCREEN_HEIGHT * .5)])
                screen.blit(new_game_msg2, [int(board.SCREEN_WIDTH * .81), int(board.SCREEN_HEIGHT * .55)])
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_SPACE:
                            board.reset_board()
                            pieces_dict = make_pieces()
                            draw_pieces(pieces_dict, screen)
                            pygame.display.update()
                            game_close = False
                            red_turn = True
                pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # selecting or placing a piece
                    pos = pygame.mouse.get_pos()
                    if piece_selected: # if we have a piece selected and are placing it now
                        #check if we have valid place to put piece
                        for x_c in range(9):
                            for y_c in range(10):
                                if (pieces_dict[sel_p].rect.collidepoint(board.board_to_actual(x_c, y_c))) \
                                        and ([x_c, y_c] in pieces_dict[sel_p].available_moves):
                                    # switch turns in needed and remove any pieces in new coordinate
                                    if ([pieces_dict[sel_p].x_coord, pieces_dict[sel_p].y_coord] != [x_c, y_c]):
                                        red_turn = not red_turn
                                        remove_piece(x_c, y_c, pieces_dict)

                                    #place the piece
                                    pieces_dict[sel_p].move(x_c, y_c, pieces_dict[sel_p].x_coord, pieces_dict[sel_p].y_coord)
                                    piece_selected = False

                                    # reset moves
                                    pieces_dict[sel_p].reset_moves()

                                    # detect captured general
                                    r_temp = "red_general"
                                    b_temp = "blue_general"
                                    if r_temp not in pieces_dict:
                                        print("blue wins!")
                                        game_close = True
                                    if b_temp not in pieces_dict:
                                        print("red wins!")
                                        game_close = True

                    else: # we have not selected a piece
                        for piece in pieces_dict:
                            if pieces_dict[piece].rect.collidepoint(pos) and \
                                ((red_turn and not pieces_dict[piece].color) or (not(red_turn) and pieces_dict[piece].color)):
                                piece_selected = True
                                pieces_dict[piece].get_available_moves()
                                sel_p = piece
                if piece_selected: #if we selected a piece but haven't placed it yet
                    (pieces_dict[sel_p].rect.centerx, pieces_dict[sel_p].rect.centery) = pygame.mouse.get_pos()
                    pieces_dict[sel_p].draw(screen)

            pygame.display.update()

    game_loop()
    pygame.quit()

# This line checks if this file is being run directly, or being imported
# Iff run directly, __name__ = __main__
if __name__ == "__main__":
    main()

quit()
