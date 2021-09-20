import pygame
from json import load
from objects import Pawn

achievements = load( open('.achievements.json') )
class Validator:
    """
    Class used to validate movements and victory checking (a judge, basically)

    Parameters
    ----------
    group : list[Pawn]
        A list of Pawn objects that are actually in the game (weren't captured
        yet)

    Attributes
    ----------
    group : list[Pawn]
        The pawns inside the game
    ids : dict
        ID table used to know who's where
    stack : list[str]
        The movement call stack of the game
    move_counter: int
        Counter to keep track of how many movements
        were made in the game
    black_wins : int
        Counts how many times the black pawns won
    white_wins: int
        Counts how many times the white pawns won

    Methods
    -------
    reset()
        Rolls back all attributes to it's original
        state when the object was created, keeping
        only move_count, black_wins and white_wins
        untouched
    check()
        Checks if the given movecode can be executed;
        if valid movecode is given, it'll update
        the pawns' positions and other game variables
        regarding movements or captures
    victory_validator()
        Checks if the actual game state of the board
        meets any of the requirements of the game to
        count as a win; returns the color who won or
        None if no victory situation was found
    get_movelist()
        Returns all possible movements for the given
        Pawn object, at the current game state
    """

    # Constructor
    def __init__(self, group):
        self.group = group
        self.ids = {}
        self.stack = [] # Move call stack for the entire game
        self.move_counter = 0
        self.black_wins = 0
        self.white_wins = 0
        
        # Create a dictionary containing all pawn ids
        # and its respective position in the group
        for pawn in self.group:
            self.ids.update({pawn.id: pawn})

    # Pawn id updater
    def __update_ids(self):
        """
        [Private Method]
        Resets and recreates the IDs table based on the game table

        Returns
        -------
        None
            Since it is just updating a class attribute, theres no
            need to return information
        """
        # Reset the id dictionary
        self.ids = {}

        # Fill the dict w/ valid pawn ids
        for pawn in self.group:
            self.ids.update({pawn.id: pawn})

    # Move tester
    def __move(self, pawn_id):
        """
        [Private Method]
        Checks if the given pawn can move ahead

        Returns
        -------
        tuple: (bool, str)
            Returns a tuple containing a boolean
            to describe if the movement was made
            or not, and a string containing a 
            message to be shown on the python
            shell
        """
        # Try to fetch the pawn object
        try:
            # Fetch the pawn object by id
            pawn = self.ids[pawn_id]

            # Get the destination square by doing some maths :D
            destination = f'{pawn_id[0]}{int(pawn_id[1]) + (1 if (pawn.color == "white") else -1)}'
        except KeyError:
            return (None, "[ERROR] Pawn not found")

        # Tests if there's any pawn in the destination square
        test_list = [ True if (test.id == destination) else False for test in self.group ]
        
        if ( test_list.count(True) > 0 ):
            # Yep, there's a pawn ahead, so don't move
            # raise a debug message
            return (False, "[ERROR] Can't move this pawn, there's another pawn at the destination")

        else:
            # There's no pawn ahead, so it can move
            return [True, f"[MOVE] {destination}"]

    # Capture tester
    def __capture(self, pawn_id, target):
        """
        [Private Method]
        Checks if the given pawn can capture
        the given target

        Returns
        -------
        tuple: (bool, str)
            Returns a tuple containing a boolean
            to describe if the capture was made
            or not, and a string containing a 
            message to be shown on the python
            shell
        """
        # Try to fetch the required objects
        try:
            # Fetch the pawn object by id
            pawn = self.ids[pawn_id]

            # Fetch the target pawn object by id
            tgt = self.ids[target]

        except KeyError:
            return (None, "[ERROR] Pawn not found")

        # Check if the pawns have different colors
        if (pawn.color != tgt.color):
            return (True, f'[CAPTURE] {pawn_id[0]}x{tgt.id}') # Can capture

        else:
            return (False, "[ERROR] The pawns have the same color") # Can't capture

    # Reset the board state
    def reset(self, silent=False):
        """
        Resets game variables to it's initial
        state, except moves_counter, black_wins
        and white_wins

        Returns
        -------
        None
            Since it is just rolling back some game
            variables, there's no need to return
            information
        """
        # Clear the pawn groups
        self.group = []

        # Recreate all pawns at its initial state
        self.group.append( Pawn("black", "a3", silent))
        self.group.append( Pawn("black", "b3", silent))
        self.group.append( Pawn("black", "c3", silent))
        self.group.append( Pawn("white", "a1", silent))
        self.group.append( Pawn("white", "b1", silent))
        self.group.append( Pawn("white", "c1", silent))

        # Update the id list
        self.__update_ids()

        # Reset the move counter
        self.move_counter = 0
        
    # Move decoder; transforms strings (movecode)
    # into pawn actions
    def check(self, movecode, silent=False):
        """
        Pawn move decoder.
        Checks and executes (if possible) the given movecodes;
        raises an error if a invalid movecode is given

        Conventions:
            - [destination_square] -> Moves a pawn to the specified square
            - [pawn_x]x[destination_square] -> Captures the pawn at the specified square

        Examples:
        a2 -> Moves a pawn to the a2 position
        axb2 -> Pawn at a1 captures a pawn at b2

        Returns
        -------
        None
            Either the game will update the pawns positions or will print a debug message
            on the python shell
        """
        if ( len(movecode) == 2 ):
            # Pawn movement
            pawn_id = f'{movecode[0]}{int(movecode[1]) + (-1 if (self.move_counter % 2 == 0) else 1)}'
            result = self.__move(pawn_id)
            if (result[0] == True):
                self.ids[pawn_id].update_id(movecode)
                self.move_counter += 1
                self.__update_ids()

            if (silent == False):
                print(result[1])

        elif ( len(movecode) == 4 ):
            # Pawn capture
            pawn_id = f'{movecode[0]}{int(movecode[3]) + (-1 if (self.move_counter % 2 == 0) else 1)}'
            target = f'{movecode[2]}{movecode[3]}'
            result = self.__capture(pawn_id, target)

            if (result[0] == True):
                # Remove the target pawn
                for p in self.group:
                    if (p.id == target):
                        rm_index = self.group.index(p)
                        break
                else:
                    print( achievements['0xff'] )

                self.group.pop(rm_index)
                self.ids[pawn_id].update_id(target)
                self.move_counter += 1
                self.__update_ids()
            
            if (silent == False):
                print(result[1]) # Logs the move result

        # Since a valid movement was made, add it to
        # the game call stack'
        if (result[0]):
            self.stack.append(movecode)

        else:
            print("[ERROR] Invalid movecode")

    # Checks if any of the sides have won
    # Resets the game if a victory is detected
    def victory_validator(self, silent=False):
        """
        Da Rules:
          You (Whites) win if:
            A: Cross the board first
            B: Capture all my pawns

          I (Blacks) win if:
            A: Cross the board first
            B: Capture all of your pawns
            C: There's no valid movement left

        Returns
        -------
        str: 'black'
            If a black win is detected, return
            a string containing its color
        str: 'white'
            If a white win is detected, return
            a string containing its color
        None
            If neither blacks or whites won
        """
        # Display meme achievement
        if (self.black_wins == 10):
            print( achievements['0x77'] )

        # Check if any pawn crossed the board
        for k, v in self.ids.items():
            # Check if any black pawn crossed the board
            if (k in ['a1', 'b1', 'c1'] and v.color == 'black'):
                self.black_wins += 1
                if silent: self.reset(silent)
                return 'black'

            # Check if any white pawn crossed the board
            if (k in ['a3', 'b3', 'c3'] and v.color == 'white'):
                self.white_wins += 1
                if silent: self.reset(silent)
                return 'white'

        # Check if there's only one pawn color present in the board
        colors = [ pawn.color for pawn in self.group ]
        if (colors.count('white') == 0):
            self.black_wins += 1
            if silent: self.reset(silent)
            return 'black'
        
        if (colors.count('black') == 0):
            self.white_wins += 1
            if silent: self.reset(silent)
            return 'white'

        # Check if there's any valid movement left
        states = []
        for pawn in self.group:
            moves = self.get_movelist(pawn)
            # Check for movementation
            # If any movecode has length 2 (a movement)
            if ( any([True if len(x) == 2 else False for x in moves]) ):
                states.append(True)
            elif ( any([True if len(x) == 4 else False for x in moves]) ):
                # This pawn can capture another pawn, so there's still a valid move
                states.append(True)
            else:
                # No valid moves for that pawn
                states.append(False)

        # Finally, checks if there's no valid movement left
        if (states.count(True) == 0):
            self.black_wins += 1
            if silent: self.reset(silent)
            return 'black'

    def get_movelist(self, pawn):
        """
        Get all possible movements for a pawn
        at the current game state

        Returns:
        moves : list[str]
            A list of strings containing the movecodes
            for all possible movements for a pawn
        """
        # Init
        moves = []
        col_dict = {
            "a": ["b"],
            "b": ["a", "c"],
            "c": ["b"]
        }

        # Check for movements
        if (self.__move(pawn.id)[0] == True):
            moves.append(
                f'{pawn.id[0]}{int(pawn.id[1]) + (-1 if (pawn.color == "black") else 1)}')

        # Check for captures
        for col in col_dict[pawn.id[0]]:
            if (self.__capture(pawn.id, f'{col}{int(pawn.id[1]) + (-1 if (pawn.color == "black") else 1)}')[0] == True):
                moves.append(
                    f'{pawn.id[0]}x{col}{int(pawn.id[1]) + (-1 if (pawn.color == "black") else 1)}')

        return moves
