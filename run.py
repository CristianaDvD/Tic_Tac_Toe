import tkinter
import random


# Global variables
current_player = "X"
board = [[0, 0, 0],
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


""" 
Code inspired from https://www.youtube.com/watch?v=nbRpDXV7QDM
to create window for tic tac toe game. 
More info in Readme
"""


