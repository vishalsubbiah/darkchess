from piece import Piece


class Pawn(Piece):
    def get_name(self):
        return "pawn"

    def get_value(self):
        return 1
       
    def get_symbol(self):
        if self.team == "white":
            return 'wp '
        elif self.team == "black":
            return 'bp '
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")
    
    def get_moves(self, board):
        pos = self.get_position()
        if self.team == "white":
            if pos[0]==1:
                return [[pos,[pos[0]+1,pos[1]],'base'],[pos,[pos[0]+2,pos[1]],'base']]
            if(pos[0]<6):
                return [[pos,[pos[0]+1,pos[1]],'base']]
            elif(pos[0]==6):
                return [[pos,[pos[0]+1,pos[1]],'evolve']]
        elif self.team == "black":
            if(pos[0]==6):
                return [[pos,[pos[0]-1,pos[1]],'base'],[pos,[pos[0]-2,pos[1]],'base']]
            if(pos[0]>1):
                return [[pos,[pos[0]-1,pos[1]],'base']]
            elif(pos[0]==1):
                return [[pos,[pos[0]-1,pos[1]],'evolve']]
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")
