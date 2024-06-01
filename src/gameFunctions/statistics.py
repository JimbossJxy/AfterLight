"""
Author Block
Author: James Collum
Date Creation: 01/06/2024
Document Name: statistics.py
Purpose of Document: This document will be used to generate statistics and modify for the game.
References: None
"""

import configparser
import logging
import util
import os
import pathlib
import sys
import shutil
import xml
from util.misc import misc
from pathlib import Path
from tempfile import TemporaryDirectory, mkdtemp
from logging.handlers import RotatingFileHandler
from xml.etree import ElementTree 

class statistics:
    def __init__(self):
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.savePath = str(Path.home() / "Documents" / "Afterlight" / "Saves")
        self.statsPath = str(Path.home() / "Documents" / "Afterlight" / "Statistics")
        self.config = configparser.ConfigParser()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.handler = RotatingFileHandler(str(Path.home() / "Documents" / "Afterlight" / "Logs" / "game.log"), maxBytes=100000, backupCount=5)
        self.logger.addHandler(self.handler)
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
    
    def generateTotalStatistics(self): # Needs to be Modified to include all creature types once they are implemented
        """
        Generates xml statistics file in the statistics folder. Will be a total of all save statistics.
        """
        _root = ElementTree.Element("totalGameStatistics")
        _totalGameStatistics =ElementTree.SubElement(_root, "totalGameStatistics")
        _totalHostilesKilled = ElementTree.SubElement(_totalGameStatistics, "totalHostilesKilled")
        _totalInteractiveKilled = ElementTree.SubElement(_totalGameStatistics, "totalNPCsKilled")
        _totalPassiveKilled = ElementTree.SubElement(_totalGameStatistics, "totalFriendlyKilled")
        _totalDamageDealt = ElementTree.SubElement(_totalGameStatistics, "totalDamageDealt")
        _totalKeysPressed = ElementTree.SubElement(_totalGameStatistics, "totalKeysPressed")

        # Total Amount of Saves
        ElementTree.SubElement(_root, "totalSaves").text = "0"

        # Total Ingame Statistics
        ElementTree.SubElement(_totalGameStatistics, "hoursPlayed").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalSpawns").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalDeaths").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalKills").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalDamageDealt").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalDamageTaken").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalDamageHealed").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalDamageBlocked").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalExperienceGained").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalDistanceTravelled").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsCrafted").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsGathered").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsDropped").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsPickedUp").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsSold").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsBought").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsTraded").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsDestroyed").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsStored").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsRetrieved").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsEquipped").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsUnequipped").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsUsed").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsConsumed").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsCooked").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsCrafted").text = "0"
        ElementTree.SubElement(_totalGameStatistics, "totalItemsRepaired").text = "0"


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
        ElementTree.SubElement(_totalKeysPressed, "totalWPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalAPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalSPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalDPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalEPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalQPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalSpacePressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalShiftPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalCtrlPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total1Pressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total2Pressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total3Pressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total4Pressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total5Pressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total6Pressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total7Pressed").text = "0"
        

        # Write to File
        _tree = ElementTree.ElementTree(_root)
        _tree.write(os.path.join(self.statsPath, "totalGameStatistics.xml"))

    def generateSaveStatistics(self, saveName): # Only to be used when a new save is created or if missing statistics file
        """
        Generates xml statistics file for each save in the statistics folder.
        """
        _root = ElementTree.Element("saveGameStatistics")
        _saveGameStatistics = ElementTree.SubElement(_root, "saveGameStatistics")
        _totalHostilesKilled = ElementTree.SubElement(_saveGameStatistics, "totalHostilesKilled")
        _totalInteractiveKilled = ElementTree.SubElement(_saveGameStatistics, "totalNPCsKilled")
        _totalPassiveKilled = ElementTree.SubElement(_saveGameStatistics, "totalFriendlyKilled")
        _totalDamageDealt = ElementTree.SubElement(_saveGameStatistics, "totalDamageDealt")
        _totalKeysPressed = ElementTree.SubElement(_saveGameStatistics, "totalKeysPressed")

        # Total Ingame Statistics
        ElementTree.SubElement(_saveGameStatistics, "hoursPlayed").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalSpawns").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalDeaths").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalKills").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalDamageDealt").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalDamageTaken").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalDamageHealed").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalDamageBlocked").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalExperienceGained").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalDistanceTravelled").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsCrafted").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsGathered").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsDropped").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsPickedUp").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsSold").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsBought").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsTraded").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsDestroyed").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsStored").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsRetrieved").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsRetrieved").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsEquipped").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsUnequipped").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsUsed").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsConsumed").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsCooked").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsCrafted").text = "0"
        ElementTree.SubElement(_saveGameStatistics, "totalItemsRepaired").text = "0"


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
        ElementTree.SubElement(_totalKeysPressed, "totalWPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalAPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalSPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalDPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalEPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalQPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalSpacePressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalShiftPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "totalCtrlPressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total1Pressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total2Pressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total3Pressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total4Pressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total5Pressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total6Pressed").text = "0"
        ElementTree.SubElement(_totalKeysPressed, "total7Pressed").text = "0"

        # Write to File
        _tree = ElementTree.ElementTree(_root)
        _tree.write(os.path.join(self.statsPath, f"{saveName}.xml"))

    def updateTotalStatistics(self):
        """
        Updates the total statistics file with all the data from each save file. 
        It will iterate through each save file and add the data to the total statistics file.
        """
        

        
        

        