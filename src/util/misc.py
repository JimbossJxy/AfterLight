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


class misc:
    def __init__(self):
        # Boilerplate code - Excluding misc class because it is the misc class
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logger = logging.getLogger(__name__)

        # Other Objects - These are objects that are used by the class

    def warningPopup(self, title, message):
        # Constants for the warning MessageBox
        _MessageboxOK = 0x0
        _MessageboxIconWarning = 0x30
        ctypes.windll.user32.MessageBoxW(0, message, title, _MessageboxOK | _MessageboxIconWarning)
        self.logger.info("Displayed warning popup successfully.")
    
    def errorPopup(self, message):
        # Constrains for Error message box
        _MessageboxOK = 0x0
        _MessageboxIconError = 0x10
        ctypes.windll.user32.MessageBoxW(0, message, "Error", _MessageboxOK | _MessageboxIconError)
        self.logger.error("Displayed error popup successfully.")
    
    def yesNoPopup(self, title, message):
        # Constants for the YesNo MessageBox
        _MessageboxYesNo = 0x4
        _MessageboxIconQuestion = 0x20
        return ctypes.windll.user32.MessageBoxW(0, message, title, _MessageboxYesNo | _MessageboxIconQuestion)

