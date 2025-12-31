import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.turn = 'X'

    def print_board(self):
        for i in range(3):
            row = self.board[i*3 : (i+1)*3]
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

    def get_human_move(self):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"Player {self.turn}'s turn (0-8): ")
            try:
                val = int(square)
                if val not in self.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val

    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        self.print_board()
        while ' ' in self.board and not self.current_winner:
            if self.turn == 'X':
                square = self.get_human_move()
            else:
                square = self.get_human_move()

            if self.make_move(square, self.turn):
                self.print_board()
                if self.current_winner:
                    print(f"Player {self.turn} wins!")
                    return
                self.turn = 'O' if self.turn == 'X' else 'X'
        
        print("It's a draw!")

class TicTacToeVsComputer(TicTacToe):
    def play(self):
        print("Welcome to Tic-Tac-Toe vs Computer!")
        self.print_board()
        while ' ' in self.board and not self.current_winner:
            if self.turn == 'X':
                square = self.get_human_move()
            else:
                print("Computer's turn...")
                square = random.choice(self.available_moves())

            if self.make_move(square, self.turn):
                self.print_board()
                if self.current_winner:
                    print(f"Player {self.turn} wins!")
                    return
                self.turn = 'O' if self.turn == 'X' else 'X'
        
        print("It's a draw!")

# Main logic to start the game
print("1. Two Players")
print("2. Vs Computer")
choice = input("Select mode: ")

if choice == '2':
    game = TicTacToeVsComputer()
else:
    game = TicTacToe()

game.play()