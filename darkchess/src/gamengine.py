from darkchess.src.piece import Piece
from darkchess.src.board import Board as base_Board
import numpy as np
import sys


class GameEngine():

    def __init__(self, Board, player1=None, player2=None):
        self.move_counter = 0
        self.Board = Board
        self.prev_Board = base_Board()
        self.prev_Board.board = np.copy(Board.board)
        if player1 is None:
            player1 = "human"
        if player2 is None:
            player2 = "human"
        self.player1 = player1  # plays as white
        self.player2 = player2  # plays as black
        self.black_check = False
        self.white_check = False

    def get_turn(self):
        if self.move_counter % 2 == 0:
            return "white", self.player1
        else:
            return "black", self.player2

    def get_moves(self, pos):
        piece = self.Board.board[pos]
        return piece.get_moves(self.Board.board)

    def choose_move(self, move=None):
        team, player = self.get_turn()
        print(team + " to play")
        if player == "human":
            print("choose a piece (once chosen have to play that piece)")
            if move is not None:
                raise ValueError("Move is not None, cant be in human mode")
            pos_str = input("piece's position:").upper()

            col_dict = {'A': 0, 'B': 1, 'C': 2,
                        'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
            pos = (int(pos_str[1])-1, col_dict[pos_str[0]])
            if isinstance(self.Board.board[pos], Piece):
                print("piece chosen: "+self.Board.board[pos].symbol)
                if self.Board.board[pos].team == team:
                    moves = self.get_moves(pos)
                    if moves == []:
                        print("no moves available for that piece")
                        self.choose_move(move)
                    move_dict = dict()
                    for i, pos_move in enumerate(moves):
                        move_dict[i+1] = pos_move
                    print(self.num_alph(move_dict))
                    option = input("move:")
                    self.prev_Board.board = np.copy(self.Board.board)
                    self.Board.update_board(move_dict[int(option)], team)
                    self.is_check()
                    if team == "white":
                        if self.white_check:
                            print("white king in check")
                            self.undo_move()
                            self.is_checkmate(team)
                            print("play again")
                            self.choose_move(move)
                    if team == "black":
                        if self.black_check:
                            print("black king in check")
                            self.undo_move()
                            self.is_checkmate(team)
                            print("play again")
                            self.choose_move(move)
                    self.move_counter += 1
                else:
                    print("wrong team tried to play. choose again")
                    self.choose_move(move)
            else:
                print("chose a tile with no piece. choose again")
                self.choose_move(move)
        elif player == "computer":
            if move is None:
                raise ValueError("Move is None, cant be in computer mode")
            self.prev_Board.board = np.copy(self.Board.board)
            self.Board.update_board(move, team)
            self.is_check()
            if team == "white":
                if self.white_check:
                    print("white king in check")
                    self.undo_move()
                    self.is_checkmate(team)
                    print("play again")
                    self.choose_move(move)
            if team == "black":
                if self.black_check:
                    print("black king in check")
                    self.undo_move()
                    self.is_checkmate(team)
                    print("play again")
                    self.choose_move(move)
            self.move_counter += 1
        else:
            raise ValueError("this player:" +
                             player +
                             " doesn't exist in the realm of this game")

    def undo_move(self):
        self.Board.board = np.copy(self.prev_Board.board)

    @staticmethod
    def num_alph(move_dict):
        new_dict = {}
        revcol_dict = {0: 'A', 1: 'B', 2: 'C',
                       3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
        for key, val in move_dict.items():
            start = val[0]
            end = val[1]
            new_start = revcol_dict[start[1]] + str(start[0]+1)
            new_end = revcol_dict[end[1]] + str(end[0]+1)
            new_dict[key] = [new_start, new_end]
        return new_dict

    def _all_moves_minus_king(self, board, team):
        all_moves_team = []
        king_pos = None
        for i in range(8):
            for j in range(8):
                if board[i, j].team == team and board[i, j].get_symbol() != team[0]+"K ":
                    all_moves_team += board[i, j].get_moves(board)
                if board[i, j].team == team and board[i, j].get_symbol() == team[0]+"K ":
                    king_pos = (i, j)
        all_pos_team = []
        for move in all_moves_team:
            all_pos_team.append(move[1])
        return list(set(all_pos_team)), king_pos

    def is_check(self):
        white_moves, wK_pos = self._all_moves_minus_king(
            self.Board.board, "white")
        black_moves, bK_pos = self._all_moves_minus_king(
            self.Board.board, "black")
        if bK_pos in white_moves:
            self.black_check = True
        else:
            self.black_check = False
        if wK_pos in black_moves:
            self.white_check = True
        else:
            self.white_check = False

    def all_moves(self):
        team, _ = self.get_turn()
        all_moves_team = []
        for i in range(8):
            for j in range(8):
                if self.Board.board[i, j].team == team:
                    all_moves_team += self.get_moves((i, j))
        return all_moves_team

    def is_checkmate(self, team):
        self.undo_move()
        moves = self.all_moves()
        game_over = True
        for move in moves:
            self.Board.update_board(move, team)
            self.is_check()
            if team == "white":
                if self.white_check:
                    self.undo_move()
                else:
                    self.undo_move()
                    game_over = False
                    break
            elif team == "black":
                if self.black_check:
                    self.undo_move()
                else:
                    self.undo_move()
                    game_over = False
                    break
        if game_over:
            print(team + " lost")
            if team == "white":
                print("black wins")
                sys.exit(0)
            if team == "black":
                print("white wins")
                sys.exit(0)
