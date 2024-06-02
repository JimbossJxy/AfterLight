"""
Author Block
Author: James Collum
Date Creation: 02/06/2024
Document Name: variables.py
Purpose of Document: This document will be used to processs physics for the game.

"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import configparser
import logging
import pathlib
import pickle
import subprocess
import shutil
import zipfile
from datetime import datetime
from pathlib import Path
from logging.handlers import RotatingFileHandler
from src.util.misc import misc

class physics:
    def __init__(self) :
        # Boilerplate code

        # Logging setup
        self.handler = RotatingFileHandler(self.logPath + "/game.log", maxBytes=5242880, backupCount=5)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handler)
        self.logger.addHandler(logging.StreamHandler())
        self.logger.info("Logging has been setup for the menu class.")

        # Other boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")

        # Other Objects - These are objects that are used by the class
    
    #class collisions:
