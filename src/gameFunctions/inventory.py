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
        self.listener = None
        self.takenSlots = 0
        self.itemList = variables.items
        
    
    def loadInventory(self, inventory):
        """
        Loads the players inventory from a load game variable to the inventory variable

        Only to be run on game load not new game or save game
        """
        _requiredKeys = {"item", "quantity", "description", "isStackable", "isUsable", "maxQuantity", "damage", "name", "brittleness", "percentage"}
        _hotbarKeys = _requiredKeys | {"isEquipped"}  # Additional key for hotbar positions
        try:
            # Iterate through the main categories in the inventory
            for category, _positions in inventory.items():
                for position, data in _positions.items():
                    # Check if we are in the hotbar category
                    if category == "hotbar":
                        if not _hotbarKeys.issubset(data.keys()):
                            logging.warning(f"Missing keys in hotbar position {position}")
                            logging.info("Inventory will be reset to default values")
                    else:
                        if not _requiredKeys.issubset(data.keys()):
                            logging.warning(f"Missing keys in {category} position {position}")
                            logging.info("Inventory will be reset to default values")
        
        except AttributeError:
            logging.error("Inventory is not a dictionary")
            logging.info("Creating a new inventory")

    # Listener for inventory changes - Will be used to update the inventory in the GUI
    def notifyInventory(self):
        """
        Notifies the GUI of any inventory changes
        """
        if self.listener is None:
            logging.error("No listener set")
            logging.info("Inventory will not be updated in the GUI")
            return
        
        try:
            self.listener.refresh() # Refresh the GUI - Needs to be implemented in the GUI
            logging.info("Inventory updated in the GUI")
        except TypeError as e:
            logging.error(f"Error updating inventory in the GUI: {e}")
            logging.info("Inventory will not be updated in the GUI")

    # Updates Existing Stack - Will be used for stacking items in the inventory
    def updateExistingStack(self, item, quantity):
        """
        Updates an existing stack of an item in the inventory
        """
        logging.info(f"Updating existing stack of {item} with {quantity}")
        _itemData = self.itemList[item]
        _maxQuantity = _itemData['maxQuantity']
        _remainingQuantity = quantity
        
        for _category, _positions in variables.inventory.items():
            for _position, _data in _positions.items():
                if _remainingQuantity <= 0:
                    return _remainingQuantity
                if _data["item"] == item:
                    _availableSpace = _maxQuantity - _data["quantity"]
                    if _availableSpace > 0:
                        _addQuantity = min(_remainingQuantity, _availableSpace)
                        _data["quantity"] += _addQuantity
                        _remainingQuantity -= _addQuantity
                        logging.info(f"Added {_addQuantity} '{item}' to {_category} {_position}, new quantity: {_data['quantity']}.")
                       # self.notify_listeners('update', item, _addQuantity)
        return _remainingQuantity
    
    # Adds a new stack of an item to the inventory - Will be used for stacking items in the inventory
    def addNewStack(self, item, quantity):
        """
        Adds a new stack of an item to the inventory
        """
        logging.info(f"Adding new stack of {item} with {quantity}")
        _itemData = self.itemList[item]
        _maxQuantity = _itemData['maxQuantity']
        _remainingQuantity = quantity
        
        for _category, _positions in variables.inventory.items():
            for _position, _data in _positions.items():
                if _remainingQuantity <= 0:
                    return _remainingQuantity
                if _data["item"] == "empty":
                    _addQuantity = min(_remainingQuantity, _maxQuantity)
                    _data["item"] = item
                    _data["quantity"] = _addQuantity
                    _remainingQuantity -= _addQuantity
                    logging.info(f"Added {_addQuantity} '{item}' to {_category} {_position}.")
                   # self.notify_listeners('add', item, _addQuantity)
        return _remainingQuantity
    
    # Attempts to add an item to the inventory - Will be used for picking up items/buying items/looting items/etc
    def addItem(self, item, quantity):
        """
        Adds an item to the players inventory

        item: The item to be added to the inventory - it will search through a dictionary of items to add the item description, stackability, usability and max quantity
        quantity: The quantity of the item to be added to the inventory - it will check if the item is stackable and if it is at the max quantity

        It will check through the whole inventory to find the item. If the item exists it will check if the quantity of that stack is less than the max quantity of the item, if it is it will add the quantity to the stack. If the item does not exist it will check for an empty slot in the inventory and add the item to that slot.
        It will check if there is a free slot from row 3 position 1 then row 3 position 2 etc to put the item in. If there are no free slots available return 3 for no free slots available.
        """
        logging.info(f"Adding {quantity} '{item}' to the inventory.")
        if item not in self.itemList:
            logging.error(f"Item '{item}' not found in items dictionary.")
            return 1  # Item not found in items dictionary

        # Update existing stacks
        _remainingQuantity = self.updateExistingStack(item, quantity)
        logging.info(f"Remaining quantity after updating existing stacks: {_remainingQuantity}")

        # Add new stacks
        _remainingQuantity = self.addNewStack(item, _remainingQuantity)
        logging.info(f"Remaining quantity after adding new stacks: {_remainingQuantity}")
        
        if _remainingQuantity > 0:
            logging.info(f"No free slots available to add '{item}'.")
            return 3  # No free slots available

        logging.info(f"Added '{item}' to the inventory successfully.")
        # self.notify_listeners('add_item', item, quantity - remaining_quantity) - Needs to be implemented in the GUI
        return 0  # Success
        
    # Remove Stack - Will be used for dropping items/using items/trading items/etc
    def removeStack(self, category, position, item, quantity):
        logging.info(f"Removing {quantity} '{item}' from the inventory.")   
        _emptyItem = {
            "item": "empty",
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
        
        _data = variables.inventory[category][position]
        if _data["item"] == item:
            if _data["quantity"] <= quantity:
                quantity = _data["quantity"]
                variables.inventory[category][position] = _emptyItem.copy()
                variables.inventory[category][position]["quantity"] = 0
            else:
                _data["quantity"] -= quantity

            return quantity
        logging.info(f"Item '{item}' not found in the inventory.")
        return 1 # Error code for item not found in inventory 
    
    # Attempts to remove an item from the inventory - Will be used for dropping items/using items/trading items/etc
    def removeItem(self, item, quantity):
        """
        Removes an item from the players inventory

        item: The item to be removed from the inventory - Done by searching through the variables.py inventory dictionary for the item name
        quantity: The quantity of the item to be removed from the inventory - Done by checking the quantity of the item in the inventory dictionary if the item exists, if it is equal to the quantity to be removed it will remove the item from the inventory, if it is less than the quantity to be removed it will remove the item from the inventory (unless trading then wont remove item) and remove the remaining quantity from the quantity to be removed
        
        It will check through the whole inventory to find the item. If the item exists it will check if the quantity of that stack is equal to the quantity to be removed,
        if there are more than 1 stack of the item it will add the quantity of the other stacks to the total quantity of that item. Then it will check if the total quantity is equal to the quantity to be removed, if it is it will check the size of each of the stacks
        and remove the stack that is equal to the quantity to be removed. If the total quantity is more than a single stack it will remove the quantity from each stack until the quantity to be removed is 0. This will be done by removing from row 3 position 1 then row 3 position 2 etc for that item.

        """
        logging.info(f"Removing {quantity} '{item}' from the inventory.")
        _totalQuantity = 0
        _positionsUpdate = []

        # Traverse the inventory to calculate total quantity and positions
        for _category, _positions in variables.inventory.items():
            for position, data in _positions.items():
                if data["item"] == item:
                    _totalQuantity += data["quantity"]
                    _positionsUpdate.append((_category, position))

        # If the item doesn't exist in the inventory
        if _totalQuantity == 0:
            logging.info(f"Item '{item}' not found in the inventory.")
            print(f"Item '{item}' not found in the inventory.")
            return 1  # Error code for item not found in inventory

        # If quantity to be removed is more than available
        if quantity > _totalQuantity:
            logging.info(f"Cannot remove {quantity} '{item}' as only {_totalQuantity} available.")
            print(f"Cannot remove {quantity} '{item}' as only {_totalQuantity} available.")
            return 2, _totalQuantity  # Error code for insufficient quantity and return the total quantity available

        # Remove the items from inventory
        for _category, position in _positionsUpdate:
            if quantity <= 0:
                break  # If quantity is 0, break the loop
            _quantityRemoved = self.removeStack(_category, position, item, quantity)
            quantity -= _quantityRemoved  # Update the quantity to be removed

        logging.info(f"Removed {quantity} '{item}' from the inventory.")
        # self.notify_listeners('remove', item, quantity)
        return 0  # Success code for item removed
        

    # Checks if the player has an item in the inventory - Will be used for quests/achievements/etc
    def hasItem(self, item, quantity):
        """
        Checks if the player has the item in the inventory

        item: The item to be checked in the inventory - Done by searching through the variables.py inventory dictionary for the item name
        quantity: The quantity of the item to be checked in the inventory - Done by checking the quantity of the item in the inventory dictionary if the item exists
        
        Returns: True if the player has the item in the inventory, False if the player does not have the item in the inventory
        """
        logging.info(f"Checking if player has {quantity} {item}")
        for i in variables.inventory:
            if i["item"] == item:
                if i["quantity"] >= quantity:
                    logging.info(f"Player has {quantity} of {item}")
                    return True
        return False


    # Checks how many free slots are in the inventory - Will be used for picking up items/buying items/looting items/etc
    def freeSlots(self):
        """
        Checks how many free slots are in the players inventory - Done by checking how many "empty" Items are in the inventory variable from variables.py
        """
        logging.info("Checking how many free slots are in the inventory")
        _freeSlots = 0
        for category, positions in variables.inventory.items():
            for position, data in positions.items():
                if data["item"] == "empty":
                    _freeSlots += 1

        logging.info(f"Player has {_freeSlots} free slots in their inventory")
        return _freeSlots


    
    # Checks if the inventory is full - Will be used for picking up items/buying items/looting items/etc
    def isFull(self):
        """
        Checks if the players inventory is full - This is done by checking if the inventory variable from variables.py has no "empty" Items within it
        """
        logging.info("Checking if inventory is full")
        for category, positions in variables.inventory.items():
            for position, data in positions.items():
                if data["item"] == "empty":
                    logging.info("Inventory is not full")
                    return False
        logging.info("Inventory is full")
        return True
        