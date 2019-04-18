from tkinter import Tk, Label, Frame, messagebox
from time import sleep

board = [" "] * 9
turn = "X"
combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
          [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

computer = "O"
human = "X"
Labels = {}


def inv(player):
    return "X" if player == "O" else "O"


def available_spaces(board):
    return [i for i in range(len(board)) if board[i] == " "]


def nextTurn():
    global turn
    turn = "X" if turn == "O" else "O"


def addLabel(frame, text, x, y):
    label = Label(frame, text=text, font=("Helvetica", 32), borderwidth=2,
                  width=2, bg="white", fg="black")
    label.grid(row=x, column=y, padx=10, pady=10)
    label.bind("<Button-1>", lambda event: click(label, x, y))
    Labels[y + x*3] = label


def reset_board():
    print("Resetting...")
    global board, turn
    board = [" "] * 9
    turn = "X"
    for label in Labels.keys():
        Labels[label]["text"] = " "
        Labels[label]["fg"] = "black"
    print("Done")


def lit(combos):
    for i in Labels.keys():
        if i in combos:
            Labels[i]["fg"] = "red"


def pop_up(message):
    messagebox.showinfo("Result", message)
    sleep(1)
    reset_board()


def find_winner(b):
    for i in range(0, len(combos)):
        combo = combos[i]
        if(b[combo[0]] == b[combo[1]] and b[combo[1]] == b[combo[2]]
           and b[combo[0]] != " "):
            return b[combo[0]], combo
    return " ", None


def click(label, x, y):
    if board[y + 3*x] != " ":
        messagebox.showwarning("warning", "Box already used")
    else:
        label["text"] = turn
        board[y + 3*x] = turn
        winner, combinations = find_winner(board)
        if winner != " ":
            lit(combinations)
            winner = "Computer" if winner == "O" else "Human"
            print(f"{winner} has won")
            pop_up(f"Winner is {winner}")
        else:
            nextTurn()
            # print(f"Available spaces: {available_spaces(board)}")
            remaining = len(available_spaces(board))
            if turn == computer and remaining > 1:
                best = minimax(board, computer)
                print(f"Human chooses position: {x, y}")
                pos = best["pos"]
                print(f"computer chooses: {pos//3, pos%3}")
                click(Labels[pos], pos//3, pos % 3)
            elif remaining == 0:
                print("match drawn")
                pop_up("Match Drawn")


def minimax(board, player):
    b = board[:]
    winner = find_winner(b)[0]
    if winner == computer:
        return {"val": 10, "pos": -1}
    if winner == human:
        return {"val": -10, "pos": -1}

    moves = available_spaces(b)
    if len(moves) < 1:
        return {"val": 0, "pos": -1}

    scores = []

    for i in range(len(moves)):
        current_move = moves[i]
        b[current_move] = player
        score = minimax(b, inv(player))
        scores.append({"val": score["val"], "pos": current_move})
        b[current_move] = " "
    f = max if player == computer else min
    best_move = f(scores, key=lambda x: x["val"])
    return best_move


if __name__ == '__main__':
    root = Tk()
    root.geometry("230x230+650+200")
    root.attributes("-toolwindow", 2)
    root.wm_title("Tic Tac Toe")
    frame = Frame(root, width=500, height=300)

    for x in range(0, 3):
        for y in range(0, 3):
            addLabel(frame, " ", x, y)

    frame.configure(background='black')
    frame.pack()
    frame.mainloop()


# Getting X, Y postion from number
# board =>
# 0 1 2
# 3 4 5
# 6 7 8

# 4 => (4//3) , (4%3)
# 4 => 1, 1

# 2-d array flattening
# getting index position from X, y
# X, Y = (1, 1)
# Y + 3 * x
# postion = 4
