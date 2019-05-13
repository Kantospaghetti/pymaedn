from tkinter import *
from random import randint

PLAYERS = [
    "blue",
    "red",
    "green",
    "yellow"
]
FIELD_SIZE = 4
FIELD_COLOR = "black"
FIELD_POSITIONS = [
    (10, 4),
    (9, 4),
    (8, 4),
    (7, 4),
    (6, 4),
    (6, 3),
    (6, 2),
    (6, 1),
    (6, 0),
    (5, 0),
    (4, 0),
    (4, 1),
    (4, 2),
    (4, 3),
    (4, 4),
    (3, 4),
    (2, 4),
    (1, 4),
    (0, 4), (0, 5), (0, 6),
    (1, 6), (2, 6), (3, 6)
    
] 

class Field:
    """Graphical represantation of a field. """
    def __init__(self, master, row, column):
        self.label = Label(master=master, bg=FIELD_COLOR, width=FIELD_SIZE, height=FIELD_SIZE//2)
        self.label.grid(row=row, column=column)

    def enter_player(self, player):
        """Change field color to player color."""
        pass

class Figure:
    """Graphical representation of a game figure."""
    def __init__(self, player):
        self.player = player
        self.position = 0

class Player:
    """Virtual representation of a player."""
    def __init__(self, color):
        self.color = color

class Gamemanager:
    """Global core gameplay mechanics."""
    def __init__(self):
        self.master = None
        self.players = []
        self.board = []

    def create_board(self, master):
        for color in PLAYERS:
            # create player
            player = Player(color)
            self.players.append(player)
        # create board quater
        for position in FIELD_POSITIONS:
            (row, column) = position
            field = Field(master, row, column)
            self.board.append(field)
            
            
class Application:
    """Manage the Tkinter root window."""
    def __init__(self, root):
        self.root = root
        gamemanager.create_board(root)

root = Tk()
gamemanager = Gamemanager()

Application(root)

root.mainloop()
