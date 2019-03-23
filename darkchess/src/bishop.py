from darkchess.src.piece import Piece


class Bishop(Piece):
    def get_name(self):
        """
        """
        return "bishop"

    def get_value(self):
        """
        """
        return 3

    def get_symbol(self):
        """
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
