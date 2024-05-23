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


class Settings:
    def __init__(self, *args, **kwargs):
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.settingsPath = str(Path.home() / "Documents" / "Afterlight" / "Settings")
        self.config = configparser.ConfigParser()
        
    