"""
Author Block
Author: James Collum
Date Creation: 29/05/2024
Document Name: variables.py
Purpose of Document: This document will be used to store all global variables for the game.

"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))






# game variables
GRAVITY = 0.75
ROWS = 16
COLS = 150
TILE_SIZE = 1080 // ROWS
TILE_TYPES = 21
level = 1


class gameState:
    MAIN_MENU = 0
    RESUME_GAME = 1
    NEW_GAME = 2
    LOAD_GAME = 3
    STATISTICS = 4
    SETTINGS = 5
    PAUSE_MENU = 6
    INVENTORY = 7
    GAME = 8

playerPosition = [0, 0]

loadGame = {}


class colours:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    PINK = (255, 192, 203)
    GREY = (128, 128, 128)
    GRAY = (128, 128, 128)
    BROWN = (165, 42, 42)
    LIME = (0, 255, 0)
    TEAL = (0, 128, 128)
    NAVY = (0, 0, 128)
    MAROON = (128, 0, 0)
    OLIVE = (128, 128, 0)
    SKY_BLUE = (135, 206, 235)
    TAN = (210, 180, 140)
    GOLD = (255, 215, 0)
    SILVER = (192, 192, 192)
    BRONZE = (205, 127, 50)
    COPPER = (184, 115, 51)
    PLATINUM = (229, 228, 226)
    DIAMOND = (185, 242, 255)
    EMERALD = (0, 201, 87)
    SAPPHIRE = (15, 82, 186)
    RUBY = (224, 17, 95)
    AMETHYST = (153, 102, 204)
    TOPAZ = (255, 204, 0)
    PEARL = (234, 224, 200)
    OPAL = (168, 195, 188)
    IRON = (240, 240, 240)
    STEEL = (192, 192, 192)
    TITANIUM = (128, 128, 128)
    ALUMINIUM = (160, 160, 160)
    COPPER = (184, 115, 51)
    BRASS = (181, 166, 66)
    

saveGame = {
    "inventory": {},
    "world": {
        "worldName": "default",
        "worldSeed": 0,
        "worldSize": 0,
        "worldType": "default",
        "worldDifficulty": 1,
        "worldTime": 0,
        "worldWeather": "clear",
    },
    "player": {
        "position": (0, 0),
        "health": 100,
        "hunger": 100,
        "thirst": 100,
        "stamina": 100,
        "oxygen": 100,
        "weight": 0,
        "speed": 5,
        "attack": 1.0,
        "defence": 1.0,
        "experience": 0,
        "difficulty": 1
    },
}
settings = {
    "displaySettings": {
        "resolution": (1920, 1080),
        "fullscreen": False,
        "aspectRatio": (16, 9),
        "refreshRate": 60,
        "vsync": False         
    },
    "graphicsSettings": {
        "textureQuality": 1,
        "shadows": True,
        "lighting": 1,
        "particles": True,
        "postProcessing": True,
        "antialiasing": True
    },
    "audioSettings": {
        "masterVolume": 1.0,
        "musicVolume": 1.0,
        "hostileVolume": 1.0,
        "friendlyVolume": 1.0,
        "interactionVolume": 1.0,
        "environmentVolume": 1.0,
        "ambientVolume": 1.0
    },
    "keybinds": {
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
        "colourBlindType": "protanopia",
        "motionSicknessMode": False,
        "subtitles": False,
        "hud": True,
        "hints": True,
        "tutorial": True,
    }
}