from darkchess.src.piece import Piece


class Bishop(Piece):
    """
    Bishop Piece (identical for all 4 in a normal game)
    """

    def get_name(self):
        """
        Returns name of the Piece
        """
        return "bishop"

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
            return 'wb '
        elif self.team == "black":
            return 'bb '
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
            for i in range(min(x, y)):
                new_pos = (x-i-1, y-i-1)
                if board[new_pos].team is None:
                    moves.append((pos, new_pos, 'base'))
                elif board[new_pos].team == "black":
                    moves.append((pos, new_pos, 'base'))
                    break
                else:
                    break

            for i in range(min(7-x, 7-y)):
                new_pos = (x+i+1, y+i+1)
                if board[new_pos].team is None:
                    moves.append((pos, new_pos, 'base'))
                elif board[new_pos].team == "black":
                    moves.append((pos, new_pos, 'base'))
                    break
                else:
                    break

            for i in range(min(x, 7-y)):
                new_pos = (x-i-1, y+i+1)
                if board[new_pos].team is None:
                    moves.append((pos, new_pos, 'base'))
                elif board[new_pos].team == "black":
                    moves.append((pos, new_pos, 'base'))
                    break
                else:
                    break

            for i in range(min(7-x, y)):
                new_pos = (x+i+1, y-i-1)
                if board[new_pos].team is None:
                    moves.append((pos, new_pos, 'base'))
                elif board[new_pos].team == "black":
                    moves.append((pos, new_pos, 'base'))
                    break
                else:
                    break

            return moves
        elif self.team == "black":
            for i in range(min(x, y)):
                new_pos = (x-i-1, y-i-1)
                if board[new_pos].team is None:
                    moves.append((pos, new_pos, 'base'))
                elif board[new_pos].team == "white":
                    moves.append((pos, new_pos, 'base'))
                    break
                else:
                    break

            for i in range(min(7-x, 7-y)):
                new_pos = (x+i+1, y+i+1)
                if board[new_pos].team is None:
                    moves.append((pos, new_pos, 'base'))
                elif board[new_pos].team == "white":
                    moves.append((pos, new_pos, 'base'))
                    break
                else:
                    break

            for i in range(min(x, 7-y)):
                new_pos = (x-i-1, y+i+1)
                if board[new_pos].team is None:
                    moves.append((pos, new_pos, 'base'))
                elif board[new_pos].team == "white":
                    moves.append((pos, new_pos, 'base'))
                    break
                else:
                    break

            for i in range(min(7-x, y)):
                new_pos = (x+i+1, y-i-1)
                if board[new_pos].team is None:
                    moves.append((pos, new_pos, 'base'))
                elif board[new_pos].team == "white":
                    moves.append((pos, new_pos, 'base'))
                    break
                else:
                    break
            return moves
        else:
            raise ValueError("this team:" +
                             self.team +
                             " doesn't exist in the realm of this game")
