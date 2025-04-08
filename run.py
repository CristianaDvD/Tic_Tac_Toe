import random
import os


# Global variables
current_player = "X"
game = [" ", " ", " ",
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
            print_game(game)
        elif play_choice == 'e':
            clear_screen()
            print("**Thank you! If you change your mind,**")
            print("***please press Run program!***")
            quit()
        else:
            print("Error! Please type in 's' or 'e'.")

    show_instructions()                
    

def intro_user_input():
    """
    Welcomes the user and gives the option to continue or no.
    """
    print("\n" + "*" * 5 + "Welcome to TIC TAC TOE game" + "*" * 5 + "\n")
    print("What is your name?")
    name = input().capitalize()
    print("")
    print("-" * 15)
    if name.isalpha():
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
                print("**Thank you! If you change your mind,**")
                print("***please press Run program!***")
                quit()
            else:
                print("Error! Please type 'y' or 'n'.") 
    else:
        print("Invalid input. Only letters accepted.")
        print("Please try again.\n")  

    intro_user_input()                 


def print_game(game):
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
    print(game[0] + " | " + game[1] + " | " + game[2] + " |")
    print("--|---|---|")
    print(game[3] + " | " + game[4] + " | " + game[5] + " |")
    print("--|---|---|")
    print(game[6] + " | " + game[7] + " | " + game[8] + " |")

    type_choice(game)


def type_choice(game):
    """
    Player to choose its spot from 1 to 9 to mark.
    """
    while True:
        try:
            inp = int(input("Choose a spot from 1 to 9: "))
            if inp in range(10) and game[inp-1] == " ":
                game[inp-1] = current_player
            else: 
                clear_screen()
                print(f"Invalid value {inp} or spot already taken! Try again!")
                print_game(game) 
        except ValueError:
            print(f"Invalid input {inp}. Must be a number from 1- 9.")
            print_game(game)          
        finally:
            switch_player()

        print_game(game)        


def row_win(game):
    """
    Checks for all possible row matches to assign winner.
    """
    global winner

    if game[0] == game[1] == game[2] and game[0] != " ":
        winner = game[0]
        return True
    elif game[3] == game[4] == game[5] and game[3] != " ":
        winner = game[3]
        return True
    elif game[6] == game[7] == game[8] and game[6] != " ":
        winner = game[6]
        return True
    

def column_win(game):
    """
    Checks for all possible column matches to assign winner.
    """ 
    global winner

    if game[0] == game[3] == game[6] and game[0] != " ":
        winner = game[0]
        return True
    elif game[1] == game[4] == game[7] and game[1] != " ":
        winner = game[1]
        return True
    elif game[2] == game[5] == game[8] and game[2] != " ":
        winner = game[2]
        return True  


def diagonal_win(game):
    """
    Checks for the 2 diagonals matches to assign winner.
    """
    global winner

    if game[0] == game[4] == game[8] and game[0] != " ":
        winner = game[0]
        return True
    elif game[2] == game[4] == game[6] and game[2] != " ":
        winner = game[2]
        return True
    

def declare_win(game):
    """
    Declares the winner of the game.
    """    
    global game_running

    if column_win(game) or row_win(game) or diagonal_win(game):
        if winner == "X":
            print("Congrats! You won the game!")
        elif winner == "O":
            print("Sorry! Computer won!")
        restart_game()   
    else:
        declare_tie(game)         


def declare_tie(game):
    """
    If no winner, declares a tie.
    """        

    if " " not in game:
        print("No winner on this ocassion. It's a TIE!")

    restart_game()    


def switch_player():
    """
    Switch player once a spot has been marked.
    """
    global current_player    
    if current_player == "X":
        current_player = "O"
        computer(game)
    else:
        current_player = "X"    


def computer(game):
    """
    Computer makes random choice. 
    """
    global current_player

    while current_player == "O":
        position = random.randint(0, 8)
        if game[position] == " ":
            game[position] = "O"
            switch_player()


def restart_game():
    """
    Gives the user the option to restart or quit
    after declaring win or tie.
    """
    pass        

              
def main():
    """
    Runs all the program functions.
    """
    while game_running:
        intro_user_input()
        print_game(game)
        type_choice(game)
        switch_player()
        computer(game)
        declare_win(game)
        declare_tie(game)
        restart_game()


if __name__ == '__main__':
    while True:
        main()

