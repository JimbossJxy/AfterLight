"""
Author Block
Author: James Collum
Date Creation: 16/05/2024
Document Name: initialise.py
Purpose of Document: This file will contain most of the initalisation code and elements
Referenced Code:


"""

"""
    Importing the required libraries for the code to run
    Need to change to it checks if the required packages are installed and if not installs them
"""
import os
import src
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import configparser
import logging
import pathlib
import subprocess
import shutil
import webbrowser
import zipfile
import urllib.request
from pathlib import Path
from tempfile import TemporaryDirectory, mkdtemp

from src.variables import settings
from src.util.misc import misc
from src.util.afterlightLogging import afterlightLogging



class initalise:
    """
    Specifies the default paths for the game to use, also checks if the paths exist and if not creates them, also specifies the default settings for the game
    """
    def __init__(self, *args, **kwargs): 
            self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
            self.settingsPath = str(Path.home() / "Documents" / "Afterlight" / "Settings")
            self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
            self.backUpPath = str(Path.home() / "Documents" / "Afterlight" / "Backups")
            self.logPath = str(Path.home() / "Documents" / "Afterlight" / "Logs")
            self.tempPath = str(Path.home() / "Documents" / "Afterlight" / "Temp")
            self.assetPath = str(Path.home() / "Documents" / "Afterlight" / "Assets")
            self.statsPath = str(Path.home() / "Documents" / "Afterlight" / "Statistics")
            self.settingsFile = str(Path.home() / "Documents" / "Afterlight" / "Settings" / "settings.ini")

            self.warningPopup = misc().warningPopup
            self.errorPopup = misc().errorPopup
            self.logger = logging.getLogger(__name__)
            
            self.defaultSettings = settings

            self.githubAssets = "https://github.com/JimbossJxy/afterlightAssets/archive/refs/heads/main.zip"
            self.assetDict = {
                "audio": {
                    "mainPath": os.path.join(self.assetPath, "audio"),
                },
                "buildings": {
                    "mainPath": os.path.join(self.assetPath, "buildings"),
                },
                "hostileCreatures": {
                    "mainPath": os.path.join(self.assetPath, "hostileCreatures"),
                },
                "items": {
                    "mainPath": os.path.join(self.assetPath, "items"),
                },
                "player": {
                    "mainPath": os.path.join(self.assetPath, "player"),
                },
                "menus": {
                    "mainPath": os.path.join(self.assetPath, "menus"),
                    "mainMenu": {
                        "mainPath": os.path.join(self.assetPath, "menus", "mainMenu"),
                    },

                },
                "npcs": {
                    "mainPath": os.path.join(self.assetPath, "npcs"),
                },
                "passiveCreatures": {
                    "mainPath": os.path.join(self.assetPath, "passiveCreatures"),
                },
                "misc": {
                    "mainPath": os.path.join(self.assetPath, "misc"),
                },
            }


    
    def checkPaths(self):
        """
        Checks if the paths exist and if not creates them
        """
        if not os.path.exists(self.defaultPath):
            os.makedirs(self.defaultPath)
        if not os.path.exists(self.settingsPath):
            os.makedirs(self.settingsPath)
        if not os.path.exists(self.logPath):
            os.makedirs(self.logPath)
        if not os.path.exists(self.tempPath):
            os.makedirs(self.tempPath)
        if not os.path.exists(self.savePath):
            os.makedirs(self.savePath)
        if not os.path.exists(self.backUpPath):
            os.makedirs(self.backUpPath)
        if not os.path.exists(self.assetPath):
            os.makedirs(self.assetPath)
        if not os.path.exists(self.statsPath):
            os.makedirs(self.statsPath)
    

    def checkSettings(self):
        """
        Checks if the settings file exist and if not creates them
        """
        if not os.path.exists(self.settingsFile):
            
            config = configparser.ConfigParser()
            config['displaySettings'] = {
            'resolution': self.defaultSettings["displaySettings"]["resolution"],
            'fullscreen': self.defaultSettings["displaySettings"]["fullscreen"],
            'aspectRatio': self.defaultSettings["displaySettings"]["aspectRatio"],
            'vsync': self.defaultSettings["displaySettings"]["vsync"]
            }
            config['graphicsSettings'] = {
                'textureQuality': self.defaultSettings["graphicsSettings"]["textureQuality"],
                'shadows': self.defaultSettings["graphicsSettings"]["shadows"],
                'lighting': self.defaultSettings["graphicsSettings"]["lighting"],
                'particles': self.defaultSettings["graphicsSettings"]["particles"],
                'postProcessing': self.defaultSettings["graphicsSettings"]["postProcessing"],
                'antialiasing': self.defaultSettings["graphicsSettings"]["antialiasing"]
            }
            config['audioSettings'] = {
                'masterVolume': self.defaultSettings["audioSettings"]["masterVolume"],
                'musicVolume': self.defaultSettings["audioSettings"]["musicVolume"],
                'hostileVolume': self.defaultSettings["audioSettings"]["hostileVolume"],
                'friendlyVolume': self.defaultSettings["audioSettings"]["friendlyVolume"],
                'interactionVolume': self.defaultSettings["audioSettings"]["interactionVolume"],
                'environmentVolume': self.defaultSettings["audioSettings"]["environmentVolume"],
                'ambientVolume': self.defaultSettings["audioSettings"]["ambientVolume"]
            }
            config['keybinds'] = {
                'moveUp': self.defaultSettings["keybinds"]["moveUp"],
                'moveDown': self.defaultSettings["keybinds"]["moveDown"],
                'moveLeft': self.defaultSettings["keybinds"]["moveLeft"],
                'moveRight': self.defaultSettings["keybinds"]["moveRight"],
                'jump': self.defaultSettings["keybinds"]["jump"],
                'inventory': self.defaultSettings["keybinds"]["inventory"],
                'pause': self.defaultSettings["keybinds"]["pause"],
                'sprint': self.defaultSettings["keybinds"]["sprint"],
                'crouch': self.defaultSettings["keybinds"]["crouch"]
            }
            config['mouseSettings'] = {
                'sensitivity': self.defaultSettings["mouseSettings"]["sensitivity"],
                'inverted': self.defaultSettings["mouseSettings"]["inverted"],
                'attack': self.defaultSettings["mouseSettings"]["attack"],
                'interact': self.defaultSettings["mouseSettings"]["interact"]
            }
            config['accessibilitySettings'] = {
                'colourBlindMode': self.defaultSettings["accessibilitySettings"]["colourBlindMode"],
                'colourBlindType': self.defaultSettings["accessibilitySettings"]["colourBlindType"],
                'motionSicknessMode': self.defaultSettings["accessibilitySettings"]["motionSicknessMode"],
                'subtitles': self.defaultSettings["accessibilitySettings"]["subtitles"],
                'hud': self.defaultSettings["accessibilitySettings"]["hud"],
                'hints': self.defaultSettings["accessibilitySettings"]["hints"],
                'tutorial': self.defaultSettings["accessibilitySettings"]["tutorial"]
            }
            with open(self.settingsFile, 'w') as configfile:
                config.write(configfile)
                self.logger.info("Wrote default settings to settings file")
        else:
            self.logger.info("Settings file exists")
            

    # Function to check if the required packages are installed and if not installs them
    def checkAndInstallPackages(self):
        """
        Checks if the required packages are installed and if not installs them
        """
        required_packages = ['pygame', "perlin-noise", "numpy", "h5py"]
        
        for package in required_packages:
            try:
                __import__(package)
                self.logger.info(f"{package} is installed")

            except ImportError: 
                if package == "perlin-noise":
                    try:
                        __import__("perlin_noise")
                        self.logger.info(f"{package} is installed")
                    except ImportError:
                        self.logger.info(f"{package} is not installed. Installing...")
                        subprocess.check_call(['pip', 'install', "perlin-noise"])
                        self.logger.info(f"{package} has been installed.")
                        __import__("perlin_noise")
                        self.logger.info(f"{package} is imported")
             
                self.logger.info(f"{package} is not installed. Installing...")
                subprocess.check_call(['pip', 'install', package])
           
                self.logger.info(f"{package} has been installed.")

    # Asset management

    def checkAndUpdateAssets(self):
        """
        Checks if the assets are up to date and if not updates them
        """
        if not self.assetsExist(assetDict=self.assetDict):
            self.downloadAndReplaceAssets()
    
    def assetsExist(self, assetDict):
        """
        Checks if the assets exist
        """
        self.logger.info("Checking if assets exist")
        for key, value in assetDict.items():
            if isinstance(value, dict):
                
                if 'mainPath' in value:
                    self.logger.info(f"Checking if {key} exists")
                    if not os.path.exists(value['mainPath']):
                        self.logger.info(f"{key} does not exist")
                        return False
                
                if not self.assetsExist(value):
                    self.logger.info(f"{key} does not exist")
                    return False
                
                self.logger.info(f"{key} exists")
            
            else:
                if not os.path.exists(value):
                    self.logger.info(f"{key} does not exist")
                    return False
                
                self.logger.info(f"{key} exists")

        self.logger.info("All assets exist")
        return True
    

    def downloadAndReplaceAssets(self):
        """
        Downloads and replaces the assets
        """
        tempDir = mkdtemp()
        self.logger.info(f"Created temp folder: {tempDir}")
        print(f"Created temp folder: {tempDir}")

        self.logger.info("Downloading assets from github")

        # Download the zip file from the github repository
        try:
            urllib.request.urlretrieve(self.githubAssets, os.path.join(tempDir, "gameFiles.zip"))
            self.logger.info("Downloaded assets from github")
        
        except Exception as e:
            self.logger.error(f"Error downloading assets: {e}")
            self.errorPopup(f"Error downloading assets: {e}")
            raise ValueError("Error downloading assets")
        
        # Extract the zip file to the temp folder
        try:
            with zipfile.ZipFile(os.path.join(tempDir, "gameFiles.zip"), 'r') as _zip:
                tempExtractPath = os.path.join(tempDir, "extracted")
                _zip.extractall(tempExtractPath)
                self.logger.info(f"Extracted assets to {tempExtractPath}")
        
        except Exception as e:
            self.logger.error(f"Error extracting assets: {e}")
            self.errorPopup(f"Error extracting assets: {e}")
            raise ValueError("Error extracting assets")
        
        # clear current assets folder
        self.logger.info(f"Clearing assets folder: {self.assetPath}")
        if os.path.exists(self.assetPath):
            shutil.rmtree(self.assetPath)
            self.logger.info(f"Deleted assets folder: {self.assetPath}")
        
        # Copy the extracted assets to the assets folder
        os.makedirs(self.assetPath)
        self.logger.info(f"Created assets folder: {self.assetPath}")

        # Move the extracted assets to the assets folder
        extractedDir = os.path.join(tempExtractPath, os.listdir(tempExtractPath)[0])
        for item in os.listdir(extractedDir):
            ertI = os.path.join(extractedDir, item)

            asI = os.path.join(self.assetPath, item)
            
            if os.path.isdir(ertI):
                shutil.copytree(ertI, asI, False, None)
                self.logger.info(f"Created directory: {asI}")

            else:
                shutil.copy2(ertI, asI)
                self.logger.info(f"Copied file: {asI}")
        
        self.logger.info("Assets have been downloaded and extracted")
        
        # clear temp folder
        shutil.rmtree(tempDir)
        self.logger.info(f"Deleted temp folder: {tempDir}")
            

   

def run():
    """
    Runs the initialisation code
    """
    initialise = initalise()
    initialise.checkPaths()
    afterlightLogging()
    initialise.checkSettings()
    initialise.checkAndInstallPackages()
    initialise.checkAndUpdateAssets()


