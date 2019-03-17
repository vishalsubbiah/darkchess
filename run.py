from darkchess.src.board import Board
from darkchess.src.gamengine import GameEngine

board = Board()
game = GameEngine(board)

while True:
    game.Board.view_board_debug()
    game.Board.view_board()
    game.choose_move()

