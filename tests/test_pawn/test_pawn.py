import pytest
import numpy as np
from darkchess.src.board import Board
from darkchess.src.pawn import Pawn
from darkchess.src.piece import Piece
from darkchess.src.gamengine import GameEngine


def test_pawn_moves():
    board = np.zeros((8,8),dtype=Piece)
    for j in range(8):
            board[1, j] = Pawn((1, j), "white")
    for j in range(8):
            board[6, j] = Pawn((6, j), "black")
    pawn_board = Board(board)
    game = GameEngine(pawn_board)

    with open("./moves.txt",'r') as f:
        for move in f.readlines():
            print(move)

