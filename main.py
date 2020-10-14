from objects import Pawn
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

    # X and Y axis positions
    x_axis = [0, 214, 428]
    y_axis = [0, 214, 428]

    # Please optimize this cringy pawn generator
    pawns.append( Pawn("B1", "black", ( x_axis[0], y_axis[0] )) )
    pawns.append( Pawn("B2", "black", ( x_axis[1], y_axis[0] )) )
    pawns.append( Pawn("B3", "black", ( x_axis[2], y_axis[0] )) )
    pawns.append( Pawn("W1", "white", ( x_axis[0], y_axis[2] )) )
    pawns.append( Pawn("W2", "white", ( x_axis[1], y_axis[2] )) )
    pawns.append( Pawn("W3", "white", ( x_axis[2], y_axis[2] )) )

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

            if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_w):
                print("dbg")
                pawns[0].capture("right")

        # Show the board on screen
        screen.blit( board, (0, 0) )

        # Blit all pawns to the screen
        # Python generators are faster than for loops :D
        [ screen.blit(pawn.image, ( pawn.x, pawn.y )) for pawn in pawns ]

        # Update the game display
        pygame.display.flip()

if __name__ == "__main__":
    main()