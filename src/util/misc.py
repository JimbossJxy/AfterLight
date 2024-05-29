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
import ctypes
import logging
import os
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
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = RotatingFileHandler(str(Path.home() / "Documents" / "Afterlight" / "Logs" / "save.log"), maxBytes=100000, backupCount=5)
        self.logger.addHandler(self.handler)
        self.logger.info("Logger created")
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")

    def warningPopup(self, title, message):
        # Constants for the warning MessageBox
        _MessageboxOK = 0x0
        _MessageboxIconWarning = 0x30
        ctypes.windll.user32.MessageBoxW(0, message, title, _MessageboxOK | _MessageboxIconWarning)
    
    def errorPopup(self, message):
        # Constrains for Error message box
        _MessageboxOK = 0x0
        _MessageboxIconError = 0x10
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        ctypes.windll.user32.MessageBoxW(0, message, "Error", _MessageboxOK | _MessageboxIconError)

