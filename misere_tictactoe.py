def make_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
    print()
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("---------")
    print()


def get_winner(board):
    lines = []
    for row in board:
        lines.append(row)
    for col in range(3):
        lines.append([board[row][col] for row in range(3)])
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != " ":
            return line[0]
    return None


def is_full(board):
    return all(board[r][c] != " " for r in range(3) for c in range(3))


def get_move(board, player):
    while True:
        try:
            move = input(f"Player {player}, enter row and column (e.g. 1 2): ")
            row, col = map(int, move.split())
            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("Numbers must be between 1 and 3.")
                continue
            row -= 1
            col -= 1
            if board[row][col] != " ":
                print("That cell is already taken.")
                continue
            return row, col
        except (ValueError, IndexError):
            print("Invalid input. Enter two numbers separated by a space.")


def play():
    print("=== Misere Tic-Tac-Toe ===")
    print("Goal: Do NOT get three in a row or you LOSE!\n")

    board = make_board()
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        row, col = get_move(board, player)
        board[row][col] = player

        winner = get_winner(board)
        if winner:
            print_board(board)
            loser = winner
            winner_player = players[1 - players.index(loser)]
            print(f"Player {loser} got three in a row and LOSES!")
            print(f"Player {winner_player} WINS!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        turn += 1


if __name__ == "__main__":
    play()
