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
        Loads the players inventory from a .dat file
        """
        