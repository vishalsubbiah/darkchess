from sty import  fg, bg, rs
from piece import Piece
from pawn import Pawn
from rook import Rook
from bishop import Bishop
from knight import Knight
from queen import Queen
from king import King
from dummy_piece import Dummy
import warnings
import numpy as np

class Board(object):

    def __init__(self):
        self.board = np.empty((8,8),dtype=Piece)
        self._start_pos()
        self.move_counter = 0

    def _start_pos(self):
        # white pieces
        for j in range(8):
            self.board[1,j] =Pawn([1,j], "white")
        self.board[0,0] = Rook([0,0], "white")
        self.board[0,7] = Rook([0,7], "white")
        self.board[0,1] = Knight([0,1], "white")
        self.board[0,6] = Knight([0,6], "white")
        self.board[0,2] = Bishop([0,2], "white")
        self.board[0,5] = Bishop([0,5], "white")
        self.board[0,3] = King([0,3], "white")
        self.board[0,4] = Queen([0,4], "white")

        #black pieces
        for j in range(8):
            self.board[6,j] =Pawn([6,j], "black")
        self.board[7,0] = Rook([7,0], "black")
        self.board[7,7] = Rook([7,7], "black")
        self.board[7,1] = Knight([7,1], "black")
        self.board[7,6] = Knight([7,6], "black")
        self.board[7,2] = Bishop([7,2], "black")
        self.board[7,5] = Bishop([7,5], "black")
        self.board[7,3] = Bishop([7,3], "black")
        self.board[7,4] = Bishop([7,4], "black")

        for i in range(2,6):
            for j in range(8):
                self.board[i,j] = Dummy([i,j], None)

    def __str__(self):
        board_rep="  A  B  C  D  E  F  G  H \n"
        for i in range(7,-1,-1):
            board_rep+=str(i+1)+" "
            for j in range(0,8,1):
                if(i%2==0 and j%2==1):
                    board_rep+= bg.white + fg.black + self.board[i][j].symbol + fg.rs + bg.rs
                if(i%2==1 and j%2==1):
                    board_rep+=bg.black + fg.white + self.board[i][j].symbol + fg.rs + bg.rs
                if(i%2==0 and j%2==0):
                    board_rep+=bg.black + fg.white + self.board[i][j].symbol + fg.rs + bg.rs
                if(i%2==1 and j%2==0):
                    board_rep+= bg.white + fg.black + self.board[i][j].symbol + fg.rs + bg.rs

            board_rep+=" "+str(i+1)
            board_rep+="\n"
        board_rep+="  A  B  C  D  E  F  G  H "
        return board_rep

    def view_board(self):
        print(self.__str__())

    def view_board_debug(self):
        board_rep=""
        for i in range(0,8,1):
            for j in range(0,8,1):
                if(i%2==1 and j%2==1):
                    board_rep+= bg.white + fg.black + self.board[i][j].symbol + fg.rs + bg.rs
                if(i%2==0 and j%2==1):
                    board_rep+=bg.black + fg.white + self.board[i][j].symbol + fg.rs + bg.rs
                if(i%2==1 and j%2==0):
                    board_rep+=bg.black + fg.white + self.board[i][j].symbol + fg.rs + bg.rs
                if(i%2==0 and j%2==0):
                    board_rep+= bg.white + fg.black + self.board[i][j].symbol + fg.rs + bg.rs

            board_rep+="\n"
        print(board_rep)

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
        piece = self.board[pos[0],pos[1]]
        return piece.get_moves(self.board)

    def choose_move(self):
        team = self.get_turn()
        print(team + " to play")
        print("choose a piece (once chosen have to play that piece)")
        pos_str = input("piece's position:").upper()

        col_dict ={'A':0,'B':1, 'C':2 , 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
        pos = [int(pos_str[1])-1,col_dict[pos_str[0]]]
        if isinstance(self.board[pos[0],pos[1]],Piece):
            print("piece chosen: "+self.board[pos[0]][pos[1]].symbol)
            if self.board[pos[0],pos[1]].team == team:
                moves = self.get_moves(pos)
                move_dict = dict()
                for i,move in enumerate(moves):
                    move_dict[i+1]=move
                print(move_dict)
                option=input("move:")
                self.update_board(move_dict[int(option)])
            else:
                print("wrong team tried to play. choose again")
                self.choose_move()
        else:
            print("chose a tile with no piece. choose again")
            self.choose_move()


    def update_board(self, move):
        start = move[0]
        end =  move[1]
        key_word = move[2] # 'enpasse' or 'castling' or 'evolve' or 'base'
        if key_word==None:
            key_word='base'

        if key_word=='base':
            # logic wrong, piece will still think its in old location
            self.board[end[0],end[1]]=self.board[start[0],start[1]]
            self.board[start[0],start[1]]=Dummy([start[0],start[1]])
            self.board[end[0],end[1]].set_position(end)
            self.move_counter+=1

        elif key_word=="enpasse":
            warnings.warn("enpasse not implemented yet")

        elif key_word=="castling":
            warnings.warn("castling not implemented yet")

        elif key_word=="evolve":
            team = self.get_turn()
            self.board[end[0],end[1]]=Queen(end,team)
            self.board[start[0],start[1]]=Dummy([start[0],start[1]])
            self.move_counter+=1
            #warnings.warn("evolve not implemented yet")

        else:
            raise ValueError("this action:"+key_word+" doesn't exist in the realm of this game")

