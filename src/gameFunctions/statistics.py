"""
Author Block
Author: James Collum
Date Creation: 01/06/2024
Document Name: statistics.py
Purpose of Document: This document will be used to generate statistics and modify for the game.
References: None
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import configparser
import logging
import shutil
from src.util.misc import misc
from pathlib import Path
from tempfile import TemporaryDirectory, mkdtemp
from xml.etree import ElementTree 


class statistics:
    def __init__(self):
        # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logger = logging.getLogger(__name__)

        # Other Objects - These are objects that are used by the class

        self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
        self.statsPath = str(Path.home() / "Documents" / "Afterlight" / "Statistics")
        self.totalStatsPath = str(Path.home() / "Documents" / "Afterlight" / "Statistics" / "totalGameStatistics.xml")
        self.keysPressed = ["W", "A", "S", "D", "E", "Q", "Space", "Shift", "Ctrl", "1", "2", "3", "4", "5", "6", "7"]
        self.statList =[
            "totalSpawns",
            "totalDeaths",
            "totalKills",
            "totalDamageDealt",
            "totalDamageTaken",
            "totalDamageHealed",
            "totalDamageBlocked",
            "totalExperienceGained",
            "totalDistanceTravelled",
            "totalItemsCrafted",
            "totalItemsGathered",
            "totalItemsDropped",
            "totalItemsPickedUp",
            "totalItemsSold",
            "totalItemsBought",
            "totalItemsTraded",
            "totalItemsDestroyed",
            "totalItemsStored",
            "totalItemsRetrieved",
            "totalItemsEquipped",
            "totalItemsUnequipped",
            "totalItemsUsed",
            "totalItemsConsumed",
            "totalItemsCooked",
            "totalItemsCrafted",
            "totalItemsRepaired"
        ]
    
    def generateTotalStatistics(self): # Needs to be Modified to include all creature types once they are implemented
        """
        Generates xml statistics file in the statistics folder. Will be a total of all save statistics.
        """
        _root = ElementTree.Element("totalGameStatistics")
        _totalHostilesKilled = ElementTree.SubElement(_root, "totalHostilesKilled")
        _totalInteractiveKilled = ElementTree.SubElement(_root, "totalNPCsKilled")
        _totalPassiveKilled = ElementTree.SubElement(_root, "totalFriendlyKilled")
        _totalDamageDealt = ElementTree.SubElement(_root, "totalDamageDealt")
        _totalKeysPressed = ElementTree.SubElement(_root, "totalKeysPressed")

        # Total Amount of Saves
        ElementTree.SubElement(_root, "totalSaves").text = "0"

        # Total Ingame Statistics
        ElementTree.SubElement(_root, "hoursPlayed").text = "0"

        for _statName in self.statList:
            ElementTree.SubElement(_root, _statName).text = "0"


        # Specific Statistics
        
        # Hostiles Killed
        ElementTree.SubElement(_totalHostilesKilled, "totalHostilesKilled").text = "0"

        # NPCs Killed
        ElementTree.SubElement(_totalInteractiveKilled, "totalNPCsKilled").text = "0"

        # Friendly Killed
        ElementTree.SubElement(_totalPassiveKilled, "totalFriendlyKilled").text = "0"

        # Damage Dealt
        ElementTree.SubElement(_totalDamageDealt, "totalDamageDealtToAnimals").text = "0"

        # Keys Pressed
        ElementTree.SubElement(_totalKeysPressed, "totalKeysPressed").text = "0"
        for _key in self.keysPressed:
            ElementTree.SubElement(_totalKeysPressed, f"total{_key}Pressed").text = "0"
        

        # Write to File
        _tree = ElementTree.ElementTree(_root)
        self.logger.info("Writing Total Statistics File")
        try:
            _tree.write(self.totalStatsPath)
            self.logger.info("Total Statistics File Written Successfully")
        except Exception as e:
            self.logger.error(f"Error Writing Total Statistics File: {e}")
            self.errorPopup(f"Error Writing Total Statistics File: {e}")
            raise Exception(f"Error Writing Total Statistics File: {e}")

    def generateSaveStatistics(self, saveName): # Only to be used when a new save is created or if missing statistics file
        """
        Generates xml statistics file for each save in the statistics folder.
        """
        _root = ElementTree.Element("totalGameStatistics")
        _totalHostilesKilled = ElementTree.SubElement(_root, "totalHostilesKilled")
        _totalInteractiveKilled = ElementTree.SubElement(_root, "totalNPCsKilled")
        _totalPassiveKilled = ElementTree.SubElement(_root, "totalFriendlyKilled")
        _totalDamageDealt = ElementTree.SubElement(_root, "totalDamageDealt")
        _totalKeysPressed = ElementTree.SubElement(_root, "totalKeysPressed")


        # Total Ingame Statistics
        ElementTree.SubElement(_root, "hoursPlayed").text = "0"

        for _statName in self.statList:
            ElementTree.SubElement(_root, _statName).text = "0"


        # Specific Statistics
        
        # Hostiles Killed
        ElementTree.SubElement(_totalHostilesKilled, "totalHostilesKilled").text = "0"

        # NPCs Killed
        ElementTree.SubElement(_totalInteractiveKilled, "totalNPCsKilled").text = "0"

        # Friendly Killed
        ElementTree.SubElement(_totalPassiveKilled, "totalFriendlyKilled").text = "0"

        # Damage Dealt
        ElementTree.SubElement(_totalDamageDealt, "totalDamageDealtToAnimals").text = "0"

        # Keys Pressed
        ElementTree.SubElement(_totalKeysPressed, "totalKeysPressed").text = "0"
        for _key in self.keysPressed:
            ElementTree.SubElement(_totalKeysPressed, f"total{_key}Pressed").text = "0"
        
        # Write to File
        _tree = ElementTree.ElementTree(_root)
        _tree.write(f"{saveName}.xml")

    def updateTotalStatistics(self, data=None):
        """
        Updates the total statistics file from when the other statistics files are updated.
        """
        
        # reads data variable and for each key in the data variable, updates the total statistics file. It will add the value of the key to the value of the key in the total statistics file.
        # If the key does not exist in the total statistics file, it will create the key and set the value to the value of the key in the data variable.
        # If the key does not exist in the data variable, it will set the value added to the key in the total statistics file to 0.

        if data is None:
            self.errorPopup("No Data to Update Total Statistics")
            self.logger.error("No Data to Update Total Statistics")
            raise Exception("No Data to Update Total Statistics")
        elif not isinstance(data, dict):
            self.errorPopup("Data is not a Dictionary")
            self.logger.error("Data is not a Dictionary")
            raise Exception("Data is not a Dictionary")
        
        # data is a dictionary
        # The data is the current data from that session of play
        # variable will be read to check if the keys in stat list, keysPressed, and specific statistics are in the data variable
        # If they are not, they will be added to the data variable and set to 0

        for _statName in self.statList:
            if _statName not in data:
                data[_statName] = 0
                self.logger.info(f"{_statName} not in Data")
        
        for _key in self.keysPressed:
            if f"total{_key}Pressed" not in data:
                data[f"total{_key}Pressed"] = 0
                self.logger.info(f"Total {_key} Pressed not in Data")
        
        if "totalHostilesKilled" not in data:
            data["totalHostilesKilled"] = 0
            self.logger.info("Total Hostiles Killed not in Data")
        
        if "totalNPCsKilled" not in data:
            data["totalNPCsKilled"] = 0
            self.logger.info("Total NPCs Killed not in Data")
        
        if "totalFriendlyKilled" not in data:
            data["totalFriendlyKilled"] = 0
            self.logger.info("Total Friendly Killed not in Data")

        
        if "totalDamageDealtToAnimals" not in data:
            data["totalDamageDealtToAnimals"] = 0
            self.logger.info("Total Damage Dealt to Animals not in Data")
        
        if "totalKeysPressed" not in data:
            data["totalKeysPressed"] = 0
            self.logger.info("Total Keys Pressed not in Data")
        

        try:
            # For each key in the data variable, add the value to the value of the key in the total statistics file.
            for _key in data:
                _tree = ElementTree.parse(self.totalStatsPath)
                _root = _tree.getroot()
                for _element in _root.iter():
                    if _element.tag == _key:
                        _element.text = str(int(_element.text) + int(data[_key]))
                        self.logger.info(f"Updated {_key} in Total Statistics")
                
            _tree.write(self.totalStatsPath)
            self.logger.info("Total Statistics Updated Successfully")
        
        except Exception as e:
            self.logger.error(f"Error Updating Total Statistics: {e}")
            self.errorPopup(f"Error Updating Total Statistics: {e}")
            raise Exception(f"Error Updating Total Statistics: {e}")

        
    def updateSaveStatistics(self, saveName, data=None):
        """
        Updates the save statistics file from when the other statistics files are updated.
        """
        _savePath = str(Path.home() / "Documents" / "Afterlight" / "Statistics" / f"{saveName}.xml")
        # Checks if the data variable is None or not a dictionary
        if data is None:
            self.errorPopup("No Data to Update Total Statistics")
            self.logger.error("No Data to Update Total Statistics")
            raise Exception("No Data to Update Total Statistics")
        elif not isinstance(data, dict):
            self.errorPopup("Data is not a Dictionary")
            self.logger.error("Data is not a Dictionary")
            raise Exception("Data is not a Dictionary")
        
        for _statName in self.statList:
            if _statName not in data:
                data[_statName] = 0
                self.logger.info(f"{_statName} not in Data")
        
        for _key in self.keysPressed:
            if f"total{_key}Pressed" not in data:
                data[f"total{_key}Pressed"] = 0
                self.logger.info(f"Total {_key} Pressed not in Data")
        
        if "totalHostilesKilled" not in data:
            data["totalHostilesKilled"] = 0
            self.logger.info("Total Hostiles Killed not in Data")
        
        if "totalNPCsKilled" not in data:
            data["totalNPCsKilled"] = 0
            self.logger.info("Total NPCs Killed not in Data")
        
        if "totalFriendlyKilled" not in data:
            data["totalFriendlyKilled"] = 0
            self.logger.info("Total Friendly Killed not in Data")

        
        if "totalDamageDealtToAnimals" not in data:
            data["totalDamageDealtToAnimals"] = 0
            self.logger.info("Total Damage Dealt to Animals not in Data")
        
        if "totalKeysPressed" not in data:
            data["totalKeysPressed"] = 0
            self.logger.info("Total Keys Pressed not in Data")

        try:
            # For each key in the data variable, add the value to the value of the key in the save statistics file.
            for _key in data:
                _tree = ElementTree.parse(f"{saveName}.xml")
                _root = _tree.getroot()
                for _element in _root.iter():
                    if _element.tag == _key:
                        _element.text = str(int(_element.text) + int(data[_key]))
                        self.logger.info(f"Updated {_key} in Save Statistics")
                
            _tree.write(_savePath)
            self.logger.info("Save Statistics Updated Successfully")
        
        except Exception as e:
            self.logger.error(f"Error Updating Save Statistics: {e}")
            self.errorPopup(f"Error Updating Save Statistics: {e}")
            raise Exception(f"Error Updating Save Statistics: {e}")
        

if __name__ == "__main__":
    _stat = statistics()
    _stat.generateTotalStatistics()
    _stat.generateSaveStatistics("test")
    _stat.updateTotalStatistics({"totalSpawns": 1, "totalDeaths": 1, "totalKills": 1, "totalDamageDealt": 1, "totalDamageTaken": 1, "totalDamageHealed": 1, "totalDamageBlocked": 1, "totalExperienceGained": 1, "totalDistanceTravelled": 1, "totalItemsCrafted": 1, "totalItemsGathered": 1, "totalItemsDropped": 1, "totalItemsPickedUp": 1, "totalItemsSold": 1, "totalItemsBought": 1, "totalItemsTraded": 1, "totalItemsDestroyed": 1, "totalItemsStored": 1, "totalItemsRetrieved": 1, "totalItemsEquipped": 1, "totalItemsUnequipped": 1, "totalItemsUsed": 1, "totalItemsConsumed": 1, "totalItemsCooked": 1, "totalItemsCrafted": 1, "totalItemsRepaired": 1})
    _stat.updateSaveStatistics("test", {"totalSpawns": 1, "totalDeaths": 1, "totalKills": 1, "totalDamageDealt": 1, "totalDamageTaken": 1, "totalDamageHealed": 1, "totalDamageBlocked": 1, "totalExperienceGained": 1, "totalDistanceTravelled": 1, "totalItemsCrafted": 1, "totalItemsGathered": 1, "totalItemsDropped": 1, "totalItemsPickedUp": 1, "totalItemsSold": 1, "totalItemsBought": 1, "totalItemsTraded": 1, "totalItemsDestroyed": 1, "totalItemsStored": 1, "totalItemsRetrieved": 1, "totalItemsEquipped": 1, "totalItemsUnequipped": 1, "totalItemsUsed": 1, "totalItemsConsumed": 1, "totalItemsCooked": 1, "totalItemsCrafted": 1, "totalItemsRepaired": 1})
    _stat.updateTotalStatistics({"totalSpawns": 1, "totalDeaths": 1, "totalKills": 1, "totalDamageDealt": 1, "totalDamageTaken": 1, "totalDamageHealed": 1, "totalDamageBlocked": 1, "totalExperienceGained": 1, "totalDistanceTravelled": 1, "totalItemsCrafted": 1, "totalItemsGathered": 1, "totalItemsDropped": 1, "totalItemsPickedUp": 1, "totalItemsSold": 1, "totalItemsBought": 1, "totalItemsTraded": 1, "totalItemsDestroyed": 1, "totalItemsStored": 1, "totalItemsRetrieved": 1, "totalItemsEquipped": 1, "totalItemsUnequipped": 1, "totalItemsUsed": 1, "totalItemsConsumed": 1, "totalItemsCooked": 1, "totalItemsCrafted": 1, "totalItemsRepaired": 1})

    

        

        
        

        