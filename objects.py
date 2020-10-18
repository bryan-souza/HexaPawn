import pygame, os

class Pawn(pygame.sprite.Sprite):
    """
    Put some decent documentation on me you punk
    Note: all the move validators will be stored at the ai module
    """
    def __init__(self, color, start_pos, silent=False):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        
        if (silent == False):
            self.image = pygame.image.load( os.path.join("sprites", color + "Pawn.png") ).convert_alpha()
        
        self.move_table = {
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
        self.x, self.y = self.move_table[start_pos]
        self.id = start_pos

    # Updates the current pawn id and its position
    def update_id(self, new_id):
        self.x, self.y = self.move_table[new_id]
        self.id = new_id
