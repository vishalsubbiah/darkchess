from piece import Piece


class Bishop(Piece):
    def get_name(self):
        return "bishop"

    def get_value(self):
        return 3
       
    def get_symbol(self):
        if self.team == "white":
            return 'wb '
        elif self.team == "black":
            return 'bb '
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")

    def get_moves(self, board):
        return []
