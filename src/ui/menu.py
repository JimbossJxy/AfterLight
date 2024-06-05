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
        self.assestsPath = str(Path.home() / "Documents" / "Afterlight" / "Assets")
        self.menuPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Menus")
        self.fontPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Menus"/ "Fonts")
        self.logger = logging.getLogger(__name__)

        # Other Objects - These are objects that are used by the class

        # menu specific objects
        self.mousePos = pygame.mouse.get_pos()
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
            mousePos = self.mousePos

            screenWidth, screenHeight = screen.get_size()
            fontSize = int(100 * (screenWidth / 1920))
            menuText = pygame.font.Font(self.fontPath / "menuFont.ttf", fontSize).render("Afterlight", True, (255, 255, 255))

            menuTextRect = menuText.get_rect(centre=(screen.get_width() / 2, 100))

            



    
    
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
    