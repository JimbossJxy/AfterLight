"""
Author Block
Author: James Collum
Date Creation: 29/05/2024
Document Name: variables.py
Purpose of Document: This document will be used to store all global variables for the game.

"""

loadGame = {"inventory": "test"}

inventory = {
        "hotbar": {
            "position1": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                "isEquipped": True,
                'maxQuantity': 1
            },
            "position2": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                "isEquipped": False,
                'maxQuantity': 1
            },
            "position3": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                "isEquipped": False,
                'maxQuantity': 1
            },
            "position4": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                "isEquipped": False,
                'maxQuantity': 1
            },
            "position5": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                "isEquipped": False,
                'maxQuantity': 1
            },
            "position6": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                "isEquipped": False,
                'maxQuantity': 1
            },
            "position7": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                "isEquipped": False,
                'maxQuantity': 1
            }
        },
        "row1": {
            "position1": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position2": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position3": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position4": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position5": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position6": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position7": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            }
            
        },
        "row2": {
            "position1": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position2": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position3": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position4": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position5": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position6": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position7": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            }
        },
        "row3": {
            "position1": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position2": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position3": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position4": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position5": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position6": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            },
            "position7": {
                "item": "empty",
                "quantity": 0,
                "description": "",
                "isStackable": False,
                "isUsable": False,
                'maxQuantity': 1
            }
        }
    }

items = {
    # Weapons
    "sword": {
        "description": "A sword",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1
    },
    "bow": {
        "description": "A bow",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1
    },
    "arrow": {
        "description": "An arrow",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 64
    },
    # Food
    "apple": {
        "description": "An apple",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 64
    },
    "bread": {
        "description": "Bread",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 64
    },
    # Tools
    "pickaxe": {
        "description": "A pickaxe",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1
    },
    "axe": {
        "description": "An axe",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1
    },
    "shovel": {
        "description": "A shovel",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1
    },
    # Armour
    "helmet": {
        "description": "A helmet",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1
    },
    "chestplate": {
        "description": "A chestplate",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1
    },
    "leggings": {
        "description": "Leggings",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1
    },
    "boots": {
        "description": "Boots",
        "isStackable": False,
        "isUsable": True,
        "maxQuantity": 1
    },
    # Misc
    "torch": {
        "description": "A torch",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 1
    },
    "batteries" : {
        "description": "Batteries",
        "isStackable": True,
        "isUsable": True,
        "maxQuantity": 64
    }
}