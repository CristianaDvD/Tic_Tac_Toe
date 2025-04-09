import random
import os
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


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
    print(Fore.LIGHTYELLOW_EX + "\n>>>>>>>> INSTRUCTIONS <<<<<<<<\n")
    print(" Tic-tac-toe is a game played on a three-by-three grid by")
    print(" two players, in this case you and the computer, who alternately")
    print(" place the marks X and O in one of the nine spaces in the grid.\n")
    print(" Consider a board with the nine positions numbered as follows:\n")
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + " 1 | 2 | 3 |")
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "---|---|---|")
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + " 4 | 5 | 6 |")
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + "---|---|---|")
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + " 7 | 8 | 9 |\n")
    print(" Choose a position from 1 to 9 in order to mark.")
    print(" Whoever gets the first 3 symbols in a row, column or diagonal,")
    print(" is the winner of the game!\n")
    print(Fore.GREEN + ">>>GOOD LUCK!<<<\n")
    print(" Type 's' to start the game or 'e' to exit:")
    while game_running:
        play_choice = input().strip().lower()
        if play_choice == 's':
            clear_screen()
            print_game(game)
        elif play_choice == 'e':
            clear_screen()
            print(Fore.LIGHTGREEN_EX +
                  "** Thank you! If you change your mind, **")
            print(Fore.LIGHTGREEN_EX + "*** please press Run program! ***")
            quit()
        else:
            print(Fore.LIGHTRED_EX + "Error! Please type in 's' or 'e'.")


def intro_user_input():
    """
    Welcomes the user and gives the option to continue or no.
    """
    print("\n" + Fore.LIGHTYELLOW_EX + Style.BRIGHT +
          "*" * 5 + " Welcome to TIC TAC TOE game " + "*" * 5 + "\n")
    print(" What is your name?")
    name = input().capitalize()
    print("")
    print("-" * 15 + "\n")
    if name.isalpha():
        print(f"{Fore.LIGHTGREEN_EX} Hi {name}! (•◡•) /\n")
        print(" Would you like to play Tic Tac Toe?")
        print(" Type 'y' for YES and 'n' for NO:")
        while game_running:
            user_choice = input().strip().lower()
            if user_choice == 'y':
                clear_screen()
                show_instructions()
            elif user_choice == 'n':
                clear_screen()
                print(Fore.LIGHTGREEN_EX +
                      "** Thank you! If you change your mind, **")
                print(Fore.LIGHTGREEN_EX + "*** please press Run program! ***")
                quit()
            else:
                print(Fore.LIGHTRED_EX + " Error! Please type 'y' or 'n'.")
    else:
        print(Fore.LIGHTRED_EX + " Invalid input. Only letters accepted.")
        print(Fore.LIGHTRED_EX + " Please try again.\n")
        intro_user_input()


def print_game(game):
    """
    Creates the game board,
    and prints reference board first for better UX.
    """
    print(Fore.LIGHTYELLOW_EX + "\n Reference board:\n")
    print(Fore.LIGHTYELLOW_EX + "1 | 2 | 3 |")
    print(Fore.LIGHTYELLOW_EX + "--|---|---|")
    print(Fore.LIGHTYELLOW_EX + "4 | 5 | 6 |")
    print(Fore.LIGHTYELLOW_EX + "--|---|---|")
    print(Fore.LIGHTYELLOW_EX + "7 | 8 | 9 |\n")
    print(Fore.BLUE + " Live play board:\n")
    print(Fore.BLUE + game[0] + " | " + game[1] + " | " + game[2] + " |")
    print(Fore.BLUE + "--|---|---|")
    print(Fore.BLUE + game[3] + " | " + game[4] + " | " + game[5] + " |")
    print(Fore.BLUE + "--|---|---|")
    print(Fore.BLUE + game[6] + " | " + game[7] + " | " + game[8] + " |" +
          "\n")

    type_choice(game)


def type_choice(game):
    """
    Player to choose its spot from 1 to 9 to mark.
    """
    while True:
        try:
            inp = int(input(" Choose a spot from 1 to 9: \n"))
            if inp in range(1, 10) and game[inp-1] == " ":
                game[inp-1] = current_player
                declare_win()
            else:
                clear_screen()
                print(f"{Fore.LIGHTRED_EX}Invalid value {inp} or spot" +
                      " already taken! Try again!")
                print_game(game)
        except ValueError:
            print(Fore.LIGHTRED_EX +
                  " Invalid input. Must be a number from 1- 9.")
            print_game(game)
        switch_player()
        print_game(game)
        declare_win()


def row_win(game):
    """
    Checks for all possible row matches to assign winner.
    """
    global winner
    global game_running

    if game[0] == game[1] == game[2] and game[0] != " ":
        winner = game[0]
        game_running = False
        return True
    elif game[3] == game[4] == game[5] and game[3] != " ":
        winner = game[3]
        game_running = False
        return True
    elif game[6] == game[7] == game[8] and game[6] != " ":
        winner = game[6]
        game_running = False
        return True


def column_win(game):
    """
    Checks for all possible column matches to assign winner.
    """
    global winner
    global game_running

    if game[0] == game[3] == game[6] and game[0] != " ":
        winner = game[0]
        game_running = False
        return True
    elif game[1] == game[4] == game[7] and game[1] != " ":
        winner = game[1]
        game_running = False
        return True
    elif game[2] == game[5] == game[8] and game[2] != " ":
        winner = game[2]
        game_running = False
        return True


def diagonal_win(game):
    """
    Checks for the 2 diagonals matches to assign winner.
    """
    global winner
    global game_running

    if game[0] == game[4] == game[8] and game[0] != " ":
        winner = game[0]
        game_running = False
        return True
    elif game[2] == game[4] == game[6] and game[2] != " ":
        winner = game[2]
        game_running = False
        return True


def declare_win():
    """
    Declares the winner of the game.
    """
    global game_running

    if column_win(game) or row_win(game) or diagonal_win(game):

        if winner == "X":
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT +
                  "☆★☆Congrats! You won the game!☆★☆")
            game_running = False
            restart_game(game)
        elif winner == "O":
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
                  "Sorry! Computer won! ◉︵◉")
            game_running = False
            restart_game(game)

    elif declare_tie(game):
        restart_game(game)


def declare_tie(game):
    """
    If no winner, declares a tie.
    """

    if " " not in game:
        print(Fore.BLUE + Style.BRIGHT +
              " No winner on this ocassion. It's a TIE! ( •_•)")
        return True


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
            declare_win()
            switch_player()


def reset_game():
    """
    Clears the game board if user choses to play again
    at the end of a game.
    """
    game.clear()
    game.extend([" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "])


def restart_game(game):
    """
    Gives the user the option to restart or quit
    after declaring win or tie.
    """
    print("\n Thank you for playing!")
    print(" Would you like to play again?")
    print(" Please type 'y' if YES or 'n' if NO:")
    while True:
        last_choice = input().strip().lower()
        if last_choice == "y":
            reset_game()
            clear_screen()
            print_game(game)
        elif last_choice == "n":
            clear_screen()
            print(Fore.CYAN + Style.BRIGHT +
                  "\n*** Thank you for playing! See you soon! ***")
            quit()
        else:
            print(Fore.LIGHTRED_EX +
                  " Invalid input. Please type 'y' or 'n'!")


def main():
    """
    Calls out the intro to the game.
    """
    while game_running:
        intro_user_input()


if __name__ == '__main__':
    while True:
        main()
