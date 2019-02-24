from piece import Piece

class Rook(Piece):
    def get_name(self):
        return "pawn"

    def get_value(self):
        return 5

    def get_symbol(self):
        if self.team == "white":
            return 'wr '
        elif self.team == "black":
            return 'br '
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")

    def get_moves(self, board):
        moves=[]
        pos = self.get_position()
        x,y = pos[0], pos[1]
        if self.team == "white":
            for j in range(y+1,8):
                if board[x,j].team == None:
                    moves.append([pos,[x,j],'base'])
                elif board[x,j].team == "black":
                    moves.append([pos,[x,j],'base'])
                    break
                else:
                    break
            for j in range(y-1,-1,-1):
                if board[x,j].team == None:
                    moves.append([pos,[x,j],'base'])
                elif board[x,j].team == "black":
                    moves.append([pos,[x,j],'base'])
                    break
                else:
                    break
            for i in range(x+1,8):
                if board[i,y].team == None:
                    moves.append([pos,[i,y],'base'])
                elif board[i,y].team == "black":
                    print("here")
                    moves.append([pos,[i,y],'base'])
                    break
                else:
                    break
            for i in range(x-1,-1,-1):
                if board[i,y].team == None:
                    moves.append([pos,[i,y],'base'])
                elif board[i,y].team == "black":
                    print("here")
                    moves.append([pos,[i,y],'base'])
                    break
                else:
                    break
            return moves
        elif self.team == "black":
            for j in range(y+1,8):
                if board[x,j].team == None:
                    moves.append([pos,[x,j],'base'])
                elif board[x,j].team == "white":
                    moves.append([pos,[x,j],'base'])
                    break
                else:
                    break
            for j in range(y-1,-1,-1):
                if board[x,j].team == None:
                    moves.append([pos,[x,j],'base'])
                elif board[x,j].team == "white":
                    moves.append([pos,[x,j],'base'])
                    break
                else:
                    break
            for i in range(x+1,8):
                if board[i,y].team == None:
                    moves.append([pos,[i,y],'base'])
                elif board[i,y].team == "white":
                    moves.append([pos,[i,y],'base'])
                    break
                else:
                    break
            for i in range(x-1,-1,-1):
                if board[i,y].team == None:
                    moves.append([pos,[i,y],'base'])
                elif board[i,y].team == "white":
                    moves.append([pos,[i,y],'base'])
                    break
                else:
                    break
            return moves
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")
