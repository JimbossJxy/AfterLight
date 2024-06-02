"""
Author Block
Author: James Collum
Date Creation: 02/06/2024
Document Name: logging.py
Purpose of Document: This document will be used to handle logging for the game.
Referenced Code:
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler


class afterlightLogging:
    def __init__(self):

        # Paths
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logPath = str(Path.home() / "Documents" / "Afterlight" / "Logs")
        
        # Logging setup
        self.handler = RotatingFileHandler(self.logPath + "/game.log", maxBytes=5242880, backupCount=5)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(self.handler)
        self.logger.addHandler(logging.StreamHandler())
        self.logger.info("Logging has been setup for this session.")

    def info(self, message):
        self.logger.info(message)
    
    def error(self, message):
        self.logger.error(message)
    
    def warning(self, message):
        self.logger.warning(message)
    
    def debug(self, message):
        self.logger.debug(message)
    
    def critical(self, message):
        self.logger.critical(message)
    
    def exception(self, message):
        self.logger.exception(message)
    
    
    
    
