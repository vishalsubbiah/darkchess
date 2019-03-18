from darkchess.src.piece import Piece
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
            raise ValueError("this team:" +
                             self.team +
                             " doesn't exist in the realm of this game")

    def get_moves(self, board):
        moves = []
        x,y = self.get_position()
        if self.team == "white":
            pass
        elif self.team == "black":
            pass
        else:
            raise ValueError("this team:"+self.team +
                             " doesn't exist in the realm of this game")
        return moves

    def is_next_move_check(self, new_pos):
        if self.team == "white":
            # find black moves
            pass
        elif self.team == "black":
            #find white moves
            pass
        else:
            raise ValueError("this team:"+self.team +
                             " doesn't exist in the realm of this game")

    def _all_opp_moves_minus_king(self):
        if self.team == "white":
            team = "black"
        if self.team == "black":
            team = "white"
        all_moves_team = []
        for i in range(8):
            for j in range(8):
                if self.Board.board[i, j].team == team and self.Board.board[i, j].get_symbol() is not team[0]+"K":
                    all_moves_team += self.get_moves((i, j))
                if self.Board.board[i, j].team == team and self.Board.board[i, j].get_symbol() == team[0]+"K":
                    opp_king_pos = (i,j)
        return all_moves_team, opp_king_pos