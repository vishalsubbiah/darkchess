from darkchess.src.piece import Piece


class GameEngine():

    def __init__(self, Board, player1=None, player2=None):
        self.move_counter = 0
        self.Board = Board
        self.prev_Board = Board
        if player1 is None:
            player1 = "human"
        if player2 is None:
            player2 = "human"
        self.player1 = player1  # plays as white
        self.player2 = player2  # plays as black

    def get_turn(self):
        if self.move_counter % 2 == 0:
            print("white's turn")
            return "white", self.player1
        else:
            print("black's turn")
            return "black", self.player2

    def get_moves(self, pos):
        piece = self.Board.board[pos[0], pos[1]]
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
            if isinstance(self.Board.board[pos[0], pos[1]], Piece):
                print("piece chosen: "+self.Board.board[pos[0], pos[1]].symbol)
                if self.Board.board[pos[0], pos[1]].team == team:
                    moves = self.get_moves(pos)
                    if moves == []:
                        print("no moves available for that piece")
                        self.choose_move(move)
                    move_dict = dict()
                    for i, move in enumerate(moves):
                        move_dict[i+1] = move
                    print(self.translate(move_dict))
                    option = input("move:")
                    self.prev_Board = self.Board
                    self.Board.update_board(move_dict[int(option)], team)
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
            self.prev_Board = self.Board
            self.Board.update_board(move, team)
            self.move_counter += 1
        else:
            raise ValueError("this player:" +
                             player +
                             " doesn't exist in the realm of this game")

    def undo_move(self):
        self.Board = self.prev_Board
        self.move_counter -= 1

    @staticmethod
    def translate(move_dict):
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

    def all_moves(self):
        team, _ = self.get_turn()
        all_moves_team = []
        for i in range(8):
            for j in range(8):
                if self.Board.board[i,j].team == team:
                    all_moves_team+=self.get_moves((i,j))
        return all_moves_team