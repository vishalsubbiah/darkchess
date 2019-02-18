from piece import Piece


class Queen(Piece):
    def get_name(self):
        return "queen"

    def get_value(self):
        return 9
       
    def get_symbol(self):
        if self.team == "white":
            return 'wq '
        elif self.team == "black":
            return 'bq '
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")

    def get_moves(self):
        return []