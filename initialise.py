"""
Author Block
Author: James Collum
Date Creation: 16/05/2024
Document Name: initialise.py
Purpose of Document: This file will contain most of the initalisation code and elements
Referenced Code:


"""
import configparser
import logging
import os
import pygame
import subprocess
from pathlib import Path
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
            self.audioPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Audio")
            self.fontPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Fonts")
            self.entityPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Entities")
            self.playerPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Player")
            self.settingsFile = str(Path.home() / "Documents" / "Afterlight" / "Settings" / "settings.ini")
            
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
                        "moveUp": pygame.K_w,
                        "moveDown": pygame.K_s,
                        "moveLeft": pygame.K_a,
                        "moveRight": pygame.K_d,
                        "jump": pygame.K_SPACE,
                        "inventory": pygame.K_e,
                        "pause": pygame.K_ESCAPE,
                        "sprint": pygame.K_LSHIFT,
                        "crouch": pygame.K_LCTRL,
                    },
                    "mouseSettings": {
                        "sensitivity": 1,
                        "inverted": False,
                        "attack": pygame.BUTTON_LEFT,
                        "interact": pygame.BUTTON_RIGHT,
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

    def setupLogging(self, maxBytes, backupCount):
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
        if not os.path.exists(self.audioPath):
            os.makedirs(self.audioPath)
        if not os.path.exists(self.fontPath):
            os.makedirs(self.fontPath)
        if not os.path.exists(self.entityPath):
            os.makedirs(self.entityPath)
        if not os.path.exists(self.playerPath):
            os.makedirs(self.playerPath)
    

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


    def check_and_install_packages():
        """
        Checks if the required packages are installed and if not installs them
        """
        required_packages = ['pygame']
        
        for package in required_packages:
            try:
                __import__(package)
            except ImportError:
                print(f"{package} is not installed. Installing...")
                subprocess.check_call(['pip', 'install', package])
                print(f"{package} has been installed.")
    

