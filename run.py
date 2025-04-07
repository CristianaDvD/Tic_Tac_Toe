import tkinter
from tkinter import messagebox
import random


# Global variables
current_player = "X"
game_board = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
turns = 0
winner = None
game_running = True


# colors to assign to window game
color_green = "#00ff00"
color_red = "#ff0000"
color_gray = "#343434"
color_light_gray = "#cccccc"


def show_error_message():
    """
    Opens error message pop up if player clicks a spot
    already marked.
    """
    messagebox.showerror("Oops!", "This spot is already marked!")


def mark_choice(row, column):
    """
    Mark X or O in the chosen spot on the game board
    """
    global current_player

    game_board[row][column]["text"] = current_player


def restart_game():
    pass


def exit_game(game_window):
    pass


""" 
Code inspired from https://www.youtube.com/watch?v=nbRpDXV7QDM
to create window for tic tac toe game. 
More info in Readme
"""

game_window = tkinter.Tk()
game_window.title("Tic Tac Toe")
game_window.resizable(False, False)

frame = tkinter.Frame(game_window)
label = tkinter.Label(frame, text=current_player+"'s turn", 
                      font=("Lucida Console", 25), 
                      background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

# Create the board in tkinter with for loop
for row in range(3):
    for column in range(3):
        game_board[row][column] = tkinter.Button(frame, text="", 
                                                 font=("Lucida Console", 50), 
                                                 background=color_gray, 
                                                 foreground="white", 
                                                 width=4, 
                                                 height=1,
                                                 command=lambda row=row, 
                                                 column=column: 
                                                 mark_choice(row, column))
        game_board[row][column].grid(row=row+1, column=column)

restart_button = tkinter.Button(frame, text="Restart Game", 
                                font=("Lucida Console", 25),
                                background=color_gray,
                                foreground=color_green,
                                command=restart_game)
restart_button.grid(row=4, column=0, columnspan=3, sticky="we")

exit_button = tkinter.Button(frame, text="Exit Game",
                             font=("Lucida Console", 25),
                             background=color_gray, 
                             foreground=color_red,
                             command=exit_game(game_window))
exit_button.grid(row=5, column=0, columnspan=3, sticky="we")

frame.pack()

# Gets the window game to open always in the center
game_window.update()
game_window_width = game_window.winfo_width()
game_window_height = game_window.winfo_height()
screen_width = game_window.winfo_screenwidth()
screen_height = game_window.winfo_screenheight()

game_window_x = int((screen_width/2) - (game_window_width/2))
game_window_y = int((screen_height/2) - (game_window_height/2))

# Formula
game_window.geometry(
    f"{game_window_width}x{game_window_height}+{game_window_x}+{game_window_y}"
    )

# Opens the window game
game_window.mainloop()

