"""
HexaPawn objects module

A module for storing (and providing) game objects
e.g. Pawns, Move indicators
"""

import pygame
import os

move_table = {
    "a1": [0, 428],
    "b1": [214, 428],
    "c1": [428, 428],
    "a2": [0, 214],
    "b2": [214, 214],
    "c2": [428, 214],
    "a3": [0, 0],
    "b3": [214, 0],
    "c3": [428, 0],
}


class Pawn(pygame.sprite.Sprite):
    """
    A object representing a chess pawn

    Parameters
    ----------
    color : str
        Defines which sprite image to use;
        choose between 'black' or 'white'
    start_pos : str
        Defines in which square the pawn
        will be positioned when the game
        starts
    silent : bool, optional
        Defines whenever the sprite should
        be rendered or not

    Attributes
    ----------
    color : str
        The color of this pawn
    image : Surface
        The corresponding pawn sprite for
        this pawn
    x : int
        The position in the x axis (in pixels) for this pawn
    y : int
        The position in the y axis (in pixels) for this pawn
    id : str
        The square that this pawn is located
        (chess convention)

    Methods
    -------
    update_id(new_id)
        Changes the pawn square, its id and
        its position on screen (x, y)
    get_movelist()
        Returns a list of strings containing
        all the moves that this pawn can make
        at the current game state
    handle_click()
        Returns True if the mouse was clicked
        while above this pawn; returns False
        if the mouse wasn't above this pawn
    """
    # Constructor

    def __init__(self, color, start_pos, silent=False):
        pygame.sprite.Sprite.__init__(self)
        self.color = color

        if (silent == False):
            self.image = pygame.image.load(os.path.join(
                "sprites", color + "Pawn.png")).convert_alpha()

        self.x, self.y = move_table[start_pos]
        self.id = start_pos

    # Updates the current pawn id and its position
    def update_id(self, new_id):
        """
        Changes the pawn position on screen
        and its id

        Parameters
        ----------
        new_id : str
            The square coordinates to where
            to move the pawn

        Returns
        -------
        None
            The action was successfully completed

        Raises
        ------
        KeyError
            The given coordinates couldn't be found
            in the move table

        """
        self.x, self.y = move_table[new_id]
        self.id = new_id

    def handle_click(self, pos):
        """
        Checks if this pawn was clicked or not

        Parameters
        ----------
        pos : pygame.event.pos
            The mouse coordinates

        Returns
        -------
        bool
            True if it was clicked; False if it wasn't
        """
        min_x = self.x
        max_x = self.x + 213

        min_y = self.y
        max_y = self.y + 213

        if (((pos[0] >= min_x) and (pos[0] <= max_x)) and ((pos[1] >= min_y) and (pos[1] <= max_y))):
            return True
        else:
            return False


class Outline(pygame.sprite.Sprite):
    """
    A object representing a move indicator on the screen

    Parameters
    ----------
    action : str
        The movecode that this outline is representing;
        Determines the color and position on screen
        to the outline

    Attributes
    ----------
    action : str
        The movecode that this outline is representing
    position : str
        The square which this outline will be rendered on
    type : str
        The type of action this outline is representing
    images : list[Surface]
        A list of sprite images to generate the animation
        effect
    index : int
        The animation frame that is being rendered
    image : Surface
        The current animation frame

    Methods
    -------
    update()
        Updates the current animation frame;
        makes the animation effect work
    handle_click(pos):
        Checks if the outline was clicked;
        executes the move bound to this outline
        when clicked
    """

    # Constructor
    def __init__(self, action):
        pygame.sprite.Sprite.__init__(self)
        self.action = action  # Movecode for this outline
        # (x, y)
        self.position = move_table[f'{action[::-1][1]}{action[::-1][0]}']
        self.type = 'move' if (len(action) == 2) else 'capture'

        # Load animation frames
        self.images = []
        for x in range(4):
            self.images.append(
                os.path.join(
                    'sprites',
                    f'{self.type}OutlineBorderless_{x}.png'
                )
            )

        self.index = 0
        self.image = pygame.image.load(self.images[self.index]).convert_alpha()

    def update(self):
        """
        Iterates to the next frame;
        resets if the counter passes 3
        """
        self.index += 1
        if (self.index > 3):
            self.index = 0
        self.image = pygame.image.load(self.images[self.index]).convert_alpha()

    def handle_click(self, pos):
        """
        Checks whenever this outline was clicked;
        returns the action bound to this ouline

        Parameters
        ----------
        pos : pygame.event.pos
            The actual mouse position

        Returns
        -------
        str
            The movecode bound to this ouline
        """
        min_x, min_y = self.position
        max_x, max_y = min_x + 213, min_y + 213

        if (((pos[0] >= min_x) and (pos[0] <= max_x)) and ((pos[1] >= min_y) and (pos[1] <= max_y))):
            return self.action
