import pytest
import numpy as np
from darkchess.src.board import Board
from darkchess.src.rook import Rook
from darkchess.src.dummy_piece import Dummy
from darkchess.src.gamengine import GameEngine
from darkchess.src.utils import clean_board



def test_stalemate_3moves():
    """
    Places 8 Pawns along two rows and plays 100 games with
    random moves to test the mechanics
    """
    pass

def test_stalemate_nomoves():
    pass