"""
Author Block
Author: James Collum
Date Creation: 16/05/2024
Document Name: misc.py
Purpose of Document: This document will be used for miscellaneous functions that don't fit into any other category.
Referenced Code:



"""
"""
Imported Libraries - No need to install any libraries as they are all built in
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import ctypes
import logging
import pathlib
import subprocess
import shutil
import winsound
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory, mkdtemp
from logging.handlers import RotatingFileHandler

class misc:
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

    def warningPopup(self, title, message):
        # Constants for the warning MessageBox
        _MessageboxOK = 0x0
        _MessageboxIconWarning = 0x30
        ctypes.windll.user32.MessageBoxW(0, message, title, _MessageboxOK | _MessageboxIconWarning)
    
    def errorPopup(self, message):
        # Constrains for Error message box
        _MessageboxOK = 0x0
        _MessageboxIconError = 0x10
        ctypes.windll.user32.MessageBoxW(0, message, "Error", _MessageboxOK | _MessageboxIconError)

