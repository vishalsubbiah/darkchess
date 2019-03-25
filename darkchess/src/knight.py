from darkchess.src.piece import Piece


class Knight(Piece):
    """
    Knight Piece (identical for all 4 in a normal game)
    """

    def get_name(self):
        """
        Returns name of the Piece
        """
        return "knight"

    def get_value(self):
        """
        Returns value of the Piece
        """
        return 3

    def get_symbol(self):
        """
        Returns symbol used to represent the Piece on the board
        """
        if self.team == "white":
            return 'wk '
        elif self.team == "black":
            return 'bk '
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
        pos = self.get_position()
        x, y = pos
        if self.team == "white":
            if x-2 >= 0 and y-1 >= 0:
                if board[x-2, y-1].team is not "white":
                    moves.append((pos, (x-2, y-1), "base"))

            if x-2 >= 0 and y+1 <= 7:
                if board[x-2, y+1].team is not "white":
                    moves.append((pos, (x-2, y+1), "base"))

            if x-1 >= 0 and y-2 >= 0:
                if board[x-1, y-2].team is not "white":
                    moves.append((pos, (x-1, y-2), "base"))

            if x+1 <= 7 and y-2 >= 0:
                if board[x+1, y-2].team is not "white":
                    moves.append((pos, (x+1, y-2), "base"))
            if x+2 <= 7 and y-1 >= 0:
                if board[x+2, y-1].team is not "white":
                    moves.append((pos, (x+2, y-1), "base"))

            if x+2 <= 7 and y+1 <= 7:
                if board[x+2, y+1].team is not "white":
                    moves.append((pos, (x+2, y+1), "base"))

            if x+1 <= 7 and y+2 <= 7:
                if board[x+1, y+2].team is not "white":
                    moves.append((pos, (x+1, y+2), "base"))
            if x-1 >= 0 and y+2 <= 7:
                if board[x-1, y+2].team is not "white":
                    moves.append((pos, (x-1, y+2), "base"))

            return moves
        elif self.team == "black":
            if x-2 >= 0 and y-1 >= 0:
                if board[x-2, y-1].team is not "black":
                    moves.append((pos, (x-2, y-1), "base"))

            if x-2 >= 0 and y+1 <= 7:
                if board[x-2, y+1].team is not "black":
                    moves.append((pos, (x-2, y+1), "base"))

            if x-1 >= 0 and y-2 >= 0:
                if board[x-1, y-2].team is not "black":
                    moves.append((pos, (x-1, y-2), "base"))

            if x+1 <= 7 and y-2 >= 0:
                if board[x+1, y-2].team is not "black":
                    moves.append((pos, (x+1, y-2), "base"))
            if x+2 <= 7 and y-1 >= 0:
                if board[x+2, y-1].team is not "black":
                    moves.append((pos, (x+2, y-1), "base"))

            if x+2 <= 7 and y+1 <= 7:
                if board[x+2, y+1].team is not "black":
                    moves.append((pos, (x+2, y+1), "base"))

            if x+1 <= 7 and y+2 <= 7:
                if board[x+1, y+2].team is not "black":
                    moves.append((pos, (x+1, y+2), "base"))
            if x-1 >= 0 and y+2 <= 7:
                if board[x-1, y+2].team is not "black":
                    moves.append((pos, (x-1, y+2), "base"))

            return moves
        else:
            raise ValueError("this team:" +
                             self.team +
                             " doesn't exist in the realm of this game")
    def copy(self):
        new_piece = Knight(self.pos,self.team)
        return new_piece