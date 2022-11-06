"""
The base classes used by each role. Each role inherits from a genral Player but
has it's own functionality.

License:

Author: Will Roper (w.roper@sussex.ac.uk)
"""

# Define constants
role_order = ["Prostitue", "Bodyguard", "Seer", "Spellcaster", "Werewolf"]


class Villager:
    """ A generic villager object containing universal methods and attributes
        for all roles.
    """

    def __init__(self, player_name: str) -> None:

        # Name of the player and role
        self.player_name = player_name

        # Set up the default status conditions
        self.alive = True
        self.silenced = False  # spellcaster has silenced
        self.protected = False  # bodyguard has protected
        self.is_home = True  # is at home
        self.pros_visit = False  # is being visisted by the prostitute

        # Create a pointer to their lover for the couple
        self.lover = None

    def lynch_mob(self) -> None:
        """ This player has been voted to be killed.
        """

        # Hang the player
        self.alive = False

    def __add__(self, other: type[Player]) -> None:
        """ Overload the addition operator to make lovers.
        """

        # Link the lovers
        self.lover = other
        other.lover = self


class Werewolf(Villager):
    """ The werewolf class. A role which aims to kill all villagers.
    """

    def __init__(self, player_name: str) -> None:

        # Inherit Villager class attributes and methods
        super().__init__(player_name)

    def murder(self, other: type[Player]) -> None:
        """ This player has been killed by the werewolves.
        """

        # Kill the player
        other.alive = False

    def __multiply__(self, other: type[Player]) -> None:
        """ The multiplication operator uses this class's ability on another.
        """

        # Kill other player if they are home and not protected, and the
        # werewolf is able to kill.
        if other.is_home() and not other.protected and not self.pros_visit:
            self.murder(other)

            # Also kill the lover
            if other.lover is not None:
                self.murder(other.lover)


class Spellcaster(Villager):
    """ The Spellcaster role. A role which can silence players for the day.
    """

    def __init__(self, player_name: str) -> None:

        # Inherit Villager class attributes and methods
        super().__init__(player_name)

    def silence(self, other: type[Player]) -> None:
        """ This player has been silenced by the spellcaster.
        """

        # Silence the player
        other.silenced = True

    def __multiply__(self, other: type[Player]) -> None:
        """ The multiplication operator uses this class's ability on another.
        """

        # Silence other player if the spellcatser is able to
        if not self.pros_visit:
            self.silence(other)


class Prostitue(Villager):
    """ The Prostitue role. A role which can visit and 'preoccupy' another role.
    """

    def __init__(self, player_name: str) -> None:

        # Inherit Villager class attributes and methods
        super().__init__(player_name)

    def visit(self, other: type[Player]) -> None:
        """ This player has been visited by the prostitute.
        """

        # Visit the player
        other.pros_visit = True

    def __multiply__(self, other: type[Player]) -> None:
        """ The multiplication operator uses this class's ability on another.
        """

        # Visit other player
        self.visit(other)


class Bodyguard(Villager):
    """ The Bodyguard role. A role which can protect another player
        from the werewolves.
    """

    def __init__(self, player_name: str) -> None:

        # Inherit Villager class attributes and methods
        super().__init__(player_name)

    def protect(self, other: type[Player]) -> None:
        """ This player has been protected by the bodyguard.
        """

        # Protect the player
        other.protected = True

    def __multiply__(self, other: type[Player]) -> None:
        """ The multiplication operator uses this class's ability on another.
        """

        # Protect other player if the bodyguard is able to
        if not self.pros_visit:
            self.protect(other)


class Seer(Villager):
    """ The Seer role. A role which can investigate other players.
    """

    def __init__(self, player_name: str) -> None:

        # Inherit Villager class attributes and methods
        super().__init__(player_name)

    def investigate(self, other: type[Player]) -> None:
        """ Invetigate the other player.
        """

        # Invesitgate the player
        if isinstance(other, Werewolf):
            print("%s IS a Werewolf!" % other.name)
        else:
            print("%s IS NOT a Werewolf!" % other.name)

    def __multiply__(self, other: type[Player]) -> None:
        """ The multiplication operator uses this class's ability on another.
        """

        # Invesitgate the other player if the seer is able to
        if not self.pros_visit:
            self.investigate(other)
        else:
            print("Cannot say!")
