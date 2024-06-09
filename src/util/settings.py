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
        self.settingsConfig = str(Path.home() / "Documents" / "Afterlight" / "Settings" / "settings.ini")
        self.config = configparser.ConfigParser()
        self.logger = logging.getLogger(__name__)
        self.settings = settings
    
    def loadSettings(self):
        # Load the settings from the settings file when the game starts
        try:
            if not Path(self.settingsConfig).exists():
                self.saveSettings()
            
            self.config.read(self.settingsConfig)
            _configDict = {section: dict(self.config.items(section)) for section in self.config.sections()}
            self.settings = _configDict
            self.logger.info(f"Settings loaded: {self.settings}")

        except Exception as e:
            self.logger.error(f"Error loading settings: {e}")
            raise Exception(f"Error loading settings: {e}")
    
    def saveSettings(self):
        # Save the settings to the settings file only when the apply button is clicked
        try:
            # Create the directories if they don't exist
            os.makedirs(os.path.dirname(self.settingsPath), exist_ok=True)

            self.config.read(self.settingsConfig)
            for section in self.settings:
                for key in self.settings[section]:
                    self.config[section][key] = str(self.settings[section][key])  # Convert value to string
            with open(self.settingsConfig, "w") as file:
                self.config.write(file)
            self.logger.info(f"Settings saved: {self.settings}")
        except Exception as e:
            self.logger.error(f"Error saving settings: {e}")
            raise Exception(f"Error saving settings: {e}")
        
    def getSetting(self, setting=None):
        # Get the setting from the settings dictionary
        if setting is None:
            self.logger.error("No setting provided")
            raise Exception("No setting provided")

        _keys = setting.split(".")
        _value = self.settings
        for key in _keys:
            if key in _value:
               _value = _value[key]
            else:
                self.logger.error("Invalid setting")
                raise Exception("Invalid setting")
            
        self.logger.info(f"Setting: {setting} Value: {_value}")
        return _value
        

    def setResolution(self, resolution= (1920, 1080)):
        # Check if the resolution is valid - cannot be less than 800x600
        if resolution[0] < 800 or resolution[1] < 600:
            self.logger.error("Resolution cannot be less than 800x600")
            raise Exception("Resolution cannot be less than 800x600")
        
        self.settings["displaySettings"]["resolution"] = resolution
    
    def setFullscreen(self, fullscreen= False):
        self.settings["displaySettings"]["fullscreen"] = fullscreen
    
    def aspectRatio(self, aspectRatio= (16, 9)):
        self.settings["displaySettings"]["aspectRatio"] = aspectRatio

    def setRefreshRate(self, refreshRate= 60):
        # Check if the refresh rate is valid - cannot be less than 5 fps
        if refreshRate < 5:
            self.logger.error("Refresh rate cannot be less than 5 fps")
            raise Exception("Refresh rate cannot be less than 5 fps")
        
        self.settings["displaySettings"]["refreshRate"] = refreshRate
    
    def vsync(self, vsync= False):
        self.settings["displaySettings"]["vsync"] = vsync
        self.logger.info(f"Vsync: {vsync}")

    def textureQuality(self, textureQuality= 1):
        self.settings["graphicsSettings"]["textureQuality"] = textureQuality
        self.logger.info(f"Texture Quality: {textureQuality}")
    
    def shadows(self, shadows= False):
        self.settings["graphicsSettings"]["shadows"] = shadows
        self.logger.info(f"Shadows: {shadows}")
    
    def lighting(self, lighting= 1):
        self.settings["graphicsSettings"]["lighting"] = lighting
        self.logger.info(f"Lighting: {lighting}")
    
    def particles(self, particles= True):
        self.settings["graphicsSettings"]["particles"] = particles
        self.logger.info(f"Particles: {particles}")
    
    def postProcessing(self, postProcessing= True):
        self.settings["graphicsSettings"]["postProcessing"] = postProcessing
        self.logger.info(f"Post Processing: {postProcessing}")
    
    def antiAliasing(self, antiAliasing= True):
        self.settings["graphicsSettings"]["antialiasing"] = antiAliasing
        self.logger.info(f"Anti Aliasing: {antiAliasing}")

    def setVolume(self, volume= 1.0):
        self.settings["audioSettings"]["masterVolume"] = volume
        self.logger.info(f"Volume: {volume}")

    def setMusicVolume(self, musicVolume= 1.0):
        self.settings["audioSettings"]["musicVolume"] = musicVolume
        self.logger.info(f"Music Volume: {musicVolume}")

    
    def setHostileVolume(self, hostileVolume= 1.0):
        self.settings["audioSettings"]["hostileVolume"] = hostileVolume
        self.logger.info(f"Hostile Volume: {hostileVolume}")
    
    def setFriendlyVolume(self, friendlyVolume= 1.0):
        self.settings["audioSettings"]["friendlyVolume"] = friendlyVolume
        self.logger.info(f"Friendly Volume: {friendlyVolume}")
    
    def setInteractionVolume(self, interactionVolume= 1.0):
        self.settings["audioSettings"]["interactionVolume"] = interactionVolume
        self.logger.info(f"Interaction Volume: {interactionVolume}")
    
    def setEnvironmentVolume(self, environmentVolume= 1.0):
        self.settings["audioSettings"]["environmentVolume"] = environmentVolume
        self.logger.info(f"Environment Volume: {environmentVolume}")
    
    def setAmbientVolume(self, ambientVolume= 1.0):
        self.settings["audioSettings"]["ambientVolume"] = ambientVolume
        self.logger.info(f"Ambient Volume: {ambientVolume}")

    def setKeyBindings(self, interaction = "moveUp", key="w"):
        self.settings["keybinds"][interaction] = key
        self.logger.info(f"Key Binding: {interaction} Key: {key}")
    
    def setMouseSensitivity(self, mouseSensitivity= 1.0):
        self.settings["mouseSettings"]["sensitivity"] = mouseSensitivity
        self.logger.info(f"Mouse Sensitivity: {mouseSensitivity}")
    
    def setInvertMouse(self, invertMouse= False):
        self.settings["mouseSettings"]["invertMouse"] = invertMouse
        self.logger.info(f"Invert Mouse: {invertMouse}")
    
    

    
    def setColourBlindMode(self, colourBlindMode= False):
        self.settings["accessibilitySettings"]["colourBlindMode"] = colourBlindMode
        self.logger.info(f"Colour Blind Mode: {colourBlindMode}")
    
    def setColourBlindModeType(self, colourBlindModeType= "protanopia"):
        # Check to see if it is a valid colour blind mode
        if colourBlindModeType not in ["protanopia", "deuteranopia", "tritanopia"]:
            self.logger.error("Invalid colour blind mode type")
            raise Exception("Invalid colour blind mode type")
        
        self.settings["accessibilitySettings"]["colourBlindType"] = colourBlindModeType
        self.logger.info(f"Colour Blind Mode Type: {colourBlindModeType}")
    
    def setMotionSicknessMode(self, motionSicknessMode= False):
        self.settings["accessibilitySettings"]["motionSicknessMode"] = motionSicknessMode
        self.logger.info(f"Motion Sickness Mode: {motionSicknessMode}")
    
    def setSubtitles(self, subtitles= True):
        self.settings["accessibilitySettings"]["subtitles"] = subtitles
        self.logger.info(f"Subtitles: {subtitles}")
    
    def setHUD(self, HUD= True):
        self.settings["accessibilitySettings"]["hud"] = HUD
        self.logger.info(f"HUD: {HUD}")

    def setHints(self, hints= True):
        self.settings["accessibilitySettings"]["hints"] = hints
        self.logger.info(f"Hints: {hints}")
    
    def setTutorial(self, tutorial= True):
        self.settings["accessibilitySettings"]["tutorial"] = tutorial
        self.logger.info(f"Tutorial: {tutorial}")

def run_tests():
    # Create an instance of the Settings class
    settings = Settings()

    # Load the settings
    settings.loadSettings()

    # Test getting a setting
    resolution = settings.getSetting("displaySettings.resolution")
    print(f"Resolution: {resolution}")

    # Test setting a resolution
    settings.setResolution((1280, 720))
    new_resolution = settings.getSetting("displaySettings.resolution")
    print(f"New Resolution: {new_resolution}")

    # Test saving the settings
    settings.saveSettings()

    # Test setting and getting other settings
    settings.setFullscreen(True)
    fullscreen = settings.getSetting("displaySettings.fullscreen")
    print(f"Fullscreen: {fullscreen}")

    settings.setRefreshRate(144)
    refresh_rate = settings.getSetting("displaySettings.refreshRate")
    print(f"Refresh Rate: {refresh_rate}")

    settings.setVolume(0.5)
    volume = settings.getSetting("audioSettings.masterVolume")
    print(f"Volume: {volume}")

    settings.setKeyBindings("moveUp", "up")
    key_binding = settings.getSetting("keybinds.moveUp")
    print(f"Key Binding: {key_binding}")

    settings.setColourBlindMode(True)
    colour_blind_mode = settings.getSetting("accessibilitySettings.colourBlindMode")
    print(f"Colour Blind Mode: {colour_blind_mode}")

    # Add more tests for other settings
    

   

    settings.setMusicVolume(0.8)
    music_volume = settings.getSetting("audioSettings.musicVolume")
    print(f"Music Volume: {music_volume}")


    settings.setHostileVolume(0.7)
    hostile_volume = settings.getSetting("audioSettings.hostileVolume")
    print(f"Hostile Volume: {hostile_volume}")

    settings.setFriendlyVolume(0.9)
    friendly_volume = settings.getSetting("audioSettings.friendlyVolume")
    print(f"Friendly Volume: {friendly_volume}")

    settings.setInteractionVolume(0.6)
    interaction_volume = settings.getSetting("audioSettings.interactionVolume")
    print(f"Interaction Volume: {interaction_volume}")

    settings.setEnvironmentVolume(0.8)
    environment_volume = settings.getSetting("audioSettings.environmentVolume")
    print(f"Environment Volume: {environment_volume}")

    settings.setAmbientVolume(0.7)
    ambient_volume = settings.getSetting("audioSettings.ambientVolume")
    print(f"Ambient Volume: {ambient_volume}")

    settings.setMouseSensitivity(0.8)
    mouse_sensitivity = settings.getSetting("mouseSettings.sensitivity")
    print(f"Mouse Sensitivity: {mouse_sensitivity}")

    settings.setInvertMouse(True)
    invert_mouse = settings.getSetting("mouseSettings.invertMouse")
    print(f"Invert Mouse: {invert_mouse}")

    settings.setColourBlindMode(True)
    colour_blind_mode = settings.getSetting("accessibilitySettings.colourBlindMode")
    print(f"Colour Blind Mode: {colour_blind_mode}")

    settings.setColourBlindModeType("deuteranopia")
    colour_blind_mode_type = settings.getSetting("accessibilitySettings.colourBlindType")
    print(f"Colour Blind Mode Type: {colour_blind_mode_type}")

    settings.setMotionSicknessMode(True)
    motion_sickness_mode = settings.getSetting("accessibilitySettings.motionSicknessMode")
    print(f"Motion Sickness Mode: {motion_sickness_mode}")

    settings.setSubtitles(False)
    subtitles = settings.getSetting("accessibilitySettings.subtitles")
    print(f"Subtitles: {subtitles}")

    settings.setHUD(False)
    hud = settings.getSetting("accessibilitySettings.hud")
    print(f"HUD: {hud}")

    settings.setHints(False)
    hints = settings.getSetting("accessibilitySettings.hints")
    print(f"Hints: {hints}")

    settings.setTutorial(False)
    tutorial = settings.getSetting("accessibilitySettings.tutorial")
    print(f"Tutorial: {tutorial}")

    # Test saving the settings
    settings.saveSettings()
    

# Run the tests
if __name__ == "__main__":
    run_tests()

