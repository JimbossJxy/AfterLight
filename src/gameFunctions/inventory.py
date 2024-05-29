"""
Author Block
Author: James Collum
Date Creation: 28/05/2024
Document Name: inventory.py
Purpose of Document: This document will be used to handle the players inventory in the game.
Referenced Code:



"""

import configparser
import logging
import util
import os
import pathlib
import pickle
import sys
import shutil
from src import variables
from util.misc import misc
from pathlib import Path
from tempfile import TemporaryDirectory, mkdtemp
from logging.handlers import RotatingFileHandler

class inventory:
    def __init__(self):
        self.inventory = {}
        self.config = configparser.ConfigParser()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = RotatingFileHandler(str(Path.home() / "Documents" / "Afterlight" / "Logs" / "inventory.log"), maxBytes=100000, backupCount=5)
        self.logger.addHandler(self.handler)
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
    
    def loadInventory(self):
        """
        Loads the players inventory from a load game variable to the inventory variable

        Only to be run on game load not new game or save game
        """
        if 'inventory' in variables.loadGame:
            self.inventory = variables.loadGame['inventory']
            _row = 0
            _position = 0
            

        else:
            self.warningPopup("No inventory data available")
            self.logger.warning("No inventory data available")




        if 'loadGame' in self.inventory:
            load_game_inventory = self.inventory['loadGame']
            if all(row in load_game_inventory for row in range(5)):
                for row in range(5):
                    if all(position in load_game_inventory[row] for position in range(5)):
                        for position in range(5):
                            self.inventory[row][position] = load_game_inventory[row][position]
                    else:
                        self.warningPopup("Invalid position in loadGame inventory")
                        self.logger.warning("Invalid position in loadGame inventory")
            else:
                self.warningPopup("Invalid row in loadGame inventory")
                self.logger.warning("Invalid row in loadGame inventory")
        else:
            self.warningPopup("No loadGame inventory data available")
            self.logger.warning("No loadGame inventory data available")


        