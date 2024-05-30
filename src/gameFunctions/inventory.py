"""
Author Block
Author: James Collum
Date Creation: 28/05/2024
Document Name: inventory.py
Purpose of Document: This document will be used to handle the players inventory in the game.
Referenced Code:



"""

import configparser
import logging
import util
import os
import pathlib
import pickle
import sys
import shutil
from src import variables
from util.misc import misc
from pathlib import Path
from tempfile import TemporaryDirectory, mkdtemp
from logging.handlers import RotatingFileHandler

class inventory:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = RotatingFileHandler(str(Path.home() / "Documents" / "Afterlight" / "Logs" / "inventory.log"), maxBytes=100000, backupCount=5)
        self.logger.addHandler(self.handler)
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
    
    def loadInventory(self, inventory):
        """
        Loads the players inventory from a load game variable to the inventory variable

        Only to be run on game load not new game or save game
        """
        required_keys = {"item", "quantity", "description", "isStackable", "isUsable", "maxQuantity"}
        hotbar_keys = required_keys | {"isEquipped"}  # Additional key for hotbar positions
        try:
            # Iterate through the main categories in the inventory
            for category, positions in inventory.items():
                for position, data in positions.items():
                    # Check if we are in the hotbar category
                    if category == "hotbar":
                        if not hotbar_keys.issubset(data.keys()):
                            logging.warning(f"Missing keys in hotbar position {position}")
                            logging.info("Inventory will be reset to default values")
                    else:
                        if not required_keys.issubset(data.keys()):
                            logging.warning(f"Missing keys in {category} position {position}")
                            logging.info("Inventory will be reset to default values")
        
        except AttributeError:
            logging.error("Inventory is not a dictionary")
            logging.info("Creating a new inventory")
    
    def modifyInventory(self, inventory, item, quantity, position, description, isStackable, isUsable, maxQuantity, isEquipped=False):
        """
        Modifies the players inventory

        inventory: The players inventory
        item: The item to be added to the inventory
        quantity: The quantity of the item to be added
        position: The position in the inventory to add the item
        stackable: Whether the item is stackable or not
        description: The description of the item
        isUsable: Whether the item is usable or not
        maxQuantity: The maximum quantity of the item that can be held in the inventory
        is stackable: Whether the item is stackable or not
        isEquipped: Whether the item is equipped or not - only for hotbar items

        It will also check if the there is already an item in the inventory at the specified position if there is it will check if it is the same item, if it is equal to the max quantity of the item and if it is stackable.
        if it is not at the max quantity it will add the quantity to the existing item. If it is at the max quantity or not stackable it will switch the item in the inventory with the that is being held by the mouse cursor.

        """
        try:
            # Check if the item is already in the inventory
            if inventory[position]["item"] == item:
                # Check if the item is stackable
                if inventory[position]["isStackable"]:
                    # Check if the item is at the max quantity
                    if inventory[position]["quantity"] < inventory[position]["maxQuantity"]:
                        # Add the quantity to the item
                        inventory[position]["quantity"] += quantity
                    else:
                        # Switch the item in the inventory with the item in the mouse cursor
                        inventory[position]["item"] = item
                        inventory[position]["quantity"] = quantity
                        inventory[position]["description"] = description
                        inventory[position]["isStackable"] = isStackable
                        inventory[position]["isUsable"] = isUsable
                        inventory[position]["maxQuantity"] = maxQuantity
                else:
                    # Switch the item in the inventory with the item in the mouse cursor
                    inventory[position]["item"] = item
                    inventory[position]["quantity"] = quantity
                    inventory[position]["description"] = description
                    inventory[position]["isStackable"] = isStackable
                    inventory[position]["isUsable"] = isUsable
                    inventory[position]["maxQuantity"] = maxQuantity
            else:
                # Switch the item in the inventory with the item in the mouse cursor
                inventory[position]["item"] = item
                inventory[position]["quantity"] = quantity
                inventory[position]["description"] = description
                inventory[position]["isStackable"] = isStackable
                inventory[position]["isUsable"] = isUsable
                inventory[position]["maxQuantity"] = maxQuantity
        except KeyError:
            logging.error("Invalid position in inventory")
            logging.info("Item will not be added to the inventory")


    def pickupItem(self, item, amount):
        """
        Adds an item to the players inventory

        item: The item to be added to the inventory - it will search through a dictionary of items to add the item description, stackability, usability and max quantity
        amount: The quantity of the item to be added to the inventory
        """
        
        


       


        