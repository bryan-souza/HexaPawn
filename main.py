import bus
import pygame
import os
from objects import Pawn
from ai import autoplay

def main():
    # SETUP SECTION
    
    pygame.init() # Initialize pygame

    # Load an image with pygame.image.load()
    # Use os.path.join if you have subdirs containing the images
    # like this project
    logo =  pygame.image.load( os.path.join("sprites", "logo32x32.png") )

    # Set the program icon
    pygame.display.set_icon( logo )

    # Define the name to be displayed on top of the window
    pygame.display.set_caption( "HexaPawn" )

    # Set the screen size (width, height)
    screen = pygame.display.set_mode( (640, 640) )
    running = True # Variable to control the running state

    # Load the board image
    board = pygame.image.load( os.path.join("sprites", "HexBoard.png") )

    # Initialize resources
    bus.init()

    # SETUP SECTION END
    while running: # Main loop
        # Event handling
        for event in pygame.event.get():
            # Handles QUIT state
            # Generally, the QUIT state is triggered when the close button is pressed
            # but it can be triggered if called from a object inside the game
            # like a close button when the gane is in fullscreen
            if (event.type == pygame.QUIT):
                running = False # Change the running state of the game

            if ( (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE) ):
                autoplay()

        # Show the board on screen
        screen.blit( board, (0, 0) )

        # Blit all pawns to the screen
        # Python generators are faster than for loops :D
        [ screen.blit(pawn.image, ( pawn.x, pawn.y )) for pawn in bus.judge.group ]

        # Update the game display
        pygame.display.flip()

if __name__ == "__main__":
    main()