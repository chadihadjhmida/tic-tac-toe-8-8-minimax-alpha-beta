import json
import os
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
mx, my = 3, 3
w = [255, 255, 255]

x = [255, 0, 0]
o = [255, 255, 255]
v = [0, 0, 0]
TRANS_TABLE_FILE = "./tab.json"

hat = [v for _ in range(64)]
sense.set_pixels(hat)
players = [x, o]
player = x


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


def flatter(board):
    l = []
    for r in range(8):
        for c in range(8):
            l.append(board[r][c])
    return l


def cond(fboard):
    return [[fboard[i] for i in range(j, j + 8, 1)] for j in range(0, 64, 8)]


def next(r, c):
    global player
    global hat
    button = cond(hat)
    if button[r][c] == v and check(button)[0] is False:
        if player == players[0]:
            button[r][c] = player
            hat = flatter(button)
            sense.set_pixels(hat)
            t = check(button)
            if t[0] is False:
                bestmove = ai()
                button[bestmove[0]][bestmove[1]] = players[1]
                hat = flatter(button)
                sense.set_pixels(hat)
            elif t[0] is True:
                pass
            elif t[1] == "tie":
                pass
        elif player == players[1]:
            button[r][c] = player
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
                    board[r][c]
                    == board[r + 1][c]
                    == board[r + 2][c]
                    == board[r + 3][c]
                    != v
                ):
                    return [True, board[r][c]]
                if c < 5:
                    if (r + 3 < 8) and (c + 3 < 8):
                        if (
                            board[r][c]
                            == board[r + 1][c + 1]
                            == board[r + 2][c + 2]
                            == board[r + 3][c + 3]
                            != v
                        ):
                            return [True, board[r][c]]
                if c < 8 and c >= 3:
                    if r + 3 < 8 and c - 3 >= 0:
                        if (
                            board[r][c]
                            == board[r + 1][c - 1]
                            == board[r + 2][c - 2]
                            == board[r + 3][c - 3]
                            != v
                        ):
                            return [True, board[r][c]]
            if c < 5:
                if (
                    board[r][c]
                    == board[r][c + 1]
                    == board[r][c + 2]
                    == board[r][c + 3]
                    != v
                ):
                    return [True, board[r][c]]
    if empty(board) is True:
        return [False, "-1"]
    else:
        print("tie")
        return [True, "tie"]


def empty(board):
    for r in range(8):
        for c in range(8):
            if board[r][c] == v:
                return True
    return False


def ai():
    button = cond(hat)
    bestscore = float("inf")
    bestmove = []
    for r in range(8):
        for c in range(8):
            if button[r][c] == v:
                button[r][c] = players[1]
                score = minmax(button, 0, True, -float("inf"), +float("inf"))
                button[r][c] = v
                if score < bestscore:
                    bestscore = score
                    bestmove = [r, c]
    return bestmove


def evaluate_board(board, player):
    opponent = o if player == x else x
    score = 0

    center_col = 8 // 2
    center_count = sum(1 for row in board if row[center_col] == player)
    score += center_count * 3
    center_count = sum(1 for row in board if row[center_col] == opponent)
    score -= center_count * 3

    for row in range(8):
        for col in range(8):
            if col < 5:
                window = [board[row][col + i] for i in range(4)]
                score += evaluate_window(window, player, opponent)
            if row < 5:
                window = [board[row + i][col] for i in range(4)]
                score += evaluate_window(window, player, opponent)
                if col < 5:
                    window = [board[row + i][col + i] for i in range(4)]
                    score += evaluate_window(window, player, opponent)
            if row >= 3:
                if col < 5:
                    window = [board[row - i][col + i] for i in range(4)]
                    score += evaluate_window(window, player, opponent)
    return score


def evaluate_window(window, player, opponent):
    score = 0

    player_count = window.count(x)
    opponent_count = window.count(o)
    empty_count = window.count(v)

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
            if board[row][col] == v:
                board[row][col] = player
                score = evaluate_board(board, player)
                possible_moves.append((score, (row, col)))
                board[row][col] = v

    if player == x:
        possible_moves.sort(reverse=True, key=lambda x: x[0])
    else:
        possible_moves.sort(reverse=False, key=lambda x: x[0])
    return [move[1] for move in possible_moves]


def minmax(board, depth, ismax, alpha, beta):
    key_board = str([[board[r][c] for c in range(8)] for r in range(8)])
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
                if board[r][c] == v:
                    board[r][c] = players[0]
                    score = minmax(board, depth + 1, False, alpha, beta)
                    board[r][c] = v
                    bestscore = max(score, bestscore)
                    alpha = max(alpha, bestscore)
                    if beta <= alpha:
                        return bestscore
        return bestscore

        # this is min-max with sorted move help with alpha beta but i'm not gonna use it because it only work in theory
        for move in get_sorted_moves(board, "x"):
            r, c = move
            board[r][c] = players[0]
            score = minmax(board, depth + 1, False, alpha, beta)
            board[r][c] = v
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
                if board[r][c] == v:
                    board[r][c] = players[1]
                    score = minmax(board, depth + 1, True, alpha, beta)
                    board[r][c] = v
                    bestscore = min(score, bestscore)
                    beta = min(beta, bestscore)
                    if beta <= alpha:
                        return bestscore
        return bestscore
        # this is min-max with sorted move help with alpha beta but i'm not gonna use it because it only work in theory
        for move in get_sorted_moves(board, "o"):
            r, c = move
            board[r][c] = players[1]
            score = minmax(board, depth + 1, True, alpha, beta)
            board[r][c] = v
            bestscore = min(score, bestscore)
            beta = min(beta, bestscore)
            if beta <= alpha:
                return bestscore
        tab[key_board] = {"eval": bestscore, "depth": depth}
        return bestscore


sense.set_pixel(mx, my, *w)


def coller(board):
    for r in range(8):
        for c in range(8):
            sense.set_pixel(r, c, board[r][c])


while True:
    board = cond(hat)
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up" and my > 0:
                sense.set_pixel(mx, my, board[mx][my])
                my -= 1
            elif event.direction == "down" and my < 7:
                sense.set_pixel(mx, my, board[mx][my])
                my += 1
            elif event.direction == "left" and mx > 0:
                sense.set_pixel(mx, my, board[mx][my])
                mx -= 1
            elif event.direction == "right" and mx < 7:
                sense.set_pixel(mx, my, board[mx][my])
                mx += 1
            elif event.direction == "middle":
                next(mx, my)
                if check(board)[0]:
                    if check(board)[1] != "tie":
                        sense.show_message("player win ", text_colour=check(board)[1])
                    else:
                        sense.show_message("player win ", text_colour=[0, 255, 0])
    coller(board)
    sense.set_pixel(mx, my, *w)
    sleep(0.1)
