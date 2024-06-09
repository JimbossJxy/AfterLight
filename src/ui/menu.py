"""
Author Block
Author: James Collum
Date Creation: 29/05/2024
Document Name: menu.py
Purpose of Document: This document will be used to handle any menu logic and rendering in the game.


"""
import os
import src
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
from src.gameFunctions.player import player


class menuImages:
    logger = logging.getLogger(__name__)
    assestsPath = str(Path.home() / "Documents" / "Afterlight" / "Assets")

    RESUME_GAME = pygame.image.load(assestsPath + "/Menus/mainMenu/Images/ResumeGame.png")
    NEW_GAME = pygame.image.load(assestsPath + "/Menus/mainMenu/Images/NewGame.png")
    LOAD_GAME = pygame.image.load(assestsPath + "/Menus/mainMenu/Images/LoadGame.png")
    STATISTICS = pygame.image.load(assestsPath + "/Menus/mainMenu/Images/Statistics.png")
    SETTINGS = pygame.image.load(assestsPath + "/Menus/mainMenu/Images/Settings.png")
    EXIT_GAME = pygame.image.load(assestsPath + "/Menus/mainMenu/Images/ExitGame.png")
    



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



class hotbar:
    def __init__(self,  screen, slotCount=7, slotSize=64, padding=10, margin=20):
        self.screen = screen
        self.slotCount = slotCount
        self.slotSize = slotSize
        self.padding = padding
        self.margin = margin
        self.slots = []
        self.selectedSlot = 0

        self.logger = logging.getLogger(__name__)

        self.screenWidth, self.screenHeight = self.screen.get_size()
        self.hotbarWidth = slotCount * (slotSize + padding) - padding
        self.hotbarRect = pygame.Rect((self.screenWidth - self.hotbarWidth) // 2, self.screenHeight - slotSize - margin, self.hotbarWidth, slotSize)

        for i in range(slotCount):
            x = self.hotbarRect.x + i * (slotSize + padding)
            y = self.hotbarRect.y
            rect = pygame.Rect(x, y, slotSize, slotSize)
            self.slots.append(rect)
    
    def draw(self):
        for i, slot in enumerate(self.slots):
            colour = (255, 255, 255) if i != self.selectedSlot else (128, 128, 128)
            pygame.draw.rect(self.screen, colour, slot, 2)

            # Draw the item in the slot
            # This is a placeholder
            #itemImage = pygame.image.load("path/to/item.png").convert_alpha()
            #itemImage = pygame.transform.scale(itemImage, (self.slotSize, self.slotSize))
            #self.screen.blit(itemImage, slot.topleft)
        
    def selectSlot(self, slot):
        if 0 <= slot < self.slotCount:
            self.selectedSlot = slot
        
       
class inGameRenderEngine:
    def __init__(self, screen, frameRate=60):
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.assestsPath = str(Path.home() / "Documents" / "Afterlight" / "Assets")
        
        self.logger = logging.getLogger(__name__)

        self.screen = screen
        self.clock = pygame.time.Clock() # This is the clock object
        self.frameRate = frameRate # This is the frame rate of the game
        self.hotbar = hotbar(screen) # This is the hotbar object

        self.screenWidth, self.screenHeight = self.screen.get_size() # Gets the screen size for x and y
        self.tileSize = 38 # This is in px

        # Player position
        self.playerCentreX, self.playerCentreY = self.player.rect.center

        self.logger.info("In Game Render Engine Initialised")
        
    

    def run(self):
        running = True
        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.hotbar.selectSlot(0)
                    elif event.key == pygame.K_2:
                        self.hotbar.selectSlot(1)
                    elif event.key == pygame.K_3:
                        self.hotbar.selectSlot(2)
                    elif event.key == pygame.K_4:
                        self.hotbar.selectSlot(3)
                    elif event.key == pygame.K_5:
                        self.hotbar.selectSlot(4)
                    elif event.key == pygame.K_6:
                        self.hotbar.selectSlot(5)
                    elif event.key == pygame.K_7:
                        self.hotbar.selectSlot(6)
                    elif event.key == pygame.K_ESCAPE:
                        running = False
            
            self.screen.fill((0, 0, 0))
            self.hotbar.draw()
            pygame.display.flip()
            self.clock.tick(self.frameRate)
        
        pygame.quit()
        self.logger.info("Game has been closed")
        sys.exit()

    def drawWorld(self):
        """
        This function will render the world of the game
        """
        startCol = (self.playerCentreX - self.screenWidth // 2) // self.tileSize
        startRow = (self.playerCentreY - self.screenHeight // 2) // self.tileSize


        
        
    
    