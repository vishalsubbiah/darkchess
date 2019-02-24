from board import Board



board = Board()
while True:
    board.view_board_debug()
    board.view_board()
    board.choose_move()
