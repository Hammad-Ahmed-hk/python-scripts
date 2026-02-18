import tkinter as tk
from tkinter import messagebox

"""create file .py simila to used python file
also include list dict and func as well
and their funct is used"""
print("hello world")
current_player = "X"
game_over = False

root = tk.Tk()
root.title("Tic Tac Toe")

status = tk.Label(root, text=f"Turn: {current_player}", font=("Arial", 14))
status.grid(row=0, column=0, columnspan=3, pady=5)

buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    b = [[buttons[r][c]["text"] for c in range(3)] for r in range(3)]
    lines = []
    for r in range(3):
        lines.append(b[r])
    for c in range(3):
        lines.append([b[r][c] for r in range(3)])
    lines.append([b[i][i] for i in range(3)])
    lines.append([b[i][2 - i] for i in range(3)])
    for line in lines:
        if line[0] and line.count(line[0]) == 3:
            return line[0]
    if all(b[r][c] for r in range(3) for c in range(3)):
        return "Tie"
    return None

def on_click(r, c):
    global current_player, game_over
    if game_over or buttons[r][c]["text"]:
        return
    buttons[r][c]["text"] = current_player
    winner = check_winner()
    if winner:
        game_over = True
        if winner == "Tie":
            status.config(text="It's a tie!")
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        else:
            status.config(text=f"{winner} wins!")
            messagebox.showinfo("Tic Tac Toe", f"{winner} wins!")
        for row in buttons:
            for b in row:
                b.config(state="disabled")
    else:
        current_player = "O" if current_player == "X" else "X"
        status.config(text=f"Turn: {current_player}")

def reset():
    global current_player, game_over
    current_player = "X"
    game_over = False
    status.config(text=f"Turn: {current_player}")
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="", state="normal")

for r in range(3):
    for c in range(3):
        btn = tk.Button(root, text="", width=6, height=3, font=("Arial", 24),
                        command=lambda r=r, c=c: on_click(r, c))
        btn.grid(row=r+1, column=c, padx=5, pady=5)
        buttons[r][c] = btn

reset_btn = tk.Button(root, text="Reset", command=reset)
reset_btn.grid(row=4, column=0, columnspan=3, pady=8)

root.resizable(False, False)
root.mainloop()