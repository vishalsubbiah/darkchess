from darkchess.src.piece import Piece


class Pawn(Piece):
    """
    Pawn Piece (identical for all in a game)
    """

    def get_name(self):
        """
        Returns name of the Piece
        """
        return "pawn"

    def get_value(self):
        """
        Returns value of the Piece
        """
        return 1

    def get_symbol(self):
        """
        Returns symbol used to represent the Piece on the board
        """
        if self.team == "white":
            return 'wp '
        elif self.team == "black":
            return 'bp '
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

            if x == 1:
                if board[x+1, y].team is None:
                    moves.append((pos, (x+1, y), 'base'))
                if board[x+2, y].team is None:
                    moves.append((pos, (x+2, y), 'base'))
                if y-1 >= 0:
                    if board[x+1, y-1].team is "black":
                        moves.append((pos, (x+1, y-1), 'base'))
                if y+1 < 8:
                    if board[x+1, y+1].team is "black":
                        moves.append((pos, (x+1, y+1), 'base'))

                return moves
            if x < 6:
                if board[x+1, y].team is None:
                    moves.append((pos, (x+1, y), 'base'))
                if y-1 >= 0:
                    if board[x+1, y-1].team is "black":
                        moves.append((pos, (x+1, y-1), 'base'))
                if y+1 < 8:
                    if board[x+1, y+1].team is "black":
                        moves.append((pos, (x+1, y+1), 'base'))
                return moves
            elif x == 6:
                if board[x+1, y].team is None:
                    moves.append((pos, (x+1, y), 'evolve'))
                if y-1 >= 0:
                    if board[x+1, y-1].team is "black":
                        moves.append((pos, (x+1, y-1), 'evolve'))
                if y+1 < 8:
                    if board[x+1, y+1].team is "black":
                        moves.append((pos, (x+1, y+1), 'evolve'))
                return moves

        elif self.team == "black":

            if x == 6:
                if board[x-1, y].team is None:
                    moves.append((pos, (x-1, y), 'base'))
                if board[x-2, y].team is None:
                    moves.append((pos, (x-2, y), 'base'))
                if y-1 >= 0:
                    if board[x-1, y-1].team is "white":
                        moves.append((pos, (x-1, y-1), 'base'))
                if y+1 < 8:
                    if board[x-1, y+1].team is "white":
                        moves.append((pos, (x-1, y+1), 'base'))
                return moves

            if x > 1:
                if board[x-1, y].team is None:
                    moves.append((pos, (x-1, y), 'base'))
                if y-1 >= 0:
                    if board[x-1, y-1].team is "white":
                        moves.append((pos, (x-1, y-1), 'base'))
                if y+1 < 8:
                    if board[x-1, y+1].team is "white":
                        moves.append((pos, (x-1, y+1), 'base'))
                return moves
            elif x == 1:
                if board[x-1, y].team is None:
                    moves.append((pos, (x-1, y), 'evolve'))
                if y-1 >= 0:
                    if board[x-1, y-1].team is "white":
                        moves.append((pos, (x-1, y-1), 'evolve'))
                if y + 1 < 8:
                    if board[x-1, y+1].team is "white":
                        moves.append((pos, (x-1, y+1), 'evolve'))
                return moves
        else:
            raise ValueError("this team:" +
                             self.team +
                             " doesn't exist in the realm of this game")
