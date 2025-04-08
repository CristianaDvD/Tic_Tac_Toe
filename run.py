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


def show_instructions():
    """
    Prints instructions for the game.
    """
    print(">>>>>>>>INSTRUCTIONS<<<<<<<<\n")
    print("Tic-tac-toe is a game played on a three-by-three grid")
    print("by two players, in this case you and the computer, who alternately")
    print("place the marks X and O in one of the nine spaces in the grid.\n")
    print("Consider a board with the nine positions numbered as follows:\n")
    print(" 1 | 2 | 3 |")
    print("---|---|---|")
    print(" 4 | 5 | 6 |")
    print("---|---|---|")
    print(" 7 | 8 | 9 |\n")
    print("Choose a position from 1 to 9 in order to mark.")
    print("Whoever gets the first 3 symbols in a row, column or diagonal,")
    print("is the winner of the game!\n")
    print(">>>GOOD LUCK!<<<")
    print("Type 's' to start the game or 'e' to exit:")
    while game_running:
        play_choice = input().strip().lower()
        if play_choice == 's':
            clear_screen()
            print_game_board(game_board)
        elif play_choice == 'e':
            clear_screen()
            print("Thank you! If you change your mind,")
            print("please press Run program!")
            break
        else:
            print("Error! Please type in 's' or 'e'.")        
    

def intro_user_input():
    """
    Welcomes the user and gives the option to continue or no.
    """
    print("\n" + "*" * 5 + "Welcome to TIC TAC TOE game" + "*" * 5 + "\n")
    print("What is your name?")
    name = input()
    print("")
    print("-" * 15)
    print(f"Hi {name}!")
    print("Would you like to play Tic Tac Toe?")
    print("Type 'y' for YES and 'n' for NO:")
    user_choice = input().strip().lower()
    while game_running:
        if user_choice == 'y':
            clear_screen()
            show_instructions()
        elif user_choice == 'n':
            clear_screen()
            print("Thank you! If you change your mind,")
            print("please press Run program!")
            break
        else:
            print("Error! Please type 'y' or 'n'")    


def print_game_board(game_board):
    """
    Creates the game board, 
    and prints reference board first for better UX.
    """
    print("\nReference board:\n")
    print("1 | 2 | 3 |")
    print("--|---|---|")
    print("4 | 5 | 6 |")
    print("--|---|---|")
    print("7 | 8 | 9 |\n")
    print("Live play board:\n")
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2] + " |")
    print("--|---|---|")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5] + " |")
    print("--|---|---|")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8] + " |")

    type_choice(game_board)


def type_choice(game_board):
    """
    Player to choose its spot from 1 to 9 to mark.
    """
    inp = int(input("Choose a spot from 1 to 9: "))
    if inp >= 1 and inp <= 9 and game_board[inp-1] == " ":
        game_board[inp-1] = current_player
    else:
        raise ValueError("Spot already taken! Try again!")    
    
    clear_screen()
    print_game_board(game_board)        
      

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
        if game_board[position] == " ":
            game_board[position] = "O"
            switch_player()


def restart_game():
    pass
            

def main():
    """
    Runs all the program functions.
    """
    while game_running:
        intro_user_input()
        print_game_board(game_board)
        type_choice(game_board)
        switch_player()
        computer(game_board)
        switch_player()


if __name__ == '__main__':
    while True:
        main()

