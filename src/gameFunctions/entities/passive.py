"""
Author Block
Author: James Collum
Date Creation: 16/05/2024
Document Name: passive.py
Purpose of Document: This document will be used to handle passive entities in the game.
Referenced Code:



"""

import configparser
import os
import pathlib
import pickle
import subprocess
import shutil
import zipfile
from datetime import datetime
from pathlib import Path
from src.util.misc import misc
from src.util.afterlightLogging import afterlightLogging

class passiveAI:
    def __init__(self):
        # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logger = afterlightLogging()

        # Other Objects - These are objects that are used by the class