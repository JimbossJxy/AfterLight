"""
Author Block
Author: James Collum
Date Creation: 16/05/2024
Document Name: saving.py
Purpose of Document: This document will be used to save the game data to a file so that the user can load the game from where they left off.
Referenced Code:



"""
import configparser
import logging
import os
import pathlib
import pickle
import subprocess
import shutil
import zipfile
from datetime import datetime
from pathlib import Path
from logging.handlers import RotatingFileHandler
from src.util.misc import misc


class saveLoadGame:
    def __init__(self):
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
        self.config = configparser.ConfigParser()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = RotatingFileHandler(str(Path.home() / "Documents" / "Afterlight" / "Logs" / "save.log"), maxBytes=100000, backupCount=5)
        self.logger.addHandler(self.handler)
    
    def saveGame(self, gameData, saveName):
        """
        Saves the game data to a .dat file
        """
        try:
            with open(self.savePath + "\\" + saveName + ".dat", "wb") as file:
                pickle.dump(gameData, file)
                self.logger.info(f"Game saved as {saveName}")
                print(f"Game saved as {saveName}")
        except Exception as e:
            self.logger.error(f"Error saving game: {e}")
            print(f"Error saving game: {e}")
        
    def loadGame(self, saveName):
        """
        Loads the game data from a .dat file
        """
        try:
            """
            Reads the .dat file and loads the game data
            """
            with open(self.savePath + "\\" + saveName + ".dat", "rb") as file:
                gameData = pickle.load(file)
                self.logger.info(f"Game loaded from {saveName}")
                print(f"Game loaded from {saveName}")
                return gameData
            
        except Exception as e:
            """
            If the file does not exist display error and return None
            """
            self.logger.error(f"Error loading game: {e}")
            print(f"Error loading game: {e}")
            return None


"""
Searches for files within directories
"""
class search:
    def __init__(self):
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
        self.gameConfigPath = str(Path.home() / "Documents" / "Afterlight" / "GameConfig")
        self.config = configparser.ConfigParser()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = RotatingFileHandler(str(Path.home() / "Documents" / "Afterlight" / "Logs" / "save.log"), maxBytes=100000, backupCount=5)
        self.logger.addHandler(self.handler)
    
    def listSaveGames(self):
        """
        Lists the save games in the save directory
        """
        try:
            saveFiles = [file for file in os.listdir(self.savePath) if file.endswith(".dat")]
            self.logger.info(f"Searching for save games")
            print(f"Searching for save games")
            if saveFiles:
                logging.info(f"Current save games:")
                print(f"Current save games:")
                for saveFile in saveFiles:
                    logging.info(f"{saveFile}")
                    print(f"{saveFile}")
                return saveFiles
            
            else:
                logging.info(f"No save games found")
                print(f"No save games found")
                return 0
        
        except Exception as e:
            logging.error(f"Error listing save games: {e}")
            print(f"Error listing save games: {e}")
            return 0
    
    def listGameConfig(self):
        """
        Lists the corresponding game config files in the save directory
        """
        try:
            configFiles = [file for file in os.listdir(self.gameConfigPath) if file.endswith(".cfg")]
            self.logger.info(f"Searching for game config files")
            print(f"Searching for game config files")
            if configFiles:
                logging.info(f"Current game config files:")
                print(f"Current game config files:")
                for configFile in configFiles:
                    logging.info(f"{configFile}")
                    print(f"{configFile}")
                return configFiles
            
            else:
                logging.info(f"No game config files found")
                print(f"No game config files found")
                return 0
        
        except Exception as e:
            logging.error(f"Error listing game config files: {e}")
            print(f"Error listing game config files: {e}")
            return 0
    

"""
Deletes files within directories
"""
class delete:
    def __init__(self):
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
        self.gameConfigPath = str(Path.home() / "Documents" / "Afterlight" / "GameConfig")
        self.logPath = str(Path.home() / "Documents" / "Afterlight" / "Logs")
        self.config = configparser.ConfigParser()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = RotatingFileHandler(str(Path.home() / "Documents" / "Afterlight" / "Logs" / "save.log"), maxBytes=100000, backupCount=5)
        self.logger.addHandler(self.handler)
        self.errorPop = misc().errorPopup
    
    def deleteSaveGame(self, saveName):
        """
        Deletes the save game file
        """
        try:
            os.remove(self.savePath + "\\" + saveName + ".dat")
            self.logger.info(f"Deleted save game {saveName}")
            print(f"Deleted save game {saveName}")
        
        except Exception as e:
            self.logger.error(f"Error deleting save game: {e}")
            print(f"Error deleting save game: {e}")
    
    def deleteGameConfig(self, configName):
        """
        Deletes the game config file
        """
        try:
            os.remove(self.gameConfigPath + "\\" + configName + ".cfg")
            self.logger.info(f"Deleted game config {configName}")
            print(f"Deleted game config {configName}")
        
        except Exception as e:
            self.logger.error(f"Error deleting game config: {e}")
            print(f"Error deleting game config: {e}")
        
    def deleteLog(self):
        """
        Deletes the log files in the game directory
        """
        try:
            os.remove(os.path.join(self.logPath, "save.log"))
            self.logger.info(f"Deleted log file")
            print(f"Deleted log file")
        
        except Exception as e:
            self.logger.error(f"Error deleting log file: {e}")
            print(f"Error deleting log file: {e}")
            self.errorPop(f"Error deleting log file: {e}")





        


