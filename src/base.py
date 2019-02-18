import numpy as np
from sty import  fg, bg, rs

class Board(object):

    def __init__(self):
        self.board=[[0 for i in range(8)] for j in range(8)]
        self.start_pos()
        self.move_counter = 0
    
    def start_pos(self):
        # white pieces
        for j in range(8):
            self.board[1][j] =Piece([1,j], "white", 'pawn')
        self.board[0][0] = Piece([0,0], "white", 'rook')
        self.board[0][7] = Piece([0,7], "white", 'rook')
        self.board[0][1] = Piece([0,1], "white", 'knight')
        self.board[0][6] = Piece([0,6], "white", 'knight')
        self.board[0][2] = Piece([0,2], "white", 'bishop')
        self.board[0][5] = Piece([0,5], "white", 'bishop')
        self.board[0][3] = Piece([0,3], "white", 'king')
        self.board[0][4] = Piece([0,4], "white", 'queen')

        #black pieces
        for j in range(8):
            self.board[6][j] =Piece([6,j], "black", 'pawn')
        self.board[7][0] = Piece([0,0], "black", 'rook')
        self.board[7][7] = Piece([7,7], "black", 'rook')
        self.board[7][1] = Piece([7,1], "black", 'knight')
        self.board[7][6] = Piece([7,6], "black", 'knight')
        self.board[7][2] = Piece([7,2], "black", 'bishop')
        self.board[7][5] = Piece([7,5], "black", 'bishop')
        self.board[7][3] = Piece([7,3], "black", 'king')
        self.board[7][4] = Piece([7,4], "black", 'queen')


    def __str__(self):
        board_rep=""
        for i in range(7,-1,-1):
            for j in range(7,-1,-1):
                    if(i%2==0 and j%2==0):
                        if isinstance(self.board[i][j], Piece):
                            board_rep+= bg.white + fg.black + self.board[i][j].symbol + fg.rs + bg.rs
                        else:
                            board_rep+=u'\u2588'+u'\u2588'+u'\u2588'
                    if(i%2==1 and j%2==0):
                        if isinstance(self.board[i][j], Piece):
                            board_rep+=self.board[i][j].symbol
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
            board_rep+="\n"
        return board_rep

    def __repr_(self):
        return self.__str__()
    
    def get_turn(self):
        if self.move_counter%2==0:
            return "white"
        else:
            return "black"

class Piece(object):

    def __init__(self, pos, team, name):
        """
        pos: the location of the piece on the board ([x,y])
        team: which team the piece is on ("white", "black")
        name: name of the piece ("pawn", "knight", "bishop", "rook", "queen", "king")
        """
        self.pos = pos
        self.team = team
        self.name = name
        self.value = self.get_worth()
        self.symbol = self.get_symbol()
    
    def get_position(self):
        return self.pos
    
    def get_team(self):
        return self.team
    
    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value

    def get_moves(self):
        # return all possible moves
        pass

    def get_worth(self):
        if self.name == "pawn":
            return 1
        if self.name == "knight":
            return 3
        if self.name == "bishop":
            return 3
        if self.name == "rook":
            return 5
        if self.name == "queen":
            return 9
        if self.name == "king":
            return np.inf
        else:
            raise ValueError("this piece "+self.name+" doesn't exist in the realm of this game")
        
    def get_symbol(self):
        if self.team == "white":
            if self.name == "pawn":
                return 'wp '
            if self.name == "knight":
                return 'wk '
            if self.name == "bishop":
                return 'wb '
            if self.name == "rook":
                return 'wr '
            if self.name == "queen":
                return 'wq '
            if self.name == "king":
                return 'wK '
            else:
                raise ValueError("this piece "+self.name+" doesn't exist in the realm of this game")

        if self.team == "black":
            if self.name == "pawn":
                return 'bp '
            if self.name == "knight":
                return 'bk '
            if self.name == "bishop":
                return 'bb '
            if self.name == "rook":
                return 'br '
            if self.name == "queen":
                return 'bq '
            if self.name =="king":
                return 'bK '
            else:
                raise ValueError("this piece "+self.name+" doesn't exist in the realm of this game")
        else:
            raise ValueError("this team "+self.team+" doesn't exist in the realm of this game")