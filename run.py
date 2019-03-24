from darkchess.src.board import Board
from darkchess.src.gamengine import GameEngine
from darkchess.src.darkboard import DarkBoard

dark_mode = False
if dark_mode:
    board = DarkBoard()
else:
    board = Board()
game = GameEngine(board)

while True:
    game.Board.view_board_debug()
    game.Board.view_board()
    if dark_mode:
        game.Board.view_board_true_sight()
    game.choose_move()
