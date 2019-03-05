from board import Board
from gamengine import GameEngine

board = Board()
game = GameEngine(board)

while True:
    game.board.view_board_debug()
    game.board.view_board()
    game.choose_move()
