import pygame
import os
from pygame import time
import pygame_gui
from json import dump, load
from random import choice
from objects import Pawn, Outline
from ai import Ai
from ui import UI
from validators import Validator


class Game():
    def __init__(self):
        # Initialize or import config file
        try:
            # Try to load config from file
            self.config = load( open('config.json') )
            self.achievements = load( open('achievements.json') )
        except:
            # Annoy the user until it puts the file back
            while True:
                try:
                    self.config = load( open('config.json') )
                    self.achievements = load( open('achievements.json') )

                    # Give achievement
                    print( self.achievements['0x69'] )

                    break
                except:
                    print("PUT IT BACK!")
                    time.wait(500)

        # SETUP SECTION
        pygame.init()  # Initialize pygame

        # Load an image with pygame.image.load()
        # Use os.path.join if you have subdirs containing the images
        # like this project
        logo = pygame.image.load(os.path.join("sprites", "logo32x32.png"))

        # Set the program icon
        pygame.display.set_icon(logo)

        # Define the name to be displayed on top of the window
        pygame.display.set_caption("HexaPawn")

        # Set the screen size (width, height)
        self.screen_width = 1040
        self.screen_height = 640
        self.screen = pygame.display.set_mode( (self.screen_width, self.screen_height) )
        self.running = True  # Variable to control the running state

        # Time and frame control
        self.clock = pygame.time.Clock()
        self.paused = False

        # Load the board image
        self.board = pygame.image.load(os.path.join("sprites", "HexBoard.png"))

        # Initialize UI
        self.ui = UI( self.screen_width, self.screen_height )

        # List of movement outlines to be rendered
        self.outlines = []

        # Playmode
        self.playmode = 'manual'

        # SETUP SECTION END

        pawns = [
            Pawn("black", "a3"),
            Pawn("black", "b3"),
            Pawn("black", "c3"),
            Pawn("white", "a1"),
            Pawn("white", "b1"),
            Pawn("white", "c1")
        ]
        self.judge = Validator(pawns)
        self.ai = Ai(self.judge)

    def autoplay(self):
        """
        Checks for moves that the white pawns can make
        given the current game state, picks and execute
        a random move.
        """
        # Column capture resolver
        col_dict = {
            "a": ["b"],
            "b": ["a", "c"],
            "c": ["b"]
        }

        # Sort white pawns
        whites = []
        for pawn in self.judge.group:
            if (pawn.color == 'white'):
                whites.append(pawn)

        # Fetch all white possible moves
        moves = []
        for pawn in whites:
            # Check for movements
            if (self.judge.move(pawn.id)[0] == True):
                moves.append(f'{pawn.id[0]}{int(pawn.id[1]) + 1}')

            # Check for captures
            for col in col_dict[pawn.id[0]]:
                if (self.judge.capture(pawn.id, f'{col}{int(pawn.id[1]) + 1}')[0] == True):
                    moves.append(f'{pawn.id[0]}x{col}{int(pawn.id[1]) + 1}')

        # Pick a random move and execute
        move = choice(moves)
        self.judge.check(move)

        # Sync changes
        self.screen.blit(self.board, (0, 0))
        [self.screen.blit(pawn.image, (pawn.x, pawn.y))
            for pawn in self.judge.group]
        pygame.display.flip()

        pygame.time.wait(500)  # Await 0.5 seconds
        self.ai.step(move)  # Notify AI

        # Sync changes
        self.screen.blit(self.board, (0, 0))
        [self.screen.blit(pawn.image, (pawn.x, pawn.y))
            for pawn in self.judge.group]
        pygame.display.flip()

        pygame.time.wait(500)
        if (self.judge.victory_validator() != None):
            pygame.time.wait(250)
            self.judge.reset()

    def run(self):
        try:
            while self.running:  # Main loop
                time_delta = self.clock.tick(30)/1000.0
                # Event handling
                for event in pygame.event.get():
                    # Handles QUIT state
                    # Generally, the QUIT state is triggered when the close button is pressed
                    # but it can be triggered if called from a object inside the game
                    # like a close button when the gane is in fullscreen
                    if (event.type == pygame.QUIT):
                        if (self.config['enable_plots']): self.ai.plot()
                        running = False  # Change the running state of the game

                    # Mouse events
                    if (event.type == pygame.MOUSEBUTTONDOWN):
                        if (self.paused == False):
                            # Checks for click in every white pawn in the board
                            if (self.playmode == 'manual'):
                                for pawn in self.judge.group:
                                    if (pawn.color == 'white') and (pawn.handle_click(event.pos) == True):
                                        # Clear all outlines
                                        self.outlines = []

                                        # Fetch all possible moves for the chosen pawn
                                        moves = self.judge.get_movelist(pawn)

                                        for move in moves:
                                            self.outlines.append(Outline(move))
                                        break
                                else:
                                    for out in self.outlines:
                                        move = out.handle_click(event.pos)
                                        if (move != None):
                                            self.outlines = []  # Clear all outlines
                                            self.judge.check(move)  # Execute the move

                                            # Sync changes
                                            self.screen.blit(self.board, (0, 0))
                                            [self.screen.blit(pawn.image, (pawn.x, pawn.y))
                                            for pawn in self.judge.group]
                                            pygame.display.flip()

                                            pygame.time.wait(500)  # Await 0.5 seconds
                                            self.ai.step(move)  # Notify AI

                                            # Sync changes
                                            self.screen.blit(self.board, (0, 0))
                                            [self.screen.blit(pawn.image, (pawn.x, pawn.y))
                                            for pawn in self.judge.group]
                                            pygame.display.flip()

                                            pygame.time.wait(500)
                                            if (self.judge.victory_validator() != None):
                                                pygame.time.wait(250)
                                                self.judge.reset()
                                            break

                    # UI events
                    if (event.type == pygame.USEREVENT):
                        if (event.user_type == pygame_gui.UI_BUTTON_PRESSED):
                            if (event.ui_element == self.ui.btn_apply):
                                # Apply settings

                                # Playmode
                                if (self.ui.sldr_playmode.current_value == 0):
                                    playmode = 'manual'
                                elif (self.ui.sldr_playmode.current_value == 1):
                                    playmode = 'automatic'

                                # AI mode
                                mode = self.ui.lst_ai_modes.get_single_selection()
                                if (mode != None):
                                    self.ai = Ai(self.judge, mode=mode.lower)

                                self.judge.reset()

                    # Keyboard events
                    if (event.type == pygame.KEYDOWN):
                        if (event.key == pygame.K_SPACE):
                            # Pause the game
                            self.paused = not self.paused
                            self.ui.img_paused.visible = not self.ui.img_paused.visible

                    self.ui.manager.process_events(event)

                # Update the UI manager
                self.ui.manager.update(time_delta)

                # Run the game if mode is set to automatic
                if (self.playmode == 'automatic') and (self.paused == False):
                    pygame.time.wait(500)
                    self.autoplay()

                # Show the board on screen
                self.screen.blit(self.board, (0, 0))

                # Blit all pawns to the screen
                # Python generators are faster than for loops :D
                [self.screen.blit(pawn.image, (pawn.x, pawn.y)) for pawn in self.judge.group]

                # Blit all outlines on screen
                if (self.outlines != []):
                    [out.update() for out in self.outlines]
                    [self.screen.blit(out.image, out.position) for out in self.outlines]

                # Draw UI elements on the screen
                self.ui.manager.draw_ui(self.screen)

                # Update the game display
                pygame.display.flip()
        except:
            print( self.achievements['0x42'] )

game = Game()
game.run()
