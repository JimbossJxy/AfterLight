"""
Author Block
Author: James Collum
Date Creation: 18/05/2024
Document Name: gamerunner.py
Purpose of Document: The purpose of this document is to handle the running of the game.
Referenced Code:


"""

import configparser
import logging
import os
import pygame
import pathlib
import subprocess
from pathlib import Path
from src.util.misc import misc
from src.util.settings import Settings

def startup():
    logger = logging.getLogger(__name__)
    pygame.init()
    logger.info("Pygame has been initialized")

    # Check resolution from settings dictionary in variables.py
    resulution = Settings().getSetting("displaySettings.resolution")
    logger.info(f"Resolution: {resulution}")

    # Check if the game is in fullscreen mode
    fullscreen = Settings().getSetting("displaySettings.fullscreen")
    logger.info(f"Fullscreen: {fullscreen}")


    if fullscreen:
        screen = pygame.display.set_mode(resulution, pygame.FULLSCREEN)
        logger.info("Game is in fullscreen mode")
        logger.info("Game resolution is set to: " + str(resulution))
    else:
        screen = pygame.display.set_mode(resulution)
        logger.info("Game is not in fullscreen mode")
        logger.info("Game resolution is set to: " + str(resulution))
    
    clock = pygame.time.Clock()
    logger.info("Clock has been created")


    # Set the title of the window
    pygame.display.set_caption("Afterlight")
    logger.info("Game title is set to: Afterlight")
    
    return screen, clock
    

