from sty import fg, bg, rs
from darkchess.src.piece import Piece
from darkchess.src.pawn import Pawn
from darkchess.src.rook import Rook
from darkchess.src.bishop import Bishop
from darkchess.src.knight import Knight
from darkchess.src.queen import Queen
from darkchess.src.king import King
from darkchess.src.dummy_piece import Dummy
import warnings
import numpy as np
from darkchess.src.utils import clean_board


class Board(object):

    def __init__(self, starting_board=None):
        self.board = np.empty((8, 8), dtype=Piece)
        if starting_board is None:
            self._start_pos()
        else:
            self.board = starting_board

    def _start_pos(self):
        # white pieces
        self.board = clean_board()
        for j in range(8):
            self.board[1, j] = Pawn((1, j), "white")
        self.board[0, 0] = Rook((0, 0), "white")
        self.board[0, 7] = Rook((0, 7), "white")
        self.board[0, 1] = Knight((0, 1), "white")
        self.board[0, 6] = Knight((0, 6), "white")
        self.board[0, 2] = Bishop((0, 2), "white")
        self.board[0, 5] = Bishop((0, 5), "white")
        self.board[0, 4] = King((0, 4), "white")
        self.board[0, 3] = Queen((0, 3), "white")

        # black pieces
        for j in range(8):
            self.board[6, j] = Pawn((6, j), "black")
        self.board[7, 0] = Rook((7, 0), "black")
        self.board[7, 7] = Rook((7, 7), "black")
        self.board[7, 1] = Knight((7, 1), "black")
        self.board[7, 6] = Knight((7, 6), "black")
        self.board[7, 2] = Bishop((7, 2), "black")
        self.board[7, 5] = Bishop((7, 5), "black")
        self.board[7, 4] = King((7, 4), "black")
        self.board[7, 3] = Queen((7, 3), "black")

    def __str__(self):
        board_rep = "  A  B  C  D  E  F  G  H \n"
        for i in range(7, -1, -1):
            board_rep += str(i+1)+" "
            for j in range(0, 8, 1):
                if(i % 2 == 0 and j % 2 == 1):
                    board_rep += bg.white + fg.black + \
                        self.board[i, j].symbol + fg.rs + bg.rs
                if(i % 2 == 1 and j % 2 == 1):
                    board_rep += bg.black + fg.white + \
                        self.board[i, j].symbol + fg.rs + bg.rs
                if(i % 2 == 0 and j % 2 == 0):
                    board_rep += bg.black + fg.white + \
                        self.board[i, j].symbol + fg.rs + bg.rs
                if(i % 2 == 1 and j % 2 == 0):
                    board_rep += bg.white + fg.black + \
                        self.board[i, j].symbol + fg.rs + bg.rs

            board_rep += " "+str(i+1)
            board_rep += "\n"
        board_rep += "  A  B  C  D  E  F  G  H "
        return board_rep

    def view_board(self):
        print(self.__str__())

    def view_board_debug(self):
        board_rep = ""
        for i in range(0, 8, 1):
            for j in range(0, 8, 1):
                if(i % 2 == 0 and j % 2 == 1):
                    board_rep += bg.white + fg.black + \
                        self.board[i, j].symbol + fg.rs + bg.rs
                if(i % 2 == 0 and j % 2 == 0):
                    board_rep += bg.black + fg.white + \
                        self.board[i, j].symbol + fg.rs + bg.rs
                if(i % 2 == 1 and j % 2 == 1):
                    board_rep += bg.black + fg.white + \
                        self.board[i, j].symbol + fg.rs + bg.rs
                if(i % 2 == 1 and j % 2 == 0):
                    board_rep += bg.white + fg.black + \
                        self.board[i, j].symbol + fg.rs + bg.rs

            board_rep += "\n"
        print(board_rep)

    def __repr_(self):
        return self.__str__()

    def update_board(self, move, team):
        start = move[0]
        end = move[1]
        key_word = move[2]  # 'enpasse' or 'castling' or 'evolve' or 'base'
        if key_word == None:
            key_word = 'base'

        if key_word == 'base':
            self.board[end] = self.board[start]
            self.board[start] = Dummy(start)
            self.board[end].set_position(end)

        elif key_word == "enpasse":
            warnings.warn("enpasse not implemented yet")

        elif key_word == "castling":
            warnings.warn("castling not implemented yet")

        elif key_word == "evolve":
            self.board[end] = Queen(end, team)
            self.board[start] = Dummy(start)

        else:
            raise ValueError("this action:"+key_word +
                             " doesn't exist in the realm of this game")
