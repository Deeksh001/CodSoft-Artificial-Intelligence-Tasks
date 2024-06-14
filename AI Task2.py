import numpy as np

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n-------------")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if (board[i, :] == player).all() or (board[:, i] == player).all():
            return True
    # Check diagonals
    if (np.diag(board) == player).all() or (np.diag(np.fliplr(board)) == player).all():
        return True
    return False

# Function to check if the board is full
def board_full(board):
    return not (board == ' ').any()

# Function to evaluate the current state of the board
def evaluate(board):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif board_full(board):
        return 0
    else:
        return None

# Function for the Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)
    if score is not None:
        return score

    if is_maximizing:
        max_eval = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = np.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI player using Minimax
def find_best_move(board):
    best_eval = -np.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                eval = minimax(board, 0, -np.inf, np.inf, False)
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Main function to play the game
def play_game():
    board = np.array([[' ']*3]*3)
    print_board(board)

    while True:
        # Human player's move
        row, col = map(int, input("Enter your move (row col): ").split())
        if board[row][col] != ' ':
            print("Invalid move! Try again.")
            continue
        board[row][col] = 'O'
        print_board(board)

        # Check if human player wins or board is full
        if check_winner(board, 'O'):
            print("Congratulations! You win!")
            break
        elif board_full(board):
            print("It's a draw!")
            break

        # AI player's move
        print("AI player is thinking...")
        row, col = find_best_move(board)
        board[row][col] = 'X'
        print_board(board)

        # Check if AI player wins or board is full
        if check_winner(board, 'X'):
            print("AI player wins! Better luck next time.")
            break
        elif board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
