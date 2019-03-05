from piece import Piece
import numpy as np


class Dummy(Piece):
    def get_name(self):
        return "dummy"

    def get_value(self):
        return 0

    def get_symbol(self):
        return "   "

    def get_moves(self, board):
        return []
