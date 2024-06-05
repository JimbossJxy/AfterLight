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
from src.util.gamerunner import startup


class menu:
    def __init__(self):
       # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.assestsPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "afterlightAssets-main")
        self.menuPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "afterlightAssets-main" / "Menus")
        self.logger = logging.getLogger(__name__)

        # Other Objects - These are objects that are used by the class

        # menu specific objects

        self.menuItems = ["Resume Game", "New Game", "Load Game", "Statistics", "Settings", "Exit Game"]

    def loadingScreen(self, screen):
        """
        This function will render the loading screen of the game
        """
        pass

    def mainMenu(self, screen):
        """
        This function will render the main menu of the game
        """
        _background =  pygame.image.load(str(self.menuPath /"MainMenu" / "background.png"))
        pygame.display.set_caption("Afterlight - Main Menu")
        self.logger.info("Rendering Main Menu")
        
        while True:
            screen.blit(_background, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_RETURN:
                        pass
                    if event.key == pygame.K_DOWN:
                        pass
                    if event.key == pygame.K_UP:
                        pass  
    
    
    def newGameMenu(self, screen):
        """
        This function will render the new game menu of the game
        """
        pass

    def loadGameMenu(self, screen):
        """
        This function will render the load game menu of the game
        """
        pass

    def settingsMenu(self, screen):
        """
        This function will render the settings menu of the game
        """
        pass

    def statisticsMenu(self, screen):
        """
        This function will render the statistics menu of the game
        """
        pass

    def popupMenu(self, screen):
        """
        This function will render the popup menu of the game. It will overlay the in game screen.
        """
        pass
    