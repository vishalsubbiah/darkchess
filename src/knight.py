from piece import Piece


class Knight(Piece):
    def get_name(self):
        return "knight"

    def get_value(self):
        return 3
       
    def get_symbol(self):
        if self.team == "white":
            return 'wk '
        elif self.team == "black":
            return 'bk '
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")

    def get_moves(self):
        return []
