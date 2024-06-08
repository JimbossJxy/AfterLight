"""
Author Block
Author: James Collum
Date Creation: 16/05/2024
Document Name: main.py
Purpose of Document: Acting as the main file to run the majority of the code from
Referenced Code:


"""


from src.ui import menu

import src.util.gamerunner 
import src.util.initialise as initialise
from src.util.misc import misc





import configparser
import logging
import os
import pathlib
import subprocess
from pathlib import Path

# DO NOT MOVE THIS IMPORT TO THE TOP OF THE FILE
initialise.run() # This is used to initialise the game - Also makes sure that the game is installed correctly
import pygame
import sys

# These imports use libraries that are not built in
from src.util.settings import Settings
from src.gameFunctions import world
from src.ui.menu import menu
    
class game:
    def __init__(self):
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logger = logging.getLogger(__name__)
        self.framerate = int(Settings().getSetting("displaySettings.refreshRate"))

        
        self.screen, self.clock = src.util.gamerunner.startup()

        self.running = True

    
    def run(self):
        while self.running:
            self.update()
            self.draw()
        self.close()
    
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            pygame.display.update()
            self.clock.tick(self.framerate)

    def draw(self):
        self.screen.fill("lightblue")
    
    def close(self):
        pygame.quit()
        self.logger.info("Game has been closed")
        sys.exit()


if __name__ == "__main__":
    game = game()
    game.run()