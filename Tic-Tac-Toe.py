import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None 

    def print_board(self):
        # Print the current state of the board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Show which number corresponds to which spot
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
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
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check column 
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Top-left to bottom-right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Top-right to bottom-left
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X'  # Starting letter
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print('')  # Empty line
            
            if game.current_winner:
                if print_game:
                    print(f'{letter} wins!')
                return letter
            
            letter = 'O' if letter == 'X' else 'X'  # Switch player
    
    if print_game:
        print('It\'s a tie!')
    return None

class HumanPlayer:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(f'{self.letter}\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves(): 
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class AIPlayer:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player, alpha=float('-inf'), beta=float('inf')):
        max_player = self.letter  # Yourself
        other_player = 'O' if player == 'X' else 'X'
        
        # First check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': float('-inf')}
        else:
            best = {'position': None, 'score': float('inf')}
        
        for possible_move in state.available_moves():
            # Step 1: Make a move, try that spot
            state.make_move(possible_move, player)
            
            # Step 2: Recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player, alpha, beta)
            
            # Step 3: Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # This represents the move optimal next move
            
            # Step 4: Update the dictionaries if necessary
            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
                    alpha = max(alpha, best['score'])
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
                    beta = min(beta, best['score'])
            
            # Alpha-beta pruning
            if alpha >= beta:
                break
        
        return best

if __name__ == '__main__':
    print("Welcome to Tic-Tac-Toe!")
    print("You'll be playing against an unbeatable AI.")
    print("Here's the numbering system for the board:")
    
    x_player = HumanPlayer('X')
    o_player = AIPlayer('O')
    t = TicTacToe()
    
    play(t, x_player, o_player, print_game=True)
