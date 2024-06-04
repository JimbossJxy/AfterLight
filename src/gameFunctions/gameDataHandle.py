"""
Author Block
Author: James Collum
Date Creation: 16/05/2024
Document Name: gameDataHandle.py
Purpose of Document: This document will be used to save the game data to a file so that the user can load the game from where they left off.
Referenced Code:



"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import configparser
import logging
import pickle
from datetime import datetime
from pathlib import Path
from src.util.misc import misc




class saveLoadGame:
    def __init__(self):
        # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopupup = self.misc.errorPopupup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logger = logging.getLogger(__name__)

        # Other Objects - These are objects that are used by the class

        self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
        self.statsPath = str(Path.home() / "Documents" / "Afterlight" / "Statistics")
        
    
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
        # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopupup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logger = afterlightLogging()

        # Other Objects - These are objects that are used by the class
        self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
        self.gameConfigPath = str(Path.home() / "Documents" / "Afterlight" / "GameConfig")
    
    def listSaveGames(self):
        """
        Lists the save games in the save directory
        """
        try:
            saveFiles = [file for file in os.listdir(self.savePath) if file.endswith(".dat")]
            self.logger.info(f"Searching for save games")
            print(f"Searching for save games")
            if saveFiles:
                self.logger.info(f"Current save games:")
                print(f"Current save games:")
                for saveFile in saveFiles:
                    self.logger.info(f"{saveFile}")
                    print(f"{saveFile}")
                return saveFiles
            
            else:
                self.logger.info(f"No save games found")
                print(f"No save games found")
                return 0
        
        except Exception as e:
            self.logger.error(f"Error listing save games: {e}")
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
                self.logger.info(f"Current game config files:")
                print(f"Current game config files:")
                for configFile in configFiles:
                    self.logger.info(f"{configFile}")
                    print(f"{configFile}")
                return configFiles
            
            else:
                self.logger.info(f"No game config files found")
                print(f"No game config files found")
                return 0
        
        except Exception as e:
            self.logger.error(f"Error listing game config files: {e}")
            print(f"Error listing game config files: {e}")
            return 0
    

"""
Deletes files within directories
"""
class delete:
    def __init__(self):
        # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logger = afterlightLogging()

        # Other Objects - These are objects that are used by the class
        self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
        self.gameConfigPath = str(Path.home() / "Documents" / "Afterlight" / "GameConfig")
        self.logPath = str(Path.home() / "Documents" / "Afterlight" / "Logs")
        self.statsPath = str(Path.home() / "Documents" / "Afterlight" / "Statistics")
    
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
            os.remove(os.path.join(self.logPath, "game.log"))
            self.logger.info(f"Deleted log file")
            print(f"Deleted log file")
        
        except Exception as e:
            self.logger.error(f"Error deleting log file: {e}")
            print(f"Error deleting log file: {e}")
            self.errorPopup(f"Error deleting log file: {e}")

    def deleteStatistics(self):
        """
        Deletes the statistics file in the game directory
        """
        # Checks all xml files in the statistics directory
        try:
            for file in os.listdir(self.statsPath):
                if file.endswith(".xml"):
                    os.remove(os.path.join(self.statsPath, file))
                    self.logger.info(f"Deleted statistics file")
                    
        
        except Exception as e:
            self.logger.error(f"Error deleting statistics file: {e}")
            self.errorPopup(f"Error deleting statistics file: {e}")
            





        


