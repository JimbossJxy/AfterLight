"""
Author Block
Author: James Collum
Date Creation: 29/05/2024
Document Name: hud.py
Purpose of Document: This document will be used to handle any HUD rendering and communication from the HUD to the game.
Referenced Code:



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

class hud:
    def __init__(self):
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
        # hud specific code
