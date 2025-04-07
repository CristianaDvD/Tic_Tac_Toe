import random


# Global variables
current_player = "X"
game_board = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " "]
winner = None
game_running = True


def print_game_board(game_board):
    pass 


def mark_choice(game_board):
    """
    Mark X or O in the chosen spot on the game board
    """
    global current_player


def validation():
    pass 


def switch_player():
    """
    Switch player once a spot has been marked.
    """
    global current_player    
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"    


def computer(game_board):
    """
    Player against computer. Computer makes the choice. 
    """
    while current_player == "O":
        position = random.randint(0, 8)
        if game_board[position] == "":
            game_board[position] = "O"
            switch_player()


def restart_game():
    pass


def exit_game(game_window):
    pass
            

while game_running:
    mark_choice(game_board)
    switch_player()
    computer(game_board)

