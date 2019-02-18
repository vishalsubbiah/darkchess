from piece import Piece

class Rook(Piece):
    def get_name(self):
        return "pawn"

    def get_value(self):
        return 5
       
    def get_symbol(self):
        if self.team == "white":
            return 'wr '
        elif self.team == "black":
            return 'br '
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")
    
    def get_moves(self, board):
        return []