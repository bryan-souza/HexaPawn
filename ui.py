"""
HexaPawn ui module

Stores UI (User Interface) manager and UI objects
"""

import pygame
import os
from pygame_gui import UIManager
from pygame_gui.elements import UIPanel, UILabel, UIButton, UIHorizontalSlider, UISelectionList, UIImage

class UI():
    def __init__(self, screen_width, screen_height):
        """
        Initialize UI elements
        """
        # UI manager
        self.manager = UIManager((screen_width, screen_height))

        # Side panel
        self.cfg_panel = UIPanel(pygame.Rect(645, 0, 395, 640), 0, manager=self.manager)
        self.lbl_cfg_panel = UILabel(
            relative_rect=pygame.Rect(650, 10, 100, 20),
            parent_element=self.cfg_panel,
            manager=self.manager,
            text="Settings"
        )

        # Game control mode
        self.lbl_ctrl_mode = UILabel(
            relative_rect=pygame.Rect(800, 40, 100, 25),
            parent_element=self.cfg_panel,
            manager=self.manager,
            text="Playmode"
        )

        self.sldr_playmode = UIHorizontalSlider(
            relative_rect=pygame.Rect(800, 60, 100, 25),
            parent_element=self.cfg_panel,
            start_value=0,
            value_range=(0, 1),
            manager=self.manager
        )

        self.lbl_manual_ctrl = UILabel(
            relative_rect=pygame.Rect(700, 60, 100, 25),
            parent_element=self.cfg_panel,
            manager=self.manager,
            text="Manual"
        )

        self.lbl_auto_ctrl = UILabel(
            relative_rect=pygame.Rect(900, 60, 100, 25),
            parent_element=self.cfg_panel,
            manager=self.manager,
            text="Auto"
        )

        # AI mode picker
        self.lbl_mode_picker = UILabel(
            relative_rect = pygame.Rect(800, 100, 100, 25),
            parent_element = self.cfg_panel,
            manager=self.manager,
            text="AI Mode" 
        )

        self.lst_ai_modes = UISelectionList(
            relative_rect=pygame.Rect(800, 120, 100, 66),
            parent_element=self.cfg_panel,
            manager=self.manager,
            item_list=[
                "Exclusive",
                "Inclusive",
                "Both"
            ]
        )

        # Apply settings
        self.btn_apply = UIButton(
            relative_rect=pygame.Rect(-110, -50, 100, 40),
            parent_element=self.cfg_panel,
            manager=self.manager,
            anchors={
                'left': 'right',
                'right': 'right',
                'top': 'bottom',
                'bottom': 'bottom'
            },
            text="Save"
        )

        self.img_paused = UIImage(
            relative_rect = pygame.Rect(-380, -50, 32, 32),
            parent_element=self.cfg_panel,
            manager=self.manager,
            anchors={
                'left': 'right',
                'right': 'right',
                'top': 'bottom',
                'bottom': 'bottom'
            },
            visible=False,
            image_surface = pygame.image.load( os.path.join('sprites', 'pauseButton.png') ).convert_alpha()
    )
