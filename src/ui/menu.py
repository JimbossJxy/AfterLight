"""
Author Block
Author: James Collum
Date Creation: 29/05/2024
Document Name: menu.py
Purpose of Document: This document will be used to handle any menu logic and rendering in the game.


"""
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


class menu:
    def __init__(self):
       # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.assestsPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "afterlightAssets-main")
        self.logger = logging.getLogger(__name__)

        # Other Objects - These are objects that are used by the class

        # menu specific objects

        self.menuItems = ["Resume Game", "New Game", "Load Game", "Statistics", "Settings", "Exit Game"]

    def loadingScreen(self):
        """
        This function will render the loading screen of the game
        """
        pass

    def mainMenu(self):
        """
        This function will render the main menu of the game
        """
        pass
    
    def newGameMenu(self):
        """
        This function will render the new game menu of the game
        """
        pass

    def loadGameMenu(self):
        """
        This function will render the load game menu of the game
        """
        pass

    def settingsMenu(self):
        """
        This function will render the settings menu of the game
        """
        pass

    def statisticsMenu(self):
        """
        This function will render the statistics menu of the game
        """
        pass

    def popupMenu(self):
        """
        This function will render the popup menu of the game. It will overlay the in game screen.
        """
        pass
    