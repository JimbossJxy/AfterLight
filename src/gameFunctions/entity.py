"""
Author Block
Author: James Collum
Date Creation: 08/06/2024
Document Name: entity.py
Purpose of Document: This document will be used to handle player logic in the game.
Referenced Code:



"""

# Add's project root to path
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import configparser
import logging
import pathlib
import pickle
import pygame
import subprocess
import shutil
import zipfile
from datetime import datetime
from pathlib import Path
from src.util.misc import misc
from src.gameFunctions.physics import physics

class entity:
    def __init__(self):
        # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logger = logging.getLogger(__name__)

        # Other Objects - These are objects that are used by the class


    def entity(self, imagePath, position):
        """
        This function will create an entity object
        """
        self.originalImage = pygame.image.load(imagePath).convert_alpha()
        self.image = self.originalImage
        self.rect = self.image.get_rect(topleft=position)
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = "right" #The direction the player is facing