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

    def all_opp_moves_minus_king(self, board):
        moves = []
        if self.team =="white":
            team = "black"
        if self.team =="black":
            team = "white"
        for i in range(8):
            for j in range(8):
                if board[i,j].team==team and board[i,j].symbol!=team[0]+'K ':
                    piece = board[i,j]
                    moves+=piece.get_moves(board)
        return moves

    def is_check(self, board):
        if self.team=="white":
            for i in range(8):
                for j in range(8):
                    if board[i,j].symbol=='wK':
                        king=board[i,j]
                        break
            opp_pos = king.extract_endpos_moves(self.all_opp_moves_minus_king(board))
            if king.get_position() in opp_pos:
                print("white king in check")
                return 1
            return 0
        if self.team=="black":
            for i in range(8):
                for j in range(8):
                    if board[i,j].symbol=='bK':
                        king=board[i,j]
                        break
            opp_pos = king.extract_endpos_moves(self.all_opp_moves_minus_king(board))
            if king.get_position() in opp_pos:
                print("black king in check")
                return 1
            return 0