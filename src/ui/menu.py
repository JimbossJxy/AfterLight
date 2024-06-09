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
    
    assestsPath = str(Path.home() / "Documents" / "Afterlight" / "Assets")

    RESUME_GAME = pygame.image.load(assestsPath + "/Menus/mainMenu/Images/ResumeGame.png").convert_alpha()
    NEW_GAME = pygame.image.load(assestsPath + "/Menus/mainMenu/Images/NewGame.png").convert_alpha()
    LOAD_GAME = pygame.image.load(assestsPath + "/Menus/mainMenu/Images/LoadGame.png").convert_alpha()
    STATISTICS = pygame.image.load(assestsPath + "/Menus/mainMenu/Images/Statistics.png").convert_alpha()
    SETTINGS = pygame.image.load(assestsPath + "/Menus/mainMenu/Images/Settings.png").convert_alpha()
    EXIT_GAME = pygame.image.load(assestsPath + "/Menus/mainMenu/Images/ExitGame.png").convert_alpha()

    BACKGROUND = pygame.image.load(assestsPath + "/Menus/mainMenu/Images/Background.png")
    

class fonts:
    MAINMENU = pygame.font.Font(str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Menus" / "Fonts" / "mainMenu.ttf"), 50)
    MAINFONT = pygame.font.Font(str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Menus" / "Fonts" / "mainFont.ttf"), 50)

    # Font sizes - Menu
    MED_MAINFONT = pygame.font.Font(str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Menus" / "Fonts" / "mainFont.ttf"), 40)
    SMALL_MAINFONT = pygame.font.Font(str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Menus" / "Fonts" / "mainFont.ttf"), 30)


# https://github.com/russs123/pygame_tutorials/blob/main/Menu/button.py
# Define the Button class
class Button:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        # Draw button on the screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

class MainMenu:
    def __init__(self, screen):

        SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
        pygame.display.set_caption("Afterlight - Main Menu")

        self.background = menuImages.BACKGROUND

        # Create buttons
        self.buttons = {
            "resumeGame": Button(menuImages.RESUME_GAME, 810, 300),
            "newGame": Button(menuImages.NEW_GAME, 810, 450),
            "loadGame": Button(menuImages.LOAD_GAME, 810, 600),
            "statistics": Button(menuImages.STATISTICS, 810, 750),
            "settings": Button(menuImages.SETTINGS, 810, 900),
            "exitGame": Button(menuImages.EXIT_GAME, 810, 1050),
        }

        self.titleFont = fonts.MAINMENU
        self.titleSurface = self.titleFont.render("Afterlight", True, (255, 255, 255))
        self.titleRect = self.titleSurface.get_rect(center=(SCREEN_WIDTH // 2, 150))

    def run(self):
        running = True
        while running:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.titleSurface, self.titleRect)

            for button in self.buttons.values():
                if button.draw(self.screen):
                    print(f"{button} button clicked")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

        pygame.quit()






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
        self.menuState = "mainMenu"
        self.gamePaused = False
        self.screenWidth, self.screenHeight = pygame.display.get_surface().get_size()

    def draw_text(self, screen, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))


    def loadingScreen(self, screen):
        """
        This function will render the loading screen of the game
        """
        pass

    def mainMenu(self, screen):
        """
        This function will render the main menu of the game
        """
        # create buttons
        running = True
        titleFont = fonts.MAINMENU
        titleText = "Afterlight - Main Menu"
        titleX = (self.screenWidth - titleFont.size(titleText)[0]) // 2
        titleY = self.screenHeight // 4
        self.draw_text(screen, titleText, titleFont, (255, 255, 255), titleX, titleY)

        buttonScale = 0.5
        buttonX = (self.screenWidth - menuImages.RESUME_GAME.get_width() * buttonScale) // 2
        buttonY = titleY + titleFont.size(titleText)[1] + 50

        resumeButton = Button(buttonX, buttonY, menuImages.RESUME_GAME, buttonScale)
        newGameButton = Button(buttonX, buttonY + 100, menuImages.NEW_GAME, buttonScale)
        loadGameButton = Button(buttonX, buttonY + 200, menuImages.LOAD_GAME, buttonScale)
        statisticsButton = Button(buttonX, buttonY + 300, menuImages.STATISTICS, buttonScale)
        settingsButton = Button(buttonX, buttonY + 400, menuImages.SETTINGS, buttonScale)
        exitButton = Button(buttonX, buttonY + 500, menuImages.EXIT_GAME, buttonScale)

        while running:
            screen.blit(menuImages.BACKGROUND, (0, 0))

            if resumeButton.draw(screen):
                self.logger.info("Resume Game Button Clicked")
            if newGameButton.draw(screen):
                self.logger.info("New Game Button Clicked")
            if loadGameButton.draw(screen):
                self.logger.info("Load Game Button Clicked")
            if statisticsButton.draw(screen):
                self.logger.info("Statistics Button Clicked")
            if settingsButton.draw(screen):
                self.logger.info("Settings Button Clicked")
            if exitButton.draw(screen):
                self.logger.info("Exit Game Button Clicked")
                pygame.quit()
                self.logger.info("Game has been closed")
                sys.exit()




    
    
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
    
    def tutorialOverlay(self, screen):
        """
        This function will render the tutorial overlay of the game. It will overlay the in game screen.
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


        
        
    
    