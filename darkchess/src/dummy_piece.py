from darkchess.src.piece import Piece
import numpy as np


class Dummy(Piece):
    """
    Dummy Piece to represent tiles on chess board with neither white or black pieces
    """

    def get_name(self):
        """
        Returns name of the Piece
        """
        return "dummy"

    def get_value(self):
        """
        Returns value of the Piece
        """
        return 0

    def get_symbol(self):
        """
        Returns symbol used to represent the Piece on the board
        """
        return "   "

    def get_moves(self, board):
        """
        All possible moves for this Piece
        Args:
            board: numpy array of dtype Piece
        Returns list of moves (start_pos,end_pos,type_move)
        """
        return []
