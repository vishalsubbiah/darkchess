from piece import Piece

class GameEngine():

    def __init__(self, board):
        self.move_counter = 0
        self.board = board
        self.prev_board = board

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
                if moves == []:
                    print("no moves available for that piece")
                    self.choose_move()
                move_dict = dict()
                for i,move in enumerate(moves):
                    move_dict[i+1]=move
                print(self.translate(move_dict))
                option=input("move:")
                self.prev_board = self.board
                self.board.update_board(move_dict[int(option)])
            else:
                print("wrong team tried to play. choose again")
                self.choose_move()
        else:
            print("chose a tile with no piece. choose again")
            self.choose_move()

    def undo_move(self):
        self.board = self.prev_board
        self.move_counter -= 1

    def translate(self, move_dict):
        new_dict={}
        revcol_dict ={0:'A',1:'B', 2:'C' , 3:'D', 4:'E', 5:'F', 6:'G', 7:'H'}
        for key, val in move_dict.items():
            start = val[0]
            end = val[1]
            new_start = revcol_dict[start[1]]+ str(start[0]+1)
            new_end = revcol_dict[end[1]]+ str(end[0]+1)
            new_dict[key]=[new_start,new_end]
        return new_dict