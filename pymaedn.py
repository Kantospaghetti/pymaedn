from tkinter import *

PLAYERS = [
    "blue",
    "red",
    "green",
    "yellow"
]

class Field:
    """Graphical represantation of a field. """
    def __init__(self, position, master):
        self.label = Label(master=master)

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
    def __init__(self, number, color):
        self.number = number
        self.color = color

class Gamemanager:
    """Global core gameplay mechanics."""
    def __init__(self):
        self.players = []

    def create_board(self, master):
        for number, color in enumerate(PLAYERS):
            player = Player(number, color)
            self.players.append(player)
            
class Application:
    """Manage the Tkinter root window."""
    def __init__(self, root):
        self.root = root
        gamemanager.create_board(root)

root = Tk()
gamemanager = Gamemanager()

Application(root)

root.mainloop()
