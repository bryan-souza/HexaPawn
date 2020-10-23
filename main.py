import bus
import pygame
import os
from objects import Pawn, Outline
from ai import autoplay


def main():
    # SETUP SECTION

    pygame.init() # Initialize pygame

    # Load an image with pygame.image.load()
    # Use os.path.join if you have subdirs containing the images
    # like this project
    logo = pygame.image.load(os.path.join("sprites", "logo32x32.png"))

    # Set the program icon
    pygame.display.set_icon(logo)

    # Define the name to be displayed on top of the window
    pygame.display.set_caption("HexaPawn")

    # Set the screen size (width, height)
    screen = pygame.display.set_mode((640, 640))
    running = True  # Variable to control the running state

    # Time and frame control
    clock = pygame.time.Clock()

    # Load the board image
    board = pygame.image.load(os.path.join("sprites", "HexBoard.png"))

    # Initialize resources
    bus.init()

    # List of movement outlines to be rendered
    outlines = []

    # SETUP SECTION END
    while running:  # Main loop
        # Event handling
        for event in pygame.event.get():
            # Handles QUIT state
            # Generally, the QUIT state is triggered when the close button is pressed
            # but it can be triggered if called from a object inside the game
            # like a close button when the gane is in fullscreen
            if (event.type == pygame.QUIT):
                bus.ai.plot()
                running = False  # Change the running state of the game

            if (event.type == pygame.MOUSEBUTTONDOWN):
                # Checks for click in every white pawn in the board
                for pawn in bus.judge.group:
                    if (pawn.color == 'white') and (pawn.handle_click(event.pos) == True):
                        # Clear all outlines
                        outlines = []

                        # Fetch all possible moves for the chosen pawn
                        moves = pawn.get_movelist()

                        for move in moves:
                            outlines.append(Outline(move))
                else:
                    for out in outlines:
                        move = out.handle_click(event.pos)
                        if (move != None):
                            outlines = [] # Clear all outlines
                            bus.judge.check(move) # Execute the move

                            # Sync changes
                            screen.blit(board, (0, 0))
                            [screen.blit(pawn.image, (pawn.x, pawn.y)) for pawn in bus.judge.group]
                            pygame.display.flip()

                            pygame.time.delay(500) # Await 0.5 seconds
                            bus.ai.step(move) # Notify AI
                            break

                # autoplay()

        # Show the board on screen
        screen.blit(board, (0, 0))

        # Blit all pawns to the screen
        # Python generators are faster than for loops :D
        [screen.blit(pawn.image, (pawn.x, pawn.y)) for pawn in bus.judge.group]

        # Blit all outlines on screen
        if (outlines != []):
            [out.update() for out in outlines]
            [screen.blit(out.image, out.position) for out in outlines]

        # Update the game display
        pygame.display.flip()

        # Delay the next loop iteration in 8 fps
        clock.tick(8)

if __name__ == "__main__":
    main()
