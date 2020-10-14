import pygame, os

class Pawn(pygame.sprite.Sprite):
    """
    Put some decent documentation on me you punk
    Note: all the move validators will be stored at the ai module
    """
    def __init__(self, id, color, start_pos):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.start_pos = start_pos
        self.color = color
        self.image = pygame.image.load( os.path.join("sprites", color + "Pawn.png") ).convert_alpha()
        self.x = start_pos[0]
        self.y = start_pos[1]

    def move(self):
        """
        Moves the pawn one square foward
        """
        if (self.color == "white"):
            self.y -= 214
        else:
            self.y += 214

    def capture(self, direction):
        """
        Captures a pawn at the given direction
        (Basically moves diagonally :D)
        """
        self.move()
        if (direction == 'left'):
            self.x -= 214
        else:
            self.x += 214

