from darkchess.src.piece import Piece


class Rook(Piece):
    """
    Rook Piece (identical for all 4 in a normal game)
    """

    def get_name(self):
        """
        Returns name of the Piece
        """
        return "rook"

    def get_value(self):
        """
        Returns value of the Piece
        """
        return 5

    def get_symbol(self):
        """
        Returns symbol used to represent the Piece on the board
        """
        if self.team == "white":
            return 'wr '
        elif self.team == "black":
            return 'br '
        else:
            raise ValueError("this team:"+self.team +
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
        x, y = pos[0], pos[1]
        if self.team == "white":
            for j in range(y+1, 8):
                if board[x, j].team == None:
                    moves.append((pos, (x, j), 'base'))
                elif board[x, j].team == "black":
                    moves.append((pos, (x, j), 'base'))
                    break
                else:
                    break
            for j in range(y-1, -1, -1):
                if board[x, j].team == None:
                    moves.append((pos, (x, j), 'base'))
                elif board[x, j].team == "black":
                    moves.append((pos, (x, j), 'base'))
                    break
                else:
                    break
            for i in range(x+1, 8):
                if board[i, y].team == None:
                    moves.append((pos, (i, y), 'base'))
                elif board[i, y].team == "black":
                    moves.append((pos, (i, y), 'base'))
                    break
                else:
                    break
            for i in range(x-1, -1, -1):
                if board[i, y].team == None:
                    moves.append((pos, (i, y), 'base'))
                elif board[i, y].team == "black":
                    moves.append((pos, (i, y), 'base'))
                    break
                else:
                    break
            return moves
        elif self.team == "black":
            for j in range(y+1, 8):
                if board[x, j].team == None:
                    moves.append((pos, (x, j), 'base'))
                elif board[x, j].team == "white":
                    moves.append((pos, (x, j), 'base'))
                    break
                else:
                    break
            for j in range(y-1, -1, -1):
                if board[x, j].team == None:
                    moves.append((pos, (x, j), 'base'))
                elif board[x, j].team == "white":
                    moves.append((pos, (x, j), 'base'))
                    break
                else:
                    break
            for i in range(x+1, 8):
                if board[i, y].team == None:
                    moves.append((pos, (i, y), 'base'))
                elif board[i, y].team == "white":
                    moves.append((pos, (i, y), 'base'))
                    break
                else:
                    break
            for i in range(x-1, -1, -1):
                if board[i, y].team == None:
                    moves.append((pos, (i, y), 'base'))
                elif board[i, y].team == "white":
                    moves.append((pos, (i, y), 'base'))
                    break
                else:
                    break
            return moves
        else:
            raise ValueError("this team:"+self.team +
                             " doesn't exist in the realm of this game")

    def copy(self):
        new_piece = Rook(self.pos, self.team)
        return new_piece
