"""
Author Block
Author: James Collum
Date Creation: 18/05/2024
Document Name: settings.py
Purpose of Document: 
                     The purpose of this document is to create a settings class that will be used to store the settings of the game. 
                     This will allow the user to change the settings of the game such as the volume, the resolution, the controls, etc. 
                     This will also allow the user to save their settings so that they do not have to change them every time they play the game.
Referenced Code:


"""
import configparser
import logging
import os
import pygame
import pathlib
import subprocess
from pathlib import Path
from src.variables import settings


class Settings:
    def __init__(self, *args, **kwargs):
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.settingsPath = str(Path.home() / "Documents" / "Afterlight" / "Settings")
        self.config = configparser.ConfigParser()
        self.logger = logging.getLogger(__name__)
        self.settings = settings
    
    def loadSettings(self):
        # Load the settings from the settings file when the game starts
        try:
            self.config.read(self.settingsPath)
            _configDict = {section: dict(self.config.items(section)) for section in self.config.sections()}
            self.settings = _configDict
            self.logger.info(f"Settings loaded: {self.settings}")

        except Exception as e:
            self.logger.error(f"Error loading settings: {e}")
            raise Exception(f"Error loading settings: {e}")
    
    def saveSettings(self):
        # Save the settings to the settings file only when the apply button is clicked
        try:
            self.config.read(self.settingsPath)
            for section in self.settings:
                for key in self.settings[section]:
                    self.config[section][key] = self.settings[section][key]
            with open(self.settingsPath, "w") as file:
                self.config.write(file)
            self.logger.info(f"Settings saved: {self.settings}")
        except Exception as e:
            self.logger.error(f"Error saving settings: {e}")
            raise Exception(f"Error saving settings: {e}")
    
    def setResolution(self, resolution= (1920, 1080)):
        # Check if the resolution is valid - cannot be less than 800x600
        if resolution[0] < 800 or resolution[1] < 600:
            self.logger.error("Resolution cannot be less than 800x600")
            raise Exception("Resolution cannot be less than 800x600")
        
        self.settings["displaySettings"]["Resolution"] = resolution
    
    def setFullscreen(self, fullscreen= False):
        self.settings["displaySettings"]["Fullscreen"] = fullscreen
    
    def aspectRatio(self, aspectRatio= (16, 9)):
        self.settings["displaySettings"]["AspectRatio"] = aspectRatio

    def setRefreshRate(self, refreshRate= 60):
        # Check if the refresh rate is valid - cannot be less than 5 fps
        if refreshRate < 5:
            self.logger.error("Refresh rate cannot be less than 5 fps")
            raise Exception("Refresh rate cannot be less than 5 fps")
        
        self.settings["displaySettings"]["RefreshRate"] = refreshRate
    
    def vsync(self, vsync= False):
        self.settings["displaySettings"]["Vsync"] = vsync

    def textureQuality(self, textureQuality= 1):
        self.settings["graphicsSettings"]["TextureQuality"] = textureQuality
    
    def shadows(self, shadows= False):
        self.settings["graphicsSettings"]["Shadows"] = shadows
    
    def lighting(self, lighting= 1):
        self.settings["graphicsSettings"]["Lighting"] = lighting
    
    def particles(self, particles= True):
        self.settings["graphicsSettings"]["Particles"] = particles
    
    def postProcessing(self, postProcessing= True):
        self.settings["graphicsSettings"]["PostProcessing"] = postProcessing
    
    def antiAliasing(self, antiAliasing= True):
        self.settings["graphicsSettings"]["AntiAliasing"] = antiAliasing

    def setVolume(self, volume= 1.0):
        self.settings["audioSettings"]["Volume"] = volume

    def setMusicVolume(self, musicVolume= 1.0):
        self.settings["audioSettings"]["MusicVolume"] = musicVolume
    
    def setSFXVolume(self, sfxVolume= 1.0):
        self.settings["audioSettings"]["SFXVolume"] = sfxVolume
    
    def setHostileVolume(self, hostileVolume= 1.0):
        self.settings["audioSettings"]["HostileVolume"] = hostileVolume
    
    def setFriendlyVolume(self, friendlyVolume= 1.0):
        self.settings["audioSettings"]["FriendlyVolume"] = friendlyVolume
    
    def setInteractionVolume(self, interactionVolume= 1.0):
        self.settings["audioSettings"]["InteractionVolume"] = interactionVolume
    
    def setEnvironmentVolume(self, environmentVolume= 1.0):
        self.settings["audioSettings"]["EnvironmentVolume"] = environmentVolume
    
    def setAmbientVolume(self, ambientVolume= 1.0):
        self.settings["audioSettings"]["AmbientVolume"] = ambientVolume

    def setKeyBindings(self, interaction = "moveUp", key="w"):
        self.settings["keybinds"][interaction] = key
    
    def setMouseSensitivity(self, mouseSensitivity= 1.0):
        self.settings["mouseSettings"]["sensitivity"] = mouseSensitivity
    
    def setInvertMouse(self, invertMouse= False):
        self.settings["mouseSettings"]["invertMouse"] = invertMouse
    
    def setAttack(self, attack= "LEFT"):
        # Check to see if it is key like w, a, s, d, etc.
        if attack not in pygame.key.name:
            self.logger.error("Invalid key for attack")
            raise Exception("Invalid key for attack")
        
        self.settings["mouseSettings"]["attack"] = attack

    def setInteract(self, interact= "RIGHT"):
        # Check to see if it is key like w, a, s, d, etc.
        if interact not in pygame.key.name:
            self.logger.error("Invalid key for interact")
            raise Exception("Invalid key for interact")
        
        self.settings["mouseSettings"]["interact"] = interact
    
    def setColourBlindMode(self, colourBlindMode= False):
        self.settings["gameSettings"]["ColourBlindMode"] = colourBlindMode
    
    def setColourBlindModeType(self, colourBlindModeType= "protanopia"):
        # Check to see if it is a valid colour blind mode
        if colourBlindModeType not in ["protanopia", "deuteranopia", "tritanopia"]:
            self.logger.error("Invalid colour blind mode type")
            raise Exception("Invalid colour blind mode type")
        
        self.settings["gameSettings"]["ColourBlindModeType"] = colourBlindModeType
    
    def setMotionSicknessMode(self, motionSicknessMode= False):
        self.settings["gameSettings"]["MotionSicknessMode"] = motionSicknessMode
    
    def setSubtitles(self, subtitles= True):
        self.settings["gameSettings"]["Subtitles"] = subtitles
    
    def setHUD(self, HUD= True):
        self.settings["gameSettings"]["HUD"] = HUD

    def setHints(self, hints= True):
        self.settings["gameSettings"]["Hints"] = hints
    
    def setTutorial(self, tutorial= True):
        self.settings["gameSettings"]["Tutorial"] = tutorial
