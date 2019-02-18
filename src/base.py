import numpy as np
from sty import  fg, bg, rs
import warnings


class Board(object):

    def __init__(self):
        self.board=[[0 for i in range(8)] for j in range(8)]
        self._start_pos()
        self.move_counter = 0
    
    def _start_pos(self):
        # white pieces
        for j in range(8):
            self.board[1][j] =Pawn([1,j], "white")
        self.board[0][0] = Rook([0,0], "white")
        self.board[0][7] = Rook([0,7], "white")
        self.board[0][1] = Knight([0,1], "white")
        self.board[0][6] = Knight([0,6], "white")
        self.board[0][2] = Bishop([0,2], "white")
        self.board[0][5] = Bishop([0,5], "white")
        self.board[0][3] = King([0,3], "white")
        self.board[0][4] = Queen([0,4], "white")

        #black pieces
        for j in range(8):
            self.board[6][j] =Pawn([6,j], "black")
        self.board[7][0] = Rook([0,0], "black")
        self.board[7][7] = Rook([7,7], "black")
        self.board[7][1] = Knight([7,1], "black")
        self.board[7][6] = Knight([7,6], "black")
        self.board[7][2] = Bishop([7,2], "black")
        self.board[7][5] = Bishop([7,5], "black")
        self.board[7][3] = Bishop([7,3], "black")
        self.board[7][4] = Bishop([7,4], "black")

    def __str__(self):
        board_rep="  A  B  C  D  E  F  G  H \n"
        for i in range(7,-1,-1):
            board_rep+=str(i+1)+" "
            for j in range(7,-1,-1):
                    if(i%2==0 and j%2==0):
                        if isinstance(self.board[i][j], Piece):
                            board_rep+= bg.white + fg.black + self.board[i][j].symbol + fg.rs + bg.rs
                        else:
                            board_rep+=u'\u2588'+u'\u2588'+u'\u2588'
                    if(i%2==1 and j%2==0):
                        if isinstance(self.board[i][j], Piece):
                            board_rep+=bg.black + fg.white + self.board[i][j].symbol + fg.rs + bg.rs
                        else:
                            board_rep+="   "
                    if(i%2==0 and j%2==1):
                        if isinstance(self.board[i][j], Piece):
                            board_rep+=self.board[i][j].symbol
                        else:
                            board_rep+="   "
                    if(i%2==1 and j%2==1):
                        if isinstance(self.board[i][j], Piece):
                            board_rep+= bg.white + fg.black + self.board[i][j].symbol + fg.rs + bg.rs
                        else:
                            board_rep+=u'\u2588'+u'\u2588'+u'\u2588'
            board_rep+=" "+str(i+1)
            board_rep+="\n"
        board_rep+="  A  B  C  D  E  F  G  H "
        return board_rep

    def view_board(self):
        print(self.__str__())

    def __repr_(self):
        return self.__str__()
    
    def get_turn(self):
        if self.move_counter%2==0:
            print("white's turn")
            return "white"
        else:
            print("black's turn")
            return "black"
    
    def get_moves(self, pos):
        piece = self.board[pos[0]][pos[1]]
        print(piece)
        return piece.get_moves()

    def choose_move(self):
        team = self.get_turn()
        print(team + " to play")
        print("choose a piece (once chosen have to play that piece)")
        pos_str = input("piece's position:").upper()
        if team =="black":
            col_dict ={'A':0,'B':1, 'C':2 , 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
        else:
            col_dict ={'A':7,'B':6, 'C':5 , 'D':4, 'E':3, 'F':2, 'G':1, 'H':0}
        pos = [int(pos_str[1])-1,col_dict[pos_str[0]]]
        print(pos)
        moves = self.get_moves(pos)
        move_dict = dict()
        for i,move in enumerate(moves):
            move_dict[i]=move
        print(move_dict)
        option=input("move:")
        self.update_board(move_dict[int(option)])

    def update_board(self, move):
        start = move[0]
        end =  move[1]
        key_word = move[2] # 'enpasse' or 'castling' or 'evolve' or 'base'
        if key_word==None:
            key_word='base'

        if key_word=='base':
            # logic wrong, piece will still think its in old location
            self.board[end[0]][end[1]]=self.board[start[0]][start[1]]
            self.board[start[0]][start[1]]=0
            self.board[end[0]][end[1]].set_position(end)
            self.move_counter+=1

        elif key_word=="enpasse":
            warnings.warn("enpasse not implemented yet")
        
        elif key_word=="castling":
            warnings.warn("castling not implemented yet")

        elif key_word=="evolve":
            team = self.get_turn()
            self.board[end[0]][end[1]]=Queen(end,team)
            self.board[start[0]][start[1]]=0
            self.move_counter+=1
            #warnings.warn("evolve not implemented yet")
        
        else:
            raise ValueError("this action:"+key_word+" doesn't exist in the realm of this game")


class Piece(object):

    def __init__(self, pos, team):
        """
        pos: the location of the piece on the board ([x,y])
        team: which team the piece is on ("white", "black")
        """
        self.pos = pos
        self.team = team
        self.name = self.get_name()
        self.value = self.get_value()
        self.symbol = self.get_symbol()
    
    def get_position(self):
        return self.pos
    
    def get_team(self):
        return self.team
    
    def get_name(self):
        raise NotImplementedError("must be implemented")

    def get_moves(self):
        raise NotImplementedError("must be implemented")

    def get_value(self):
        raise NotImplementedError("must be implemented")
        
    def get_symbol(self):
        raise NotImplementedError("must be implemented")
    
    def set_position(self, pos):
        self.pos = pos


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
    
    def get_moves(self):
        pos = self.get_position()
        if self.team == "white":
            if(pos[1]<6):
                return [[pos,[pos[0]+1,pos[1]],'base']]
            elif(pos[1]==6):
                return [[pos,[pos[0]+1,pos[1]],'evolve']]
        elif self.team == "black":
            if(pos[1]>1):
                return [[pos,[pos[0]-1,pos[1]],'base']]
            elif(pos[1]==1):
                return [[pos,[pos[0]-1,pos[1]],'evolve']]
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")


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
    
    def get_moves(self):
        return []


class Bishop(Piece):
    def get_name(self):
        return "bishop"

    def get_value(self):
        return 3
       
    def get_symbol(self):
        if self.team == "white":
            return 'wb '
        elif self.team == "black":
            return 'bb '
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")

    def get_moves(self):
        return []


class Knight(Piece):
    def get_name(self):
        return "knight"

    def get_value(self):
        return 3
       
    def get_symbol(self):
        if self.team == "white":
            return 'wk '
        elif self.team == "black":
            return 'bk '
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")

    def get_moves(self):
        return []


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

    def get_moves(self):
        return []


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
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")
    
    def get_moves(self):
        return []