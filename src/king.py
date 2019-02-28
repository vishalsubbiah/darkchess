from piece import Piece
import numpy as np


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

    def get_moves(self, board):
        moves=[]
        pos = self.get_position()
        x,y = pos
        opp_king_pos = self.find_opp_king(board)
        if self.team == "white":
            opp_pos = self.extract_endpos_moves(self.all_opp_moves_minus_king(board))
            if(x>0):
                if board[x-1,y].team is None and [x-1,y] not in opp_pos and not self.too_close([x-1,y],opp_king_pos):
                    moves.append([pos,[x-1,y],'base'])
            if(x>0 and y>0):
                if board[x-1,y-1].team is None and [x-1,y-1] not in opp_pos and not self.too_close([x-1,y-1],opp_king_pos):
                    moves.append([pos,[x-1,y-1],'base'])
                if board[x,y-1].team is None and [x,y-1] not in opp_pos and not self.too_close([x,y-1],opp_king_pos):
                    moves.append([pos,[x,y-1],'base'])
            if (x>0 and y<7):
                if board[x-1,y+1].team is None and [x-1,y+1] not in opp_pos and not self.too_close([x-1,y+1],opp_king_pos):
                    moves.append([pos,[x-1,y+1],'base'])
                if board[x,y+1].team is None and [x,y+1] not in opp_pos and not self.too_close([x,y+1],opp_king_pos):
                    moves.append([pos,[x,y+1],'base'])
            if(x<7):
                if board[x+1,y].team is None and [x+1,y] not in opp_pos and not self.too_close([x+1,y],opp_king_pos):
                    moves.append([pos,[x+1,y],'base'])
            if(x<7 and y>0):
                if board[x+1,y-1].team is None and [x+1,y-1] not in opp_pos and not self.too_close([x+1,y-1],opp_king_pos):
                    moves.append([pos,[x+1,y-1],'base'])
            if(x<7 and y<7):
                if board[x+1,y+1].team is None and [x+1,y+1] not in opp_pos and not self.too_close([x+1,y+1],opp_king_pos):
                    moves.append([pos,[x+1,y+1],'base'])
            return moves

        elif self.team == "black":
            opp_pos = self.extract_endpos_moves(self.all_opp_moves_minus_king(board))
            if(x>0):
                if board[x-1,y].team is None and [x-1,y] not in opp_pos and not self.too_close([x-1,y],opp_king_pos):
                    moves.append([pos,[x-1,y],'base'])
            if(x>0 and y>0):
                if board[x-1,y-1].team is None and [x-1,y-1] not in opp_pos and not self.too_close([x-1,y-1],opp_king_pos):
                    moves.append([pos,[x-1,y-1],'base'])
                if board[x,y-1].team is None and [x,y-1] not in opp_pos and not self.too_close([x,y-1],opp_king_pos):
                    moves.append([pos,[x,y-1],'base'])
            if (x>0 and y<7):
                if board[x-1,y+1].team is None and [x-1,y+1] not in opp_pos and not self.too_close([x-1,y+1],opp_king_pos):
                    moves.append([pos,[x-1,y+1],'base'])
                if board[x,y+1].team is None and [x,y+1] not in opp_pos and not self.too_close([x,y+1],opp_king_pos):
                    moves.append([pos,[x,y+1],'base'])
            if(x<7):
                if board[x+1,y].team is None and [x+1,y] not in opp_pos and not self.too_close([x+1,y],opp_king_pos):
                    moves.append([pos,[x+1,y],'base'])
            if(x<7 and y>0):
                if board[x+1,y-1].team is None and [x+1,y-1] not in opp_pos and not self.too_close([x+1,y-1],opp_king_pos):
                    moves.append([pos,[x+1,y-1],'base'])
            if(x<7 and y<7):
                if board[x+1,y+1].team is None and [x+1,y+1] not in opp_pos and not self.too_close([x+1,y+1],opp_king_pos):
                    moves.append([pos,[x+1,y+1],'base'])
            return moves
        else:
            raise ValueError("this team:"+self.team+" doesn't exist in the realm of this game")

    def extract_endpos_moves(self,moves):
        all_pos = []
        for move in moves:
            all_pos.append((move[1][0],move[1][1]))
        return list(set(all_pos))

    def find_opp_king(self, board):
        if self.team=="white":
            for i in range(8):
                for j in range(8):
                    if board[i,j].get_symbol()=='bK':
                        return (i,j)
        if self.team=="black":
            for i in range(8):
                for j in range(8):
                    if board[i,j].get_symbol()=='wK':
                        return (i,j)

    def too_close(self, new_pos, opp_king_pos):
        val = (opp_king_pos[0]-new_pos[0])**2 + (opp_king_pos[1]-new_pos[1])**2
        if val==1:
            return True
        return False