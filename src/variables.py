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
# Default inventory layout - This will be used to create the inventory for the player or if the player has a corrupted inventory will be used to reset the inventory.
inventory = {
    "hotbar": {
        "position1": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        "isEquipped": True,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position2": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        "isEquipped": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position3": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        "isEquipped": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position4": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        "isEquipped": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position5": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        "isEquipped": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position6": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        "isEquipped": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position7": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        "isEquipped": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        }
    },
    "row1": {
        "position1": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position2": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position3": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position4": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position5": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position6": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position7": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        }
        
    },
    "row2": {
        "position1": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position2": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position3": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position4": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position5": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position6": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position7": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        }
    },
    "row3": {
        "position1": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position2": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position3": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position4": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position5": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position6": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        },
        "position7": {
        "item": "empty",
        "quantity": 0,
        "description": "",
        "isStackable": False,
        "isUsable": False,
        'maxQuantity': 1,
        "percentage": 0.0,
        "damage": 0.0,
        "name": "",
        "brittleness": 0.0
        }
    }
}
 
items = {
    # Empty placeholder
    "empty": {
        "description": "",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 0.0,
        "name": ""
    },
    # Weapons

    # Knives
    "woodknife": {
        "description": "A wooden knife, not very sharp but it will do the job.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 3.0,
        "percentage": 1.0,
        "name": "Wooden Knife",
        "brittleness": 0.25
    },
    "stoneknife": {
        "description": "A stone knife, sharper than a wooden knife but still not the best.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 4.0,
        "percentage": 1.0,
        "name": "Stone Knife",
        "brittleness": 0.2
    },
    "ironknife": {
        "description": "An iron knife, sharp and deadly. Prone to rusting if not taken care of.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 5.0,
        "percentage": 1.0,
        "name": "Iron Knife",
        "brittleness": 0.15
    },
    "steelknife": {
        "description": "A steel knife, sharp and deadly. Very durable.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 6.0,
        "percentage": 1.0,
        "name": "Steel Knife",
        "brittleness": 0.1
    },
    "copperknife": {
        "description": "A copper knife, sharp however doesn't last long.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 4.5,
        "percentage": 1.0,
        "name": "Copper Knife",
        "brittleness": 0.6
    },
    "harditeknife": {
        "description": "A hardite knife, sharp and durable. Hardite is a rare metal only found in volcanic areas.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 7.5,
        "percentage": 1.0,
        "name": "Hardite Knife",
        "brittleness": 0.025
    },

    # Swords
    "katanasword": {
        "description": "A katana, a traditional Japanese sword. Very sharp, deadly and very very rare.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 9.0,
        "percentage": 1.0,
        "name": "Katana",
        "brittleness": 0.01
    },

    # bows
    "diybow": {
        "description": "A DIY bow, made from wood and string. Not very powerful but it will do the job.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 2.0,
        "percentage": 1.0,
        "name": "DIY Bow",
        "brittleness": 0.25
    },
    "compoundbow": {
        "description": "A compound bow, a modern bow design. Very powerful and very accurate.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 6.0,
        "percentage": 1.0,
        "name": "Compound Bow",
        "brittleness": 0.1
    },
    "crossbow": {
        "description": "A crossbow, a medieval weapon. Very powerful and very accurate.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 5.0,
        "percentage": 1.0,
        "name": "Crossbow",
        "brittleness": 0.15
    },

    # Arrows
    "DIYarrow": {
        "description": "A DIY arrow, made from a stick and a rock. Not very powerful or accurate but it will do the job.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 2.0,
        "percentage": 1.0,
        "name": "DIY Arrow",
        "brittleness": 0.0
    },
    "ironarrow": {
        "description": "An iron arrow, made from iron. Very powerful and very accurate.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 4.0,
        "percentage": 1.0,
        "name": "Iron Arrow",
        "brittleness": 0.0
    },
    "steelarrow": {
        "description": "A steel arrow, made from steel. Very powerful and very accurate.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 6.0,
        "percentage": 1.0,
        "name": "Steel Arrow",
        "brittleness": 0.0
    },
    "poisonarrow": {
        "description": "A poison arrow, made from a stick and a toxic plant. Very deadly.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 8.0,
        "percentage": 1.0,
        "name": "Poison Arrow",
        "brittleness": 0.0
    },

    # Guns
    "pistol": {
        "description": "A pistol, a small firearm. Basic and semi accurate. Requires bullets.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 8.0,
        "percentage": 1.0,
        "name": "Pistol",
        "brittleness": 0.1
    },
    "rifle": {
        "description": "A rifle, a long firearm. Powerful and accurate. Requires bullets.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 12.0,
        "percentage": 1.0,
        "name": "Rifle",
        "brittleness": 0.025
    },
    "shotgun": {
        "description": "A shotgun, a short firearm. Very powerful at close range but not very accurate. Requires bullets.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 16.0,
        "percentage": 1.0,
        "name": "Shotgun",
        "brittleness": 0.05
    },
    "sniper": {
        "description": "A sniper rifle, a long range firearm. Very powerful, very accurate, but slow. Requires bullets.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 20.0,
        "percentage": 1.0,
        "name": "Sniper Rifle",
        "brittleness": 0.05
    },
    "machinegun": {
        "description": "A machine gun, a rapid fire firearm. Very powerful but not very accurate. Only found in loot creates. Requires bullets.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 10.0,
        "percentage": 1.0,
        "name": "Machine Gun",
        "brittleness": 0.1
    },

    # Bullets
    "9mm": {
        "description": "A 9mm bullet, used for pistols.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 8.0,
        "percentage": 0.0,
        "name": "9mm Bullet",
        "brittleness": 0.0
    },
    "556": {
        "description": "A 5.56 bullet, used for rifles.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 64,
        "damage": 12.0,
        "percentage": 0.0,
        "name": "5.56 Bullet",
        "brittleness": 0.0
    },
    "shotgunshell": {
        "description": "A shotgun shell, used for shotguns.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 15,
        "damage": 16.0,
        "percentage": 0.0,
        "name": "Shotgun Shell",
        "brittleness": 0.0
    },
    "sniperbullet": {
        "description": "A sniper bullet, used for sniper rifles.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 20.0,
        "percentage": 0.0,
        "name": "Sniper Bullet",
        "brittleness": 0.0
    },
    "machinegunbullet": {
        "description": "A machine gun bullet, used for machine guns.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 64,
        "damage": 10.0,
        "percentage": 0.0,
        "name": "Machine Gun Bullet",
        "brittleness": 0.0
    },

    # Tools

    # Axes
    "woodaxe": {
        "description": "A wooden axe, very dull but it will do the job.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 3.0,
        "percentage": 1.0,
        "name": "Wooden Axe",
        "brittleness": 0.25
    },
    "stoneaxe": {
        "description": "A stone axe, sharper than a wooden axe but still not the best. Very cheap to make.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 4.0,
        "percentage": 1.0,
        "name": "Stone Axe",
        "brittleness": 0.2
    },
    "ironaxe": {
        "description": "An iron axe, sharp and deadly. Prone to rusting if not taken care of.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 5.0,
        "percentage": 1.0,
        "name": "Iron Axe",
        "brittleness": 0.15
    },
    "steelaxe": {
        "description": "A steel axe, sharp and deadly. Very durable.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 6.0,
        "percentage": 1.0,
        "name": "Steel Axe",
        "brittleness": 0.1
    },
    "copperaxe": {
        "description": "A copper axe, sharp however doesn't last long.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 4.5,
        "percentage": 1.0,
        "name": "Copper Axe",
        "brittleness": 0.6
    },
    "harditeaxe": {
        "description": "A hardite axe, sharp and durable. Hardite is a rare metal only found in volcanic areas.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 7.5,
        "percentage": 1.0,
        "name": "Hardite Axe",
        "brittleness": 0.025
    },

    # Pickaxes
    "woodpickaxe": {
        "description": "A wooden pickaxe, very dull but it will do the job.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 3.0,
        "percentage": 1.0,
        "name": "Wooden Pickaxe",
        "brittleness": 0.25
    },
    "stonepickaxe": {
        "description": "A stone pickaxe, sharper than a wooden pickaxe but still not the best. Very cheap to make.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 4.0,
        "percentage": 1.0,
        "name": "Stone Pickaxe",
        "brittleness": 0.2
    },
    "ironpickaxe": {
        "description": "An iron pickaxe, heavy work tool. Prone to rusting if not taken care of.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 5.0,
        "percentage": 1.0,
        "name": "Iron Pickaxe",
        "brittleness": 0.15
    },
    "steelpickaxe": {
        "description": "A steel pickaxe, sharp work tool. Very durable.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 6.0,
        "percentage": 1.0,
        "name": "Steel Pickaxe",
        "brittleness": 0.1
    },
    "copperpickaxe": {
        "description": "A copper pickaxe, sharp work tool however doesn't last long.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 4.5,
        "percentage": 1.0,
        "name": "Copper Pickaxe",
        "brittleness": 0.6
    },

    # Hammers
    "ironhammer": {
        "description": "An iron hammer, heavy work tool. Prone to rusting if not taken care of.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 5.0,
        "percentage": 1.0,
        "name": "Iron Hammer",
        "brittleness": 0.15
    },
    "steelhammer": {
        "description": "A steel hammer, sharp work tool. Very durable.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 6.0,
        "percentage": 1.0,
        "name": "Steel Hammer",
        "brittleness": 0.1
    },

    # Plows
    "woodplow": {
        "description": "A wooden plow, very dull but it will do the job.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 1.5,
        "percentage": 1.0,
        "name": "Wooden Plow",
        "brittleness": 0.25
    },
    "stoneplow": {
        "description": "A stone plow, sharper than a wooden plow but still not the best. Very cheap to make.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 2.5,
        "percentage": 1.0,
        "name": "Stone Plow",
        "brittleness": 0.2
    },
    "ironplow": {
        "description": "An iron plow, heavy work tool. Prone to rusting if not taken care of.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 3.5,
        "percentage": 1.0,
        "name": "Iron Plow",
        "brittleness": 0.15
    },
    "steelplow": {
        "description": "A steel plow, sharp work tool. Very durable.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 4.5,
        "percentage": 1.0,
        "name": "Steel Plow",
        "brittleness": 0.1
    },
    "copperplow": {
        "description": "A copper plow, sharp work tool however doesn't last long.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 3.0,
        "percentage": 1.0,
        "name": "Copper Plow",
        "brittleness": 0.6
    },

    # Shovels
    "woodshovel": {
        "description": "A wooden shovel, very dull but it will do the job.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 1.25,
        "percentage": 1.0,
        "name": "Wooden Shovel",
        "brittleness": 0.25
    },
    "stoneshovel": {
        "description": "A stone shovel, sharper than a wooden shovel but still not the best. Very cheap to make.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 2.25,
        "percentage": 1.0,
        "name": "Stone Shovel",
        "brittleness": 0.2
    },
    "ironshovel": {
        "description": "An iron shovel, heavy work tool. Prone to rusting if not taken care of.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 3.25,
        "percentage": 1.0,
        "name": "Iron Shovel",
        "brittleness": 0.15
    },
    "steelshovel": {
        "description": "A steel shovel, sharp work tool. Very durable.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 4.25,
        "percentage": 1.0,
        "name": "Steel Shovel",
        "brittleness": 0.1
    },
    "coppershovel": {
        "description": "A copper shovel, sharp work tool however doesn't last long.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 2.75,
        "percentage": 1.0,
        "name": "Copper Shovel",
        "brittleness": 0.6
    },

    # Power Tools
    "chainsaw": {
        "description": "A chainsaw, a powerful tool for cutting down trees. Very loud and very dangerous.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 8.0,
        "percentage": 1.0,
        "name": "Chainsaw",
        "brittleness": 0.05
    },
    "jackhammer": {
        "description": "A jackhammer, a powerful tool for breaking rocks. Very loud and very dangerous.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 8.0,
        "percentage": 1.0,
        "name": "Jackhammer",
        "brittleness": 0.05
    },
    "drill": {
        "description": "A drill, a powerful tool for drilling holes. Very loud and very dangerous.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 8.0,
        "percentage": 1.0,
        "name": "Drill",
        "brittleness": 0.05
    },

    # Misc
    "handmadetorch": {
        "description": "A hand made torch, a light source. Very useful in dark places. Does require fuel.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 0.0,
        "percentage": 1.0,
        "name": "Handmade Torch",
        "brittleness": 0.0
    },
    "flashlight": {
        "description": "A flashlight, a light source. Very useful in dark places. Does require batteries.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 0.0,
        "percentage": 1.0,
        "name": "Flashlight",
        "brittleness": 0.0
    },

        
    # Armour
    
    # Helmets
    "woodhelmet": {
        "description": "A wooden helmet, not comfortable but will protect your head.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Wooden Helmet",
        "brittleness": 0.25
    },

    "ironhelmet": {
        "description": "An iron helmet, heavy and uncomfortable but will protect your head.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Iron Helmet",
        "brittleness": 0.15
    },
    "secuirtyhelmet": {
        "description": "A security helmet, a modern helmet design. Very protective. Only found in abandoned structures.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Security Helmet",
        "brittleness": 0.05
    },
    "armyhelmet": {
        "description": "An army helmet, a military helmet design. Very protective. Only found in military bases.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Army Helmet",
        "brittleness": 0.025
    },
    "mechhelmet": {
        "description": "A mechanical helmet, a robotic helmet design. Very protective. Only found in robotic factories.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Mechanical Helmet",
        "brittleness": 0.01
    },

    # Chestplates
    "woodchestplate": {
        "description": "A wooden chestplate, not comfortable made from raw wood but will protect your chest.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 2,
        "percentage": 1.0,
        "name": "Wooden Chestplate",
        "brittleness": 0.25
    },
    "chainlinkchesplate": {
        "description": "An iron chestplate, heavy and uncomfortable but will protect your chest.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 2,
        "percentage": 1.0,
        "name": "Chain Chestplate",
        "brittleness": 0.15
    },
    "kevlarchestplate": {
        "description": "A kevlar chestplate, a modern chestplate design. Very protective. Only found in abandoned structures.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 2,
        "percentage": 1.0,
        "name": "Kevlar Chestplate",
        "brittleness": 0.05
    },
    "armychestplate": {
        "description": "An army chestplate, a military chestplate design. Very protective. Only found in military bases.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 2,
        "percentage": 1.0,
        "name": "Army Chestplate",
        "brittleness": 0.025
    },
    "mechchestplate": {
        "description": "A mechanical chestplate, a robotic chestplate design. Very protective. Only found in robotic factories.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 2,
        "percentage": 1.0,
        "name": "Mechanical Chestplate",
        "brittleness": 0.01
    },

    # Leggings
    "woodleggings": {
        "description": "Wooden leggings, not comfortable but will protect your legs.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Wooden Leggings",
        "brittleness": 0.25
    },
    "chainlinkleggings": {
        "description": "Iron leggings, heavy and uncomfortable but will protect your legs.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Chain Leggings",
        "brittleness": 0.15
    },
    "kevlarleggings": {
        "description": "Kevlar leggings, a modern leggings design. Very protective. Only found in abandoned structures.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Kevlar Leggings",
        "brittleness": 0.05
    },
    "armyleggings": {
        "description": "Army leggings, a military leggings design. Very protective. Only found in military bases.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Army Leggings",
        "brittleness": 0.025
    },
    "mechleggings": {
        "description": "Mechanical leggings, a robotic leggings design. Very protective. Only found in robotic factories.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Mechanical Leggings",
        "brittleness": 0.01
    },

    # Boots
    "sandals": {
        "description": "Sandals, not very protective but they will keep your feet of the ground.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Sandals",
        "brittleness": 0.25
    },
    "letherboots": {
        "description": "Leather boots, not very protective but they will keep your feet safe.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Leather Boots",
        "brittleness": 0.15
    },
    "steeltoeboots": {
        "description": "Steel toe boots, a modern boots design. Very protective. Only found in abandoned structures.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Steel Toe Boots",
        "brittleness": 0.05
    },
    "armyboots": {
        "description": "Army boots, a military boot design. Very protective. Only found in military bases.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Army Boots",
        "brittleness": 0.025
    },
    "mechboots": {
        "description": "Mechanical boots, a robotic boot design. Very protective. Only found in robotic factories.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 1,
        "percentage": 1.0,
        "name": "Mechanical Boots",
        "brittleness": 0.01
    },

    # Clothing

    # Hats
    "buckethat": {
        "description": "A bucket hat, a simple hat design. Not very protective but it will keep the sun out of your eyes.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Bucket Hat",
        "brittleness": 0.25
    },
    "beanie": {
        "description": "A beanie, a simple hat design. Not very protective but it will keep your head warm.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Beanie",
        "brittleness": 0.25
    },
    "cap": {
        "description": "A cap, a simple hat design. Not very protective but it will keep the sun out of your eyes.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Cap",
        "brittleness": 0.25
    },

    # Shirts
    "tshirt": {
        "description": "A t-shirt, a simple shirt design. Not very protective but it will keep you cool.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "T-Shirt",
        "brittleness": 0.25
    },
    "longsleeve": {
        "description": "A long sleeve shirt, a simple shirt design. Not very protective but it will keep you warm.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Long Sleeve",
        "brittleness": 0.25
    },
    "hoodie": {
        "description": "A hoodie, a simple shirt design. Not very protective but it will keep you warm.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Hoodie",
        "brittleness": 0.25
    },

    # Jackets
    "jacket": {
        "description": "A jacket, a simple jacket design. Not very protective but it will keep you warm.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Jacket",
        "brittleness": 0.25
    },
    "windbreaker": {
        "description": "A windbreaker, a simple jacket design. Not very protective but it will keep you warm.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Windbreaker",
        "brittleness": 0.25
    },
    "letherjacket": {
        "description": "A leather jacket, a simple jacket design. Not very protective but it will keep you warm.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Leather Jacket",
        "brittleness": 0.25
    },

    # Pants
    "jeans": {
        "description": "Jeans, a simple pants design. Not very protective but they will keep you warm.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Jeans",
        "brittleness": 0.25
    },
    "sweatpants": {
        "description": "Sweatpants, a simple pants design. Not very protective but they will keep you warm.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Sweatpants",
        "brittleness": 0.25
    },
    "shorts": {
        "description": "Shorts, a simple pants design. Not very protective but they will keep you cool.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Shorts",
        "brittleness": 0.25
    },

    # Shoes
    "sneakers": {
        "description": "Sneakers, a simple shoes design. Not very protective but they will keep your feet safe.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Sneakers",
        "brittleness": 0.25
    },
    "flipflops": {
        "description": "Flip flops, a simple shoes design. Not very protective but they will keep your feet cool.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.5,
        "percentage": 1.0,
        "name": "Flip Flops",
        "brittleness": 0.25
    },

    # Medical supplies

    # Bandages
    "bandage": {
        "description": "A bandage, used to heal small wounds.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Bandage",
        "brittleness": 0.0
    },
    "medkit": {
        "description": "A medkit, used to heal large wounds.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 8,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Medkit",
        "brittleness": 0.0
    },

    # Medicine
    "naturalmedicine": {
        "description": "Natural medicine, used to heal small wounds.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Natural Medicine",
        "brittleness": 0.0
    },
    "painkillers": {
        "description": "Painkillers, used to reduce pain and heal small wounds.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 8,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Painkillers",
        "brittleness": 0.0
    },
    "antirad": {
        "description": "Anti radiation pills, used to reduce radiation poisoning.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 8,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Anti Radiation Pills",
        "brittleness": 0.0
    },
    "stimpack": {
        "description": "Stimpack, used to heal large wounds and increase health for a short period of time.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 8,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Stimpack",
        "brittleness": 0.0
    },

    # Food

    # Fruits
    "apple": {
        "description": "An apple",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Apple",
    },
    "radioana": {
        "description": "A radioana, a rare fruit only found in the radioactive wastelands. Its effects are unknown.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Radioana",
    },
    "morange": {
        "description": "A morange, a rare fruit only found in the misty forests.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Morange",
    },
    "pomberry": {
        "description": "A pomberry, a common fruit found in the wastelands.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Pomberry",
    },
    "banapple": {
        "description": "A banapple, found commonly on the shores of the wastelands.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Banapple",
    },

    # Vegetables
    "misteriousroot": {
        "description": "A misterious root, a rare vegetable only found in the misty forests. Its effects are unknown.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Misterious Root",
    },
    "potato": {
        "description": "A potato, a common vegetable found in the wastelands.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Potato",
    },
    "bomroot": {
        "description": "A bomroot, a mutant vegetable from unknown origins.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Bomroot",
    },
    "carrot": {
        "description": "A carrot, a common vegetable found in the wastelands.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Carrot",
    },

    # Raw Meat
    "mysterymeat": {
        "description": "Mystery meat from unknon origins. Its effects are unknown.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Mystery Meat",
    },
    "rawmow": {
        "description": "Raw mow meat, a common meat found in the wastelands.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Raw Mow",
    },
    "rawplagoose": {
        "description": "Raw plagoose meat, a common meat found in the wastelands.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Raw Plagoose",
    },
    "rawbom": {
        "description": "Raw bom meat, a common meat found in the wastelands.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Raw Bom",
    },

    # Cooked Meat
    "mowsteak": {
        "description": "Mow steak, a common meat found in the wastelands.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Mow Steak",
    },
    "plagoose": {
        "description": "Plagoose, a common meat found in the wastelands.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Plagoose",
    },
    "bomsteak": {
        "description": "Bom steak, a common meat found in the wastelands.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Bom Steak",
    },
    "cookedmysterymeat": {
        "description": "Mystery meat from unknon origins. Its effects are unknown.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Cooked Mystery Meat",
    },

    # Grains
    "mutantwheat": {
        "description": "Mutant wheat, similar to normal wheat just a bit more radioactive.",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Mutant Wheat",
    },
    "mutantrice": {
        "description": "Mutant rice, similar to normal rice just a bit more radioactive.",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Mutant Rice",
    },
    "mutantcorn": {
        "description": "Mutant corn, similar to normal corn just a bit more radioactive.",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Mutant Corn",
    },

    # Grain Products
    "bread": {
        "description": "Bread, made from mutant wheat.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Bread",
    },
    "ricecake": {
        "description": "Rice cake, made from mutant rice.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Rice Cake",
    },
    "cornbread": {
        "description": "Corn bread, made from mutant corn.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 32,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Corn Bread",
    },
    "specialcake": {
        "description": "Special cake, made from the mutated grains and products of the wastelands, neatly presented with delicious frosting.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Special Cake",
    },

    # Drinks
    "waterbottle": {
        "description": "A water bottle, can be refilled at any water source. Beware of filling it comtaminated water.",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1,
        "damage": 0.0,
        "percentage": 1.0,
        "name": "Water Bottle",
    },
    "radiotapop": {
        "description": "Radioactive soda, a common beverage found in the wastelands.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Radiota-Pop",
    },
    "fruitjuice": {
        "description": "Fruit juice, made from the fruits of the wastelands.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Fruit Juice",
    },
    "Milch": {
        "description": "Milch, made from the wild mutated cows of the wastelands.",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 16,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Milch",
    },
    
    # Materials - Raw/Proccessed Meterials

    # Wood
    "woodlog": {
        "description": "A wooden log",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Log",
    },
    "woodplank": {
        "description": "A wooden plank",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Plank",
    },
    "stick": {
        "description": "A stick",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Stick",
    },
    "twig": {
        "description": "A twig",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Twig",
    },

    # Stone
    "stone": {
        "description": "A stone",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Stone",
    },
    "rock": {
        "description": "A rock",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 1.25,
        "percentage": 0.0,
        "name": "Rock",
    },
    # Iron/Steel
    "rawiron": {
        "description": "Raw iron",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 1.0,
        "name": "Raw Iron",
    },
    "ironingot": {
        "description": "An iron ingot",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Iron Ingot",
    },
    "ironnugget": {
        "description": "An iron nugget",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Iron Nugget",
    },
    "ironrod": {
        "description": "An iron rod",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Iron Rod",
    },
    "steelbar": {
        "description": "A steel bar",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Steel Bar",
    },
    "steelrod": {
        "description": "A steel rod",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Steel Rod",
    },
    "steelplate": {
        "description": "A steel plate",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Steel Plate",
    },

    # Copper
    "rawcopper": {
        "description": "Raw copper",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 1.0,
        "name": "Raw Copper",
    },
    "copperingot": {
        "description": "A copper ingot",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Copper Ingot",
    },
    "copperwire": {
        "description": "Copper wire",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Copper Wire",
    },
    "copperrod": {
        "description": "A copper rod",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Copper Rod",
    },

    # Hardite
    "rawhardite": {
        "description": "Raw hardite",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Raw Hardite",
    },
    "harditeingot": {
        "description": "A hardite ingot",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Hardite Ingot",
    },
    "harditerod": {
        "description": "A hardite rod",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64
    },
    "harditeplate": {
        "description": "A hardite plate",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Hardite Plate",
    },

    # Aluminium
    "rawaluminium": {
        "description": "Raw aluminium",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 1.0,
        "name": "Raw Aluminium",
    },
    "aluminiumingot": {
        "description": "An aluminium ingot",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Aluminium Ingot",
    },
    "aluminiumrod": {
        "description": "An aluminium rod",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Aluminium Rod",
    },
    "aluminiumplate": {
        "description": "An aluminium plate",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Aluminium Plate",
    },
    "aluminiumwire": {
        "description": "An aluminium wire",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Aluminium Wire",
    },

    # Titanium
    "rawtitanium": {
        "description": "Raw titanium",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 1.0,
        "name": "Raw Titanium",
    },
    "titaniumingot": {
        "description": "A titanium ingot",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Titanium Ingot",
    },
    "titaniumrod": {
        "description": "A titanium rod",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Titanium Rod",
    },
    "titaniumplate": {
        "description": "A titanium plate",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Titanium Plate",
    },


    # Scrap
    "scrapcircuit": {
        "description": "A scrap circuit",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Scrap Circuit",
    },
    "scrapbattery": {
        "description": "A scrap battery",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Scrap Battery",
    },
    "scrapmetal": {
        "description": "Scrap metal",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Scrap Metal",
    },
    "scrapplastic": {
        "name": "Used Plastic",
        "description": "Scrap plastic",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
    },

    # Electronics
    "circuitboard": {
        "description": "A circuit board used to make electronic devices.",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Circuit Board",
    },
    "microchip": {
        "description": "A microchip used to make circuit boards.",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Microchip",
    },
    "battery": {
        "description": "A battery used to power electronic devices.",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Battery",
    },

    # Fuel
    "biofuel": {
        "description": "Biofuel, used to power vehicles and generators. Can be made from organic materials.",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Biofuel",
    },
    "gasoline": {
        "description": "Gasoline, used to power vehicles and generators. Only found in fuel stations.",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Gasoline",
    },
    "diesel": {
        "description": "Diesel, used to power vehicles and generators. Only found in fuel stations.",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Diesel",
    },
    "jetfuel": {
        "description": "Jet fuel, used to power aircraft and other devices. Only found in the abandoned airfields.",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Jet Fuel",
    },
    "charcoal": {
        "description": "Charcoal, used to power smelters and other devices. Can be made from wood.",
        "isStackable": True,
        "isUsable": False,
        "maxQuantity": 64,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Charcoal",
    },

    # Crafting/Smelting
    "craftingbench": {
        "description": "A crafting bench used to craft items.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Crafting Bench",
    },
    "scrapbbq": {
        "description": "A scrap BBQ used to cook food.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Scrap BBQ",
    },
    "smelter": {
        "description": "A smelter used to smelt metals.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Smelter",
    },
    "workbench": {
        "description": "A workbench used to craft higher tiered tools and items.",
        "isStackable": False,
        "isUsable": False,
        "maxQuantity": 1,
        "damage": 0.0,
        "percentage": 0.0,
        "name": "Workbench",
    },
}