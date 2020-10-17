from objects import Pawn
from validators import Validator
import pygame
import os

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

    # Create a group to store all pawns in the game
    pawns = []

    # Please optimize this cringy pawn generator
    pawns.append( Pawn("black", "a3"))
    pawns.append( Pawn("black", "b3"))
    pawns.append( Pawn("black", "c3"))
    pawns.append( Pawn("white", "a1"))
    pawns.append( Pawn("white", "b1"))
    pawns.append( Pawn("white", "c1"))

    # Instantiate a validator object
    judge = Validator(pawns)

    # DEBUG SESSION

    move_cntr = 0

    # List of movements to test the validator
    # Whites Move, Blacks Move
    session = [
        'a2', 'bxa2',
        'b2', 'a1',
    ]

    # END DEBUG SESSION

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
                if (move_cntr < len(session)):
                    judge.check(session[move_cntr])
                    move_cntr += 1

        # Show the board on screen
        screen.blit( board, (0, 0) )

        # Blit all pawns to the screen
        # Python generators are faster than for loops :D
        [ screen.blit(pawn.image, ( pawn.x, pawn.y )) for pawn in judge.group ]

        # Update the game display
        pygame.display.flip()

        # Check if anyone won
        judge.victory_validator()

if __name__ == "__main__":
    main()