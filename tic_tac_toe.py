import math

HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    print("\n")
    for i in range(3):
        print(" " + " | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(board, player):
    win_patterns = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

def is_board_full(board):
    return all(cell != EMPTY for cell in board)

def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]

def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 10 - depth
    elif check_winner(board, HUMAN):
        return -10 + depth
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_empty_cells(board):
            board[move] = AI
            score = minimax(board, depth + 1, False)
            board[move] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_empty_cells(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, True)
            board[move] = EMPTY
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_empty_cells(board):
        board[move] = AI
        score = minimax(board, 0, False)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    board = [EMPTY] * 9
    print("=== Tic-Tac-Toe vs Unbeatable AI ===")
    print("You are X, AI is O")
    print("Enter position 1-9:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")

    start = input("Do you want to go first? (y/n): ").lower()
    human_turn = (start == 'y')

    while True:
        print_board(board)

        if human_turn:
            try:
                move = int(input("Your move (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != EMPTY:
                    print("Invalid move! Try again.")
                    continue
                board[move] = HUMAN
            except ValueError:
                print("Enter a number.")
                continue

            if check_winner(board, HUMAN):
                print_board(board)
                print("Congratulations! You won!")
                break
            human_turn = False
        else:
            print("AI is thinking...")
            move = ai_move(board)
            if move is not None:
                board[move] = AI
                print(f"AI chose position {move + 1}")

            if check_winner(board, AI):
                print_board(board)
                print("AI won!")
                break
            human_turn = True

        if is_board_full(board):
            print_board(board)
            print("It's a draw! AI never loses.")
            break

play_game()
