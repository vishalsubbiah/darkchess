from piece import Piece
import numpy as np


class King(Piece):
    def get_name(self):
        return "king"

    def get_value(self):
        return np.inf
       
    def get_symbol(self):
        if self.team == "white":
            return 'wK '
        elif self.team == "black":
            return 'bK '
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")
    
    def get_moves(self):
        return []