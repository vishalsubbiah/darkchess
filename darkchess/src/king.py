from darkchess.src.piece import Piece
import numpy as np


class King(Piece):
    """
    King Piece (identical for all both in a normal game)
    """

    def get_name(self):
        """
        Returns name of the Piece
        """
        return "king"

    def get_value(self):
        """
        Returns value of the Piece
        """
        return np.inf

    def get_symbol(self):
        """
        Returns symbol used to represent the Piece on the board
        """
        if self.team == "white":
            return 'wK '
        elif self.team == "black":
            return 'bK '
        else:
            raise ValueError("this team:" +
                             self.team +
                             " doesn't exist in the realm of this game")

    def get_moves(self, board):
        """
        All possible moves for this Piece
        Args:
            board: numpy array of dtype Piece
        Returns list of moves (start_pos,end_pos,type_move)
        """
        moves = []
        x, y = self.get_position()
        # 8 positions
        all_opp_pos, opp_king_pos = self._all_opp_moves_minus_king(board)
        if self.team == "white":
            if(x+1 < 8):
                if (x+1, y) not in all_opp_pos and not self.too_close((x+1, y), opp_king_pos):
                    moves.append(((x, y), (x+1, y), 'base'))
                if(y+1 < 8):
                    if (x+1, y+1) not in all_opp_pos and not self.too_close((x+1, y+1), opp_king_pos):
                        moves.append(((x, y), (x+1, y+1), 'base'))
                    if (x, y+1) not in all_opp_pos and not self.too_close((x, y+1), opp_king_pos):
                        moves.append(((x, y), (x, y+1), 'base'))
                if(y > 0):
                    if (x+1, y-1) not in all_opp_pos and not self.too_close((x+1, y-1), opp_king_pos):
                        moves.append(((x, y), (x+1, y-1), 'base'))
                    if (x, y-1) not in all_opp_pos and not self.too_close((x, y-1), opp_king_pos):
                        moves.append(((x, y), (x, y-1), 'base'))
            if(x > 0):
                if (x-1, y) not in all_opp_pos and not self.too_close((x-1, y), opp_king_pos):
                    moves.append(((x, y), (x-1, y), 'base'))
                if(y+1 < 8):
                    if (x-1, y+1) not in all_opp_pos and not self.too_close((x-1, y+1), opp_king_pos):
                        moves.append(((x, y), (x-1, y+1), 'base'))
                if(y > 0):
                    if (x-1, y-1) not in all_opp_pos and not self.too_close((x-1, y-1), opp_king_pos):
                        moves.append(((x, y), (x-1, y-1), 'base'))

        elif self.team == "black":
            if(x+1 < 8):
                if (x+1, y) not in all_opp_pos and not self.too_close((x+1, y), opp_king_pos):
                    moves.append(((x, y), (x+1, y), 'base'))
                if(y+1 < 8):
                    if (x+1, y+1) not in all_opp_pos and not self.too_close((x+1, y+1), opp_king_pos):
                        moves.append(((x, y), (x+1, y+1), 'base'))
                    if (x, y+1) not in all_opp_pos and not self.too_close((x, y+1), opp_king_pos):
                        moves.append(((x, y), (x, y+1), 'base'))
                if(y > 0):
                    if (x+1, y-1) not in all_opp_pos and not self.too_close((x+1, y-1), opp_king_pos):
                        moves.append(((x, y), (x+1, y-1), 'base'))
                    if (x, y-1) not in all_opp_pos and not self.too_close((x, y-1), opp_king_pos):
                        moves.append(((x, y), (x, y-1), 'base'))
            if(x > 0):
                if (x-1, y) not in all_opp_pos and not self.too_close((x-1, y), opp_king_pos):
                    moves.append(((x, y), (x-1, y), 'base'))
                if(y+1 < 8):
                    if (x-1, y+1) not in all_opp_pos and not self.too_close((x-1, y+1), opp_king_pos):
                        moves.append(((x, y), (x-1, y+1), 'base'))
                if(y > 0):
                    if (x-1, y-1) not in all_opp_pos and not self.too_close((x-1, y-1), opp_king_pos):
                        moves.append(((x, y), (x-1, y-1), 'base'))
        else:
            raise ValueError("this team:"+self.team +
                             " doesn't exist in the realm of this game")
        return moves

    def is_next_move_check(self, new_pos):
        """
        """
        if self.team == "white":
            # find black moves
            pass
        elif self.team == "black":
            # find white moves
            pass
        else:
            raise ValueError("this team:"+self.team +
                             " doesn't exist in the realm of this game")

    def _all_opp_moves_minus_king(self, board):
        """
        Returns all opponent moves except their king's moves
        Args:
            board: numpy array of dtype Piece
        """
        opp_king_pos = None
        if self.team == "white":
            team = "black"
        if self.team == "black":
            team = "white"
        all_moves_team = []
        for i in range(8):
            for j in range(8):
                if board[i, j].team == team and board[i, j].get_symbol() != team[0]+"K ":
                    all_moves_team += board[i, j].get_moves(board)
                if board[i, j].team == team and board[i, j].get_symbol() == team[0]+"K ":
                    opp_king_pos = (i, j)
        all_pos_team = []
        for move in all_moves_team:
            all_pos_team.append(move[1])
        return list(set(all_pos_team)), opp_king_pos

    def too_close(self, pos1, pos2):
        """
        Check if two positions are within sqrt(2) distance of each other
        Used to check if the two kings are adjacent to each other
        Args:
            pos1: position on board
            pos2: position on board
        """
        if pos1 is None or pos2 is None:
            return False
        x1, y1 = pos1
        x2, y2 = pos2
        if (x1-x2)**2 + (y1-y2)**2 <= 2:
            return True
        return False
