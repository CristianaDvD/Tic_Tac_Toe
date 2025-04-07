import random
import os


# Global variables
current_player = "X"
game_board = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " "]
winner = None
game_running = True


def clear_screen(numlines=100):
    """
    Clears the console to get a better UX.
    numlines is an optional argument used only as a fall-back (credits to:
    https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python)
    """
    if os.name == "posix":
        # for OS -> Unix / Linux / MacOS / BSD etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # for OS -> DOS / Windows
        os.system('CLS') 
    else:
        # Fallback for other operating systmes.
        print('\n' * numlines)       


def instructions():
    """
    Prints instructions for the game.
    """
    print("*" * 5 + "Welcome to TIC TAC TOE game" + "*" * 5 + "\n")
    print(">>>>>>>>INSTRUCTIONS<<<<<<<<\n")
    print("Tic-tac-toe is a game played on a three-by-three grid")
    print("by two players, in this case you and the computer, who alternately")
    print("place the marks X and O in one of the nine spaces in the grid.\n")
    print("Consider a board with the nine positions numbered as follows:\n")
    print(" 0 | 1 | 2 |")
    print("---|---|---|")
    print(" 3 | 4 | 5 |")
    print("---|---|---|")
    print(" 6 | 7 | 8 |\n")
    print("Choose a position from 0 to 8 in order to mark.")
    print("Whoever gets the first 3 symbols in a row, column or diagonal,")
    print("is the winner of the game!\n")
    print(">>>GOOD LUCK!<<<")


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
            

def main():
    """
    Welcomes the user and gives the option to continue or no.
    Runs all the program functions.
    """
    
    instructions()
    print_game_board(game_board)
    mark_choice(game_board)
    switch_player()
    computer(game_board)


if __name__ == '__main__':
    while True:
        main()
