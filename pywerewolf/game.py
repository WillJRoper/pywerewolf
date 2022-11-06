"""
The main game object that tracks rounds and resolves all interactions.

License:

Author: Will Roper (w.roper@sussex.ac.uk)
"""
from roles import role_order
from roles import Villager, Werewolf, Spellcaster, Bodyguard, Seer, Prostitue


class Game:
    """ The main game class. This contains everything needed to track the
        state of the game.
    """

    def __init__(self, ) -> None:

        # Define metadata we need to track
        self.night = 0
        self.nplayers = 0
        self.nwerewolves = 0

        # Players in the game
        self.players = {}

        # Roles in the game
        self.roles = {}

        # Set up the game
        self.setup()

    def setup(self, simulated=False) -> None:
        """ This function sets up the initial state of the game.

        :param: simulated: If True it won't ask for names or other real world
                           information.
        :return:
        """

        if not simulated:

            # Get all player names?
            for role in role_order:
                self.players[role] = input("Who is the %s?" % role)

            # Set up role instances

        else:
            pass

    def night_time(self,) -> None:
        """ This is the main round function. Each player gets a chance to use
            their ability and then the logic in the chaos is resolved to give
            the game state at dawn the next day.
        """

        # We're done, increment the night count
        self.night += 1

        # And report the game state
        print("So and so Died")


class SimulatedGame(Game):
    """ The main game class used when simulating games. This contains all the
        normal game functionality but also extra functionality needed when
        simulating a game.
    """

    def __init__(self) -> None:

        # Get all the properties and methods from the parent game class
        super().__init__()

    def inherit_game_state(self, other_game) -> None:
        """ A helper function to cleanly inherit the state of an existing game.
        """

        # Loop over the other game and get it's state to intialise this one.
        for key, val in other_game.__dict__:
            self.__dict__[key] = val
