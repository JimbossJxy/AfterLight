"""
Author Block
Author: James Collum
Date Creation: 2/06/2024
Document Name: player.py
Purpose of Document: This document will be used to handle world generation and logic in the game.
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
from src.util.misc import misc
from src.util.afterlightLogging import afterlightLogging

class world:
    def __init__(self):
        # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logger = logging.getLogger(__name__)

        # Other Objects - These are objects that are used by the class
        
