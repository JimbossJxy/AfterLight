"""
Author Block
Author: James Collum
Date Creation: 29/05/2024
Document Name: world.py
Purpose of Document: This document will be used to handle terrain generation, world logic, world data, chunk loading and unloading, and world saving and loading
Referenced Code:



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


class world:
    def __init__(self):
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
        self.config = configparser.ConfigParser()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = RotatingFileHandler(str(Path.home() / "Documents" / "Afterlight" / "Logs" / "save.log"), maxBytes=100000, backupCount=5)
        self.logger.addHandler(self.handler)
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
    