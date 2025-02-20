import tkinter
import random
import json
import os

TRANS_TABLE_FILE = "./tab.json"


def load_transposition_table():
    if os.path.exists(TRANS_TABLE_FILE) and os.path.getsize(TRANS_TABLE_FILE) > 0:
        try:
            with open(TRANS_TABLE_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Resetting transposition table.")
            return {}
    return {}


def save_transposition_table(table):
    with open(TRANS_TABLE_FILE, "w") as file:
        json.dump(table, file)


tab = load_transposition_table()


def rundomplay(board):
    r = random.randint(0, 7)
    c = random.randint(0, 7)
    while board[r][c]["text"] != "":
        r = random.randint(0, 7)
        c = random.randint(0, 7)
    return [r, c]


def next(r, c):
    global player
    if button[r][c]["text"] == "" and check(button)[0] is False:
        if player == players[0]:
            button[r][c]["text"] = player
            t = check(button)
            if t[0] is False:
                # print(evaluate_board(button, "x"))
                # player = players[1]
                # print(str([[button[r][c]["text"] for c in range(8)] for r in range(8)]))
                bestmove = ai()
                button[bestmove[0]][bestmove[1]]["text"] = players[1]
                # r, c = rundomplay(button)
                save_transposition_table(tab)
                next(r, c)
            elif t[0] is True:
                save_transposition_table(tab)
                pass
            elif t[1] == "tie":
                save_transposition_table(tab)
                pass
        elif player == players[1]:
            button[r][c]["text"] = player
            t = check(button)
            if t[0] is False:
                player = players[0]
            if t[0] is True:
                save_transposition_table(tab)
                pass
            if t[1] == "tie":
                save_transposition_table(tab)
                pass


def check(board):
    for r in range(8):
        for c in range(8):
            if r < 5:
                if (
                    board[r][c]["text"]
                    == board[r + 1][c]["text"]
                    == board[r + 2][c]["text"]
                    == board[r + 3][c]["text"]
                    != ""
                ):
                    print(board[r][c]["text"] + " win")
                    return [True, board[r][c]["text"]]
                if c < 5:
                    if (r + 3 < 8) and (c + 3 < 8):
                        if (
                            board[r][c]["text"]
                            == board[r + 1][c + 1]["text"]
                            == board[r + 2][c + 2]["text"]
                            == board[r + 3][c + 3]["text"]
                            != ""
                        ):
                            print(board[r][c]["text"] + " win")
                            return [True, board[r][c]["text"]]
                if c < 8 and c >= 3:
                    if r + 3 < 8 and c - 3 >= 0:
                        if (
                            board[r][c]["text"]
                            == board[r + 1][c - 1]["text"]
                            == board[r + 2][c - 2]["text"]
                            == board[r + 3][c - 3]["text"]
                            != ""
                        ):
                            print(board[r][c]["text"] + " win")
                            return [True, board[r][c]["text"]]
            if c < 5:
                if (
                    board[r][c]["text"]
                    == board[r][c + 1]["text"]
                    == board[r][c + 2]["text"]
                    == board[r][c + 3]["text"]
                    != ""
                ):
                    print(board[r][c]["text"] + " win")
                    return [True, board[r][c]["text"]]
    if empty(board) is True:
        return [False, "-1"]
    else:
        print("tie")
        return [True, "tie"]


def empty(board):
    for r in range(8):
        for c in range(8):
            if board[r][c]["text"] == "":
                return True
    return False


def ai():
    bestscore = float("inf")
    bestmove = []
    for r in range(8):
        for c in range(8):
            if button[r][c]["text"] == "":
                button[r][c]["text"] = players[1]
                score = minmax(button, 0, True, -float("inf"), +float("inf"))
                button[r][c]["text"] = ""
                if score < bestscore:
                    bestscore = score
                    bestmove = [r, c]
    return bestmove


scores = {"x": 1000, "o": -1000, "tie": 0}


def evaluate_board(board, player):
    opponent = "o" if player == "x" else "x"
    score = 0

    center_col = 8 // 2
    center_count = sum(1 for row in board if row[center_col] == player)
    score += center_count * 3
    center_count = sum(1 for row in board if row[center_col] == opponent)
    score -= center_count * 3

    for row in range(8):
        for col in range(8):
            if col < 5:
                window = [board[row][col + i]["text"] for i in range(4)]
                score += evaluate_window(window, player, opponent)
            if row < 5:
                window = [board[row + i][col]["text"] for i in range(4)]
                score += evaluate_window(window, player, opponent)
                if col < 5:
                    window = [board[row + i][col + i]["text"] for i in range(4)]
                    score += evaluate_window(window, player, opponent)
            if row >= 3:
                if col < 5:
                    window = [board[row - i][col + i]["text"] for i in range(4)]
                    score += evaluate_window(window, player, opponent)
    return score


def evaluate_window(window, player, opponent):
    score = 0
    player_count = window.count("x")
    opponent_count = window.count("o")
    empty_count = window.count("")

    if player_count > 0 and opponent_count > 0:
        return 0

    if player_count == 4:
        score += 100000
    elif player_count == 3 and empty_count == 1:
        score += 100
    elif player_count == 2 and empty_count == 2:
        score += 10

    if opponent_count == 4:
        score -= 100000
    elif opponent_count == 3 and empty_count == 1:
        score -= 100
    elif opponent_count == 2 and empty_count == 2:
        score -= 10

    return score


def get_sorted_moves(board, player):
    possible_moves = []
    for row in range(8):
        for col in range(8):
            if board[row][col]["text"] == "":
                board[row][col]["text"] = player
                score = evaluate_board(board, player)
                possible_moves.append((score, (row, col)))
                board[row][col]["text"] = ""

    if player == "x":
        possible_moves.sort(reverse=True, key=lambda x: x[0])
    else:
        possible_moves.sort(reverse=False, key=lambda x: x[0])
    return [move[1] for move in possible_moves]


def minmax(board, depth, ismax, alpha, beta):
    key_board = str([[board[r][c]["text"] for c in range(8)] for r in range(8)])
    if key_board in tab and tab[key_board]["depth"] >= depth:
        return tab[key_board]["eval"]

    if check(board)[0] or depth == 2:
        re = evaluate_board(board, "x")
        print(re)
        tab[key_board] = {"eval": re, "depth": depth}
        return re
    if ismax:
        bestscore = -float("inf")

        for r in range(8):
            for c in range(8):
                if board[r][c]["text"] == "":
                    board[r][c]["text"] = players[0]
                    score = minmax(board, depth + 1, False, alpha, beta)
                    board[r][c]["text"] = ""
                    bestscore = max(score, bestscore)
                    alpha = max(alpha, bestscore)
                    if beta <= alpha:
                        return bestscore
        return bestscore

        for move in get_sorted_moves(board, "x"):
            r, c = move
            board[r][c]["text"] = players[0]
            score = minmax(board, depth + 1, False, alpha, beta)
            board[r][c]["text"] = ""
            bestscore = max(score, bestscore)
            alpha = max(alpha, bestscore)
            if beta <= alpha:
                return bestscore
        tab[key_board] = {"eval": bestscore, "depth": depth}
        return bestscore
    else:
        bestscore = float("inf")

        for r in range(8):
            for c in range(8):
                if board[r][c]["text"] == "":
                    board[r][c]["text"] = players[1]
                    score = minmax(board, depth + 1, True, alpha, beta)
                    board[r][c]["text"] = ""
                    bestscore = min(score, bestscore)
                    beta = min(beta, bestscore)
                    if beta <= alpha:
                        return bestscore
        return bestscore

        for move in get_sorted_moves(board, "o"):
            r, c = move
            board[r][c]["text"] = players[1]
            score = minmax(board, depth + 1, True, alpha, beta)
            board[r][c]["text"] = ""
            bestscore = min(score, bestscore)
            beta = min(beta, bestscore)
            if beta <= alpha:
                return bestscore
        tab[key_board] = {"eval": bestscore, "depth": depth}
        return bestscore


def new_game():
    pass


window = tkinter.Tk()
players = ["x", "o"]
player = "x"

button = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

frame = tkinter.Frame(window)
frame.pack()

for r in range(8):
    for c in range(8):
        button[r][c] = tkinter.Button(
            frame,
            text="",
            font=("consolas"),
            width=5,
            height=2,
            command=lambda r=r, c=c: next(r, c),
        )
        button[r][c].grid(row=r, column=c)

window.mainloop()
