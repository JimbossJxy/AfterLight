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
import configparser
import ctypes
import logging
import misc
import os
import pathlib
import subprocess
import sys
import shutil
import webbrowser
import zipfile
from misc import misc
from pathlib import Path
from tempfile import TemporaryDirectory, mkdtemp
from logging.handlers import RotatingFileHandler



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
            
            self.defaultSettings = {
                  "displaySettings": {
                        "resolution": (1920, 1080),
                        "fullscreen": False,
                        "aspectRatio": (16, 9),
                        "vsync": False         
                    },
                    "graphicsSettings": {
                        "textureQuality": 1,
                        "shadows": True,
                        "lighting": True,
                        "particles": True,
                        "postProcessing": True,
                        "antialiasing": True
                    },
                    "audioSettings": {
                        "masterVolume": 1,
                        "musicVolume": 1,
                        "sfxVolume": 1
                    },
                    "keybinds": {
                        "moveUp": "w",
                        "moveDown": "s",
                        "moveLeft": "a",
                        "moveRight": "d",
                        "jump": "SPACE",
                        "inventory": "e",
                        "pause": "ESCAPE",
                        "sprint": "LSHIFT",
                        "crouch": "LCRTL",
                    },
                    "mouseSettings": {
                        "sensitivity": 1,
                        "inverted": False,
                        "attack": "LEFT",
                        "interact": "RIGHT",
                    },
                    "accessibilitySettings": {
                        "colourBlindMode": False,
                        "colourBlindType": 0,
                        "motionSicknessMode": False,
                        "subtitles": False,
                        "hud": True,
                        "crosshair": True,
                        "hints": True,
                        "tutorial": True,
                    },
                    "logSettings": {
                          "fileSize": 3145728,
                          "maxFiles": 10,
                    }
            }

    def setupLogging(self, maxBytes, backupCount): # Function to setup logging - Must be called before logging is used and after the paths have been checked
        """
        Sets up the logging for the game
        """
        handler = RotatingFileHandler(self.logPath + "/game.log", maxBytes=maxBytes, backupCount=backupCount)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.addHandler(logging.StreamHandler())
        logger.info("Logging has been setup")

    
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
            config['DisplaySettings'] = {
                'resolution': self.defaultSettings["displaySettings"]["resolution"],
                'fullscreen': self.defaultSettings["displaySettings"]["fullscreen"],
                'aspectRatio': self.defaultSettings["displaySettings"]["aspectRatio"],
                'vsync': self.defaultSettings["displaySettings"]["vsync"]
            }
            config['GraphicsSettings'] = {
                'textureQuality': self.defaultSettings["graphicsSettings"]["textureQuality"],
                'shadows': self.defaultSettings["graphicsSettings"]["shadows"],
                'lighting': self.defaultSettings["graphicsSettings"]["lighting"],
                'particles': self.defaultSettings["graphicsSettings"]["particles"],
                'postProcessing': self.defaultSettings["graphicsSettings"]["postProcessing"],
                'antialiasing': self.defaultSettings["graphicsSettings"]["antialiasing"]
            }
            config['AudioSettings'] = {
                'masterVolume': self.defaultSettings["audioSettings"]["masterVolume"],
                'musicVolume': self.defaultSettings["audioSettings"]["musicVolume"],
                'sfxVolume': self.defaultSettings["audioSettings"]["sfxVolume"]
            }
            config['Keybinds'] = {
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
            config['MouseSettings'] = {
                'sensitivity': self.defaultSettings["mouseSettings"]["sensitivity"],
                'inverted': self.defaultSettings["mouseSettings"]["inverted"],
                'attack': self.defaultSettings["mouseSettings"]["attack"],
                'interact': self.defaultSettings["mouseSettings"]["interact"]
            }
            config['AccessibilitySettings'] = {
                'colourBlindMode': self.defaultSettings["accessibilitySettings"]["colourBlindMode"],
                'colourBlindType': self.defaultSettings["accessibilitySettings"]["colourBlindType"],
                'motionSicknessMode': self.defaultSettings["accessibilitySettings"]["motionSicknessMode"],
                'subtitles': self.defaultSettings["accessibilitySettings"]["subtitles"],
                'hud': self.defaultSettings["accessibilitySettings"]["hud"],
                'crosshair': self.defaultSettings["accessibilitySettings"]["crosshair"],
                'hints': self.defaultSettings["accessibilitySettings"]["hints"],
                'tutorial': self.defaultSettings["accessibilitySettings"]["tutorial"]
            }
            with open(self.settingsFile, 'w') as configfile:
                config.write(configfile)
                logging.info("Wrote default settings to settings file")
                print("Wrote default settings to settings file")

    # Function to check if the required packages are installed and if not installs them
    def check_and_install_packages(self):
        """
        Checks if the required packages are installed and if not installs them
        """
        required_packages = ['pygame', 'requests', "perlin-noise"]
        
        for package in required_packages:
            try:
                __import__(package)
                logging.info(f"{package} is installed")
                print(f"{package} is installed")
            except ImportError: 
                print(f"{package} is not installed. Installing...")
                logging.info(f"{package} is not installed. Installing...")
                subprocess.check_call(['pip', 'install', package])
                print(f"{package} has been installed.")
                logging.info(f"{package} has been installed.")


    
    def download_and_extract_assets(self):
        import requests
        """
        Downloads the assets from the github repository and extracts them to the assets folder
        """
        _zipUrl = "https://github.com/JimbossJxy/afterlightAssets/archive/refs/heads/main.zip"
        try:
            # Download the zip file from the github repository
            logging.info("Downloading assets from github")
            _getZip = requests.get(_zipUrl)
            _getZip.raise_for_status()
            
            # Verify that the content type is a zip file
            if _getZip.headers['Content-Type'] != 'application/zip':
                logging.error("Error downloading assets: Content type is not a zip file")
                print("Error downloading assets: Content type is not a zip file")
                raise ValueError("Content type is not a zip file")

            # Extract the zip file to the temp folder
            tempDir = mkdtemp()
            logging.info(f"Created temp folder: {tempDir}")
            print(f"Created temp folder: {tempDir}")

            
            _zipPath = os.path.join(tempDir, "gameFiles.zip")
            with open(_zipPath, 'wb') as _zipFile:
                _zipFile.write(_getZip.content)
                logging.info(f"Extracting assets to the temp folder: {_zipPath}")
                print(f"Extracting assets to the temp folder: {_zipPath}")

            # Extract the zip file to temparory folder
            with zipfile.ZipFile(_zipPath, 'r') as _zip:
                tempExtractPath = os.path.join(tempDir, "extracted")
                logging.info(f"Temp path: {tempExtractPath}")
                _zip.extractall(tempExtractPath)
                logging.info(f"Extracted assets to {tempExtractPath}")
                print(f"Extracted assets to {tempExtractPath}")
                
                # Check if all assests exist in assets folder
                
                assetsExist = True
                for root, _, files in os.walk(tempExtractPath):
                    for name in files:
                        relativePath = os.path.relpath(os.path.join(root, name), tempExtractPath)
                        if not os.path.exists(os.path.join(self.assetPath,relativePath)):
                            assetsExist = False
                            break
                    if not assetsExist:
                        break
                

                # If assets do not exist, clear assets folder and copy them to the assets folder
                if not assetsExist:
                    logging.info(f"Missing assets detected, clearing assets folder: {self.assetPath}")
                    print(f"Missing assets detected, clearing assets folder: {self.assetPath}")
                    if os.path.exists(self.assetPath):
                        shutil.rmtree(self.assetPath)
                        logging.info(f"Deleted assets folder: {self.assetPath}")
                        print(f"Deleted assets folder: {self.assetPath}")

                    os.makedirs(self.assetPath)
                    logging.info(f"Created assets folder: {self.assetPath}")
                    print(f"Created assets folder: {self.assetPath}")
                    logging.info(f"Copying assets to assets folder: {self.assetPath}")

                    for root, directories, files in os.walk(tempExtractPath):
                        for _ in directories:
                            destinationFolderPath = os.path.join(self.assetPath, os.path.relpath(root, tempExtractPath))
                            os.makedirs(destinationFolderPath, exist_ok=True)
                            logging.info(f"Created directory: {destinationFolderPath}")
                            print(f"Created directory: {destinationFolderPath}")
                        for fileName in files:
                            relativePath = os.path.relpath(os.path.join(root, fileName), tempExtractPath)
                            destinationFilePath = os.path.join(self.assetPath, relativePath)
                            os.makedirs(os.path.dirname(destinationFilePath), exist_ok=True)
                            shutil.copy2(os.path.join(root, fileName), destinationFilePath)
                    
            logging.info("Assets have been downloaded and extracted")
            print("Assets have been downloaded and extracted")

            # Remove the temp folder for cleanup
            os.remove(tempDir)    
        
        # Error handling
        except requests.exceptions.RequestException as e:
            logging.error(f"Error downloading assets: {e}")
            print(f"Error downloading assets: {e}")
            self.errorPopup(f"Error downloading assets{e}")
            raise ValueError("Error downloading assets")
        
        except zipfile.BadZipFile as e:
            logging.error(f"Error extracting assets: {e}")
            print(f"Error extracting assets: {e}")
            self.errorPopup(f"Error extracting assets: {e}")
            raise ValueError("Error extracting assets")
        
        except Exception as e:
            logging.error(f"An Unexpected Error Occured: {e}")
            print(f"An Unexpected Error Occured: {e}")
            self.errorPopup(f"An Unexpected Error Occured: {e}")
            raise e

    
initalise().check_and_install_packages()

