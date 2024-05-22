"""
Author Block
Author: James Collum
Date Creation: 16/05/2024
Document Name: initialise.py
Purpose of Document: This file will contain most of the initalisation code and elements
Referenced Code:


"""
import pygame
import os
import configparser
from pathlib import Path

class initalise:
    """
    Specifies the default paths for the game to use, also checks if the paths exist and if not creates them, also specifies the default settings for the game
    """
    def __init__(self, *args, **kwargs): 
            self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
            self.settingsPath = str(Path.home() / "Documents" / "Afterlight" / "Settings")
            self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
            self.backUpPath = str(Path.home() / "Documents" / "Afterlight" / "Backups")
            self.assetPath = str(Path.home() / "Documents" / "Afterlight" / "Assets")
            self.audioPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Audio")
            self.fontPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Fonts")
            self.entityPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Entities")
            self.playerPath = str(Path.home() / "Documents" / "Afterlight" / "Assets" / "Player")
            """
            self.defualtSettings = {
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
                    }
            }
            """
            self.settingsFile = str(Path.home() / "Documents" / "Afterlight" / "Settings" / "settings.json")
            self.gameSettingsFile = str(Path.home() / "Documents" / "Afterlight" / "Settings" / "gameSettings.json")
            