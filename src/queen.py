from piece import Piece


class Queen(Piece):
    def get_name(self):
        return "queen"

    def get_value(self):
        return 9

    def get_symbol(self):
        if self.team == "white":
            return 'wq '
        elif self.team == "black":
            return 'bq '
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")

    def get_moves(self, board):
        moves=[]
        pos = self.get_position()
        x,y = pos
        if self.team == "white":
            # rook moves
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
            # bishop moves
            for i in range(min(x,y)):
                if board[x-i-1,y-i-1].team == None:
                    moves.append([pos,[x-i-1,y-i-1],'base'])
                elif board[x-i-1,y-i-1].team == "black":
                    moves.append([pos,[x-i-1,y-i-1],'base'])
                    break
                else:
                    break

            for i in range(min(7-x,7-y)):
                if board[x+i+1,y+i+1].team == None:
                    moves.append([pos,[x+i+1,y+i+1],'base'])
                elif board[x+i+1,y+i+1].team == "black":
                    moves.append([pos,[x+i+1,y+i+1],'base'])
                    break
                else:
                    break

            for i in range(min(x,7-y)):
                if board[x-i-1,y+i+1].team == None:
                    moves.append([pos,[x-i-1,y+i+1],'base'])
                elif board[x-i-1,y+i+1].team == "black":
                    moves.append([pos,[x-i-1,y+i+1],'base'])
                    break
                else:
                    break

            for i in range(min(7-x,y)):
                if board[x+i+1,y-i-1].team == None:
                    moves.append([pos,[x+i+1,y-i-1],'base'])
                elif board[x+i+1,y-i-1].team == "black":
                    moves.append([pos,[x+i+1,y-i-1],'base'])
                    break
                else:
                    break
            return moves
        elif self.team == "black":
            # rook moves
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
            #bishop moves
            for i in range(min(x,y)):
                if board[x-i-1,y-i-1].team == None:
                    moves.append([pos,[x-i-1,y-i-1],'base'])
                elif board[x-i-1,y-i-1].team == "white":
                    moves.append([pos,[x-i-1,y-i-1],'base'])
                    break
                else:
                    break

            for i in range(min(7-x,7-y)):
                if board[x+i+1,y+i+1].team == None:
                    moves.append([pos,[x+i+1,y+i+1],'base'])
                elif board[x+i+1,y+i+1].team == "white":
                    moves.append([pos,[x+i+1,y+i+1],'base'])
                    break
                else:
                    break

            for i in range(min(x,7-y)):
                if board[x-i-1,y+i+1].team == None:
                    moves.append([pos,[x-i-1,y+i+1],'base'])
                elif board[x-i-1,y+i+1].team == "white":
                    moves.append([pos,[x-i-1,y+i+1],'base'])
                    break
                else:
                    break

            for i in range(min(7-x,y)):
                if board[x+i+1,y-i-1].team == None:
                    moves.append([pos,[x+i+1,y-i-1],'base'])
                elif board[x+i+1,y-i-1].team == "white":
                    moves.append([pos,[x+i+1,y-i-1],'base'])
                    break
                else:
                    break
            return moves

        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")