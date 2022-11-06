"""
The main game object that tracks rounds and resolves all interactions.

License:

Author: Will Roper (w.roper@sussex.ac.uk)
"""
from roles import *


class Game:
    """ The main game class. This contains everything needed to track the
        state of the game.
    """

    def __init__(self, ) -> None:

        # Define metadata we need to track
        self.night = 0
        self.nplayers = 0

        # Players in the game
        self.players = {}


class SimulatedGame(Game):
    """ The main game class used when simulating games. This contains all the
        normal game functionality but also extra functionality needed when
        simulating a game.
    """

    def __init__(self) -> None:

        # Get all the properties and methods from the parent game class
        super().__init()

    def inherit_game_state(self, other_game) -> None:
        """ A helper function to cleanly inherit the state of an existing game.
        """

        # Loop over the other game and get it's state to intialise this one.
        for key, val in other_game.__dict__:
            self.__dict__[key] = val
