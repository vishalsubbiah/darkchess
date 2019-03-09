import pytest
import numpy as np
from darkchess.src.board import Board
from darkchess.src.pawn import Pawn
from darkchess.src.dummy_piece import Dummy
from darkchess.src.gamengine import GameEngine
from darkchess.src.utils import clean_board
import os

def test_pawn_moves():
    board = clean_board()
    for j in range(8):
            board[1, j] = Pawn((1, j), "white")
    for j in range(8):
            board[6, j] = Pawn((6, j), "black")
    pawn_board = Board(board)
    game = GameEngine(pawn_board, player1="computer", player2="computer")
    for i in range(10):
        print(i+1)
        while True:
            game = GameEngine(pawn_board, player1="computer", player2="computer")

            moves = game.all_moves()
            if len(moves)==0:
                break
            print(moves)
            game.Board.view_board()
            game.choose_move(moves[0])
            game.Board.view_board()
            input()
