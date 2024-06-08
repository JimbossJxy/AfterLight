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
from src.ui.button import Button


class menu:
    def __init__(self):
       # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.assestsPath = str(Path.home() / "Documents" / "Afterlight" / "Assets")
        
        self.logger = logging.getLogger(__name__)

        # Other Objects - These are objects that are used by the class

        # menu specific objects
        self.menuPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Menus")
        self.fontPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Menus"/ "Fonts")
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
        try:
            _background =  pygame.image.load(str(os.path.join(self.menuPath,"MainMenu","Background.png")))
            self.logger.info("Main Menu Background Loaded")
        except FileNotFoundError as e:
            self.logger.error("Main Menu Background Not Found")
            self.errorPopup("Main Menu Background Not Found")
            return
        
        
        pygame.display.set_caption("Afterlight - Main Menu")
        self.logger.info("Rendering Main Menu")
        
        while True:
            screenWidth, screenHeight = screen.get_size()
            screen.blit(_background, (0, 0))
            pygame.display.update()
            mousePos = self.mousePos
            
            # Main Menu Text
            
            fontSize = int(100 * (screenWidth / 1920))
            _mainMenuFont = (self.fontPath + "/" + "mainmenu.ttf")
            menuText = pygame.font.Font(_mainMenuFont, fontSize).render("Afterlight", True, (255, 255, 255))

            
            menuTextRect = menuText.get_rect(centre=(screen.get_width() / 2, 100))

            # Main Menu Buttons
            resumeGameButton = Button(None, (screenWidth / 2, screenHeight / 2), "Resume Game", pygame.font.Font(_mainMenuFont, int(50 * (screenWidth / 1920))), (255, 255, 255), (255, 255, 255))
            newGameButton = Button(None, (screenWidth / 2, screenHeight / 2 + 50), "New Game", pygame.font.Font(_mainMenuFont, int(50 * (screenWidth / 1920))), (255, 255, 255), (255, 255, 255))
            loadGameButton = Button(None, (screenWidth / 2, screenHeight / 2 + 100), "Load Game", pygame.font.Font(_mainMenuFont, int(50 * (screenWidth / 1920))), (255, 255, 255), (255, 255, 255))
            statisticsButton = Button(None, (screenWidth / 2, screenHeight / 2 + 150), "Statistics", pygame.font.Font(_mainMenuFont, int(50 * (screenWidth / 1920))), (255, 255, 255), (255, 255, 255))
            settingsButton = Button(None, (screenWidth / 2, screenHeight / 2 + 200), "Settings", pygame.font.Font(_mainMenuFont, int(50 * (screenWidth / 1920))), (255, 255, 255), (255, 255, 255))
            exitGameButton = Button(None, (screenWidth / 2, screenHeight / 2 + 250), "Exit Game", pygame.font.Font(_mainMenuFont, int(50 * (screenWidth / 1920))), (255, 255, 255), (255, 255, 255))

            # Update Buttons
            for button in (resumeGameButton, newGameButton, loadGameButton, statisticsButton, settingsButton, exitGameButton):
                button.changeColour(mousePos)
                button.update(screen)

            # Update Text
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resumeGameButton.checkForInput(mousePos):
                        self.logger.info("Resume Game Button Clicked")
                        return
                    elif newGameButton.checkForInput(mousePos):
                        self.logger.info("New Game Button Clicked")
                        return
                    elif loadGameButton.checkForInput(mousePos):
                        self.logger.info("Load Game Button Clicked")
                        return
                    elif statisticsButton.checkForInput(mousePos):
                        self.logger.info("Statistics Button Clicked")
                        return
                    elif settingsButton.checkForInput(mousePos):
                        self.logger.info("Settings Button Clicked")
                        return
                    elif exitGameButton.checkForInput(mousePos):
                        self.logger.info("Exit Game Button Clicked")
                        self.logger.info("Game has been closed")
                        pygame.quit()
                        sys.exit()
            
            pygame.display.update()


    
    
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
        while True:
            screenWidth, screenHeight = screen.get_size()
            

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


class inGameRenderEngine:
    def __init__(self):
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.assestsPath = str(Path.home() / "Documents" / "Afterlight" / "Assets")
        
        self.logger = logging.getLogger(__name__)
    
    