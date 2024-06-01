"""
Author Block
Author: James Collum
Date Creation: 01/06/2024
Document Name: statistics.py
Purpose of Document: This document will be used to generate statistics and modify for the game.
References: None
"""

import configparser
import logging
import util
import os
import pathlib
import sys
import shutil
from util.misc import misc
from pathlib import Path
from tempfile import TemporaryDirectory, mkdtemp
from logging.handlers import RotatingFileHandler

class statistics:
    def __init__(self):
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
        self.statsPath = str(Path.home() / "Documents" / "Afterlight" / "Statistics")
        self.config = configparser.ConfigParser()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = RotatingFileHandler(str(Path.home() / "Documents" / "Afterlight" / "Logs" / "game.log"), maxBytes=100000, backupCount=5)
        self.logger.addHandler(self.handler)
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup