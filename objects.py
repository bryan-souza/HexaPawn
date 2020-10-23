import pygame
import os
import bus

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
    Put some decent documentation on me you punk
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
        self.x, self.y = move_table[new_id]
        self.id = new_id

    def get_movelist(self):
        # Init
        moves = []
        col_dict = {
            "a": ["b"],
            "b": ["a", "c"],
            "c": ["b"]
        }

        # Check for movements
        if (bus.judge.move_check(self.id)[0] == True):
            moves.append(
                f'{self.id[0]}{int(self.id[1]) + (-1 if (self.color == "black") else 1)}')

        # Check for captures
        for col in col_dict[self.id[0]]:
            if (bus.judge.capture_check(self.id, f'{col}{int(self.id[1]) + (-1 if (self.color == "black") else 1)}')[0] == True):
                moves.append(
                    f'{self.id[0]}x{col}{int(self.id[1]) + (-1 if (self.color == "black") else 1)}')

        return moves

    def handle_click(self, pos):
        min_x = self.x
        max_x = self.x + 213

        min_y = self.y
        max_y = self.y + 213

        if (((pos[0] >= min_x) and (pos[0] <= max_x)) and ((pos[1] >= min_y) and (pos[1] <= max_y))):
            return True
        else:
            return False


class Outline(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, action, mode='borderless'):
        pygame.sprite.Sprite.__init__(self)
        self.action = action # Movecode for this outline
        self.position = move_table[f'{action[::-1][1]}{action[::-1][0]}'] # (x, y)
        self.type = 'move' if (len(action) == 2) else 'capture'

        # Load animation frames
        self.images = []
        for x in range(4):
            self.images.append(
                os.path.join(
                    'sprites',
                    f'{self.type}Outline{mode.capitalize()}_{x}.png'
                )
            )

        self.index = 0
        self.image = pygame.image.load( self.images[self.index] ).convert_alpha()

    def update(self):
        """
        Iterates to the next frame;
        resets if the counter passes 3
        """
        self.index += 1
        if (self.index > 3):
            self.index = 0
        self.image = pygame.image.load( self.images[self.index] ).convert_alpha()

    def handle_click(self, pos):
        min_x, min_y = self.position
        max_x, max_y = min_x + 213, min_y + 213

        if (((pos[0] >= min_x) and (pos[0] <= max_x)) and ((pos[1] >= min_y) and (pos[1] <= max_y))):
            return self.action