import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Tic Tac Toe")

# Constants
WIDTH, HEIGHT = 300, 300  # Canvas dimensions
CELL_SIZE = WIDTH // 3  # Size of each cell
LINE_COLOR = "black"
PLAYER_X = "X"
PLAYER_O = "O"

# Game state
board = [["" for _ in range(3)] for _ in range(3)]
current_player = PLAYER_X


# Function to draw the game board
def draw_board(canvas):
    for i in range(1, 3):
        canvas.create_line(i * CELL_SIZE, 0, i * CELL_SIZE, HEIGHT, fill=LINE_COLOR, width=2)
        canvas.create_line(0, i * CELL_SIZE, WIDTH, i * CELL_SIZE, fill=LINE_COLOR, width=2)


# Function to check for a winner
def check_winner():
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]

    # Check for a tie
    if all(cell != "" for row in board for cell in row):
        return "Tie"

    return None


# Function to handle player moves
def handle_click(event):
    global current_player
    x, y = event.x, event.y
    row, col = y // CELL_SIZE, x // CELL_SIZE

    if board[row][col] == "":
        # Update board and draw the player's mark
        board[row][col] = current_player
        x_start, y_start = col * CELL_SIZE, row * CELL_SIZE
        x_end, y_end = x_start + CELL_SIZE, y_start + CELL_SIZE
        canvas.create_text((x_start + x_end) // 2, (y_start + y_end) // 2,
                           text=current_player, font=("Arial", 48), fill="blue")

        # Check for a winner
        winner = check_winner()
        if winner:
            if winner == "Tie":
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_game()
        else:
            # Switch players
            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X


# Function to reset the game
def reset_game():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = PLAYER_X
    canvas.delete("all")
    draw_board(canvas)


# Create canvas for the game board
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Draw initial board
draw_board(canvas)

# Bind mouse clicks to handle player moves
canvas.bind("<Button-1>", handle_click)

# Start the Tkinter main loop
root.mainloop()
