class Piece(object):

    def __init__(self, pos, team=None):
        """
        pos: the location of the piece on the board ([x,y])
        team: which team the piece is on ("white", "black")
        """
        self.pos = pos
        self.team = team
        self.name = self.get_name()
        self.value = self.get_value()
        self.symbol = self.get_symbol()

    def get_position(self):
        return self.pos

    def get_team(self):
        return self.team

    def get_name(self):
        raise NotImplementedError("must be implemented")

    def get_moves(self, board):
        raise NotImplementedError("must be implemented")

    def get_value(self):
        raise NotImplementedError("must be implemented")

    def get_symbol(self):
        raise NotImplementedError("must be implemented")

    def set_position(self, pos):
        self.pos = pos
