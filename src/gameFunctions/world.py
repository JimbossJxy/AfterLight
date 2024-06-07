"""
Author Block
Author: James Collum
Date Creation: 2/06/2024
Document Name: player.py
Purpose of Document: This document will be used to handle world generation and logic in the game.
Referenced Code:

"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import configparser
import h5py
import logging
import numpy
import pathlib
import pickle
import random
import subprocess
import shutil
import string

import zipfile
from datetime import datetime
from pathlib import Path
from src.util.misc import misc
from perlin_noise import PerlinNoise

# Constants
class biome:
    RADIOACTIVE_WASTELAND = "R"
    NORMAL_WASTELAND = "W"
    WASTELAND_SHORES = "S"
    PONDS = ["1", "2", "3", "4"]  # radioactive, salt, dirty, clean
    RIVERS = ["5", "6", "7", "8"]  # radioactive, salt, dirty, clean
    DESERTS = ["D", "d", "r"]  # normal, red, radioactive
    VOLCANIC = "V"
    FORESTS = ["F", "f", "T", "t", "M"]  # snowy, radioactive, dead, rain, misty
    SWAMPS = ["9", "A", "B"]  # radioactive, deep, shallow
    GRASSLANDS = "G"
    OCEANS = ["O", "C"]  # glowing, cold
    MOUNTAINS = "M"
    TECTONIC_PLATE = "X" # Represents the world border

class Block:
    # Grass blocks
    WILTED_GRASS = 'A'
    ALIVE_GRASS = 'B'
    LONG_GRASS = 'C'
    DEAD_GRASS = 'D'
    
    # Path blocks
    DIRT_PATH = 'E'
    PEBBLE_PATH = 'F'
    
    # Road blocks
    ASPHALT_ROAD = 'G'
    
    # Farmland blocks
    WET_FARMLAND = 'H'
    DRY_FARMLAND = 'I'
    SEEDED_FARMLAND = 'J'
    
    # Dirt blocks
    RADIOACTIVE_DIRT = 'K'
    NORMAL_DIRT = 'L'
    
    # Wood blocks
    LOGS = 'M'
    PLANKS = 'N'
    DOORS = 'O'
    
    # Ore encased in stone
    IRON_ORE = 'P'
    COPPER_ORE = 'Q'
    TITANIUM_ORE = 'R'
    HARDITE_ORE = 'S'
    ALUMINIUM_ORE = 'T'
    GOLD_ORE = 'U'
    
    # Structure blocks
    BBQ = 'V'
    SMELTER = 'W'
    CRAFTING_BENCH = 'X'
    WORKBENCH = 'Y'
    
    # Military base blocks
    FENCING = 'Z'
    CANVAS = 'a'
    BARRICADE = 'b'
    WATCHTOWER = 'c'
    AMMO_CRATE = 'd'
    SANDBAGS = 'e'
    
    # Robotic factory blocks
    ASSEMBLY_LINE_BELT = 'f'
    ROBOTIC_ARM = 'g'
    CONTROL_PANEL = 'h'
    CONVEYOR_BELT = 'i'
    FABRICATOR = 'j'
    STORAGE_UNIT = 'k'
    
    # Concrete blocks
    WALL = 'l'
    BOLLARD = 'm'
    BROKEN_WALL = 'n'
    FLOOR = 'o'
    COLUMN = 'p'
    STAIRS = 'q'
    PAVEMENT = 'r'
    
    # Radioactive wasteland blocks
    CRACKED_GROUND = 's'
    TOXIC_SLUDGE = 't'
    MUTATED_PLANT = 'u'
    RUINED_BUILDING = 'v'
    
    # Volcanic vent blocks
    HARDITE_DEPOSIT = 'w'
    LAVA_POOL = 'x'
    ASH_COVERED_ROCK = 'y'
    BASALT = 'z'
    MAGMA_CHAMBER = '0'
    
    # Makeshift shop and structure blocks
    WOOD_FENCING = '1'
    MAKESHIFT_ROOF = '2'
    WOODEN_COUNTER = '3'
    STORAGE_CRATE = '4'
    SIGNPOST = '5'
    TENT = '6'
    MARKET_STALL = '7'

# Define block variations within biomes
BLOCK_VARIATIONS = {
    'G': [Block.WILTED_GRASS, Block.ALIVE_GRASS, Block.LONG_GRASS, Block.DEAD_GRASS],  # Grass
    'P': [Block.DIRT_PATH, Block.PEBBLE_PATH],  # Path
    'R': [Block.ASPHALT_ROAD],  # Road
    'F': [Block.WET_FARMLAND, Block.DRY_FARMLAND, Block.SEEDED_FARMLAND],  # Farmland
    'D': [Block.RADIOACTIVE_DIRT, Block.NORMAL_DIRT],  # Dirt
    'W': [Block.LOGS, Block.PLANKS, Block.DOORS],  # Wood
    'O': [Block.IRON_ORE, Block.COPPER_ORE, Block.TITANIUM_ORE, Block.HARDITE_ORE, Block.ALUMINIUM_ORE, Block.GOLD_ORE],  # Ore encased in stone
    'S': [Block.BBQ, Block.SMELTER, Block.CRAFTING_BENCH, Block.WORKBENCH],  # Structures
    'M': [Block.FENCING, Block.CANVAS, Block.BARRICADE, Block.WATCHTOWER, Block.AMMO_CRATE, Block.SANDBAGS],  # Military base blocks
    'B': [Block.ASSEMBLY_LINE_BELT, Block.ROBOTIC_ARM, Block.CONTROL_PANEL, Block.CONVEYOR_BELT, Block.FABRICATOR, Block.STORAGE_UNIT],  # Robotic factory blocks
    'C': [Block.WALL, Block.BOLLARD, Block.BROKEN_WALL, Block.FLOOR, Block.COLUMN, Block.STAIRS, Block.PAVEMENT],  # Concrete
    'R': [Block.CRACKED_GROUND, Block.TOXIC_SLUDGE, Block.MUTATED_PLANT, Block.RUINED_BUILDING],  # Radioactive wasteland blocks
    'V': [Block.HARDITE_DEPOSIT, Block.LAVA_POOL, Block.ASH_COVERED_ROCK, Block.BASALT, Block.MAGMA_CHAMBER],  # Volcanic vents
    'H': [Block.WOOD_FENCING, Block.MAKESHIFT_ROOF, Block.WOODEN_COUNTER, Block.STORAGE_CRATE, Block.SIGNPOST, Block.TENT, Block.MARKET_STALL],  # Makeshift shops and structures
}


# Classes
class world:
    def __init__(self):
        # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logger = logging.getLogger(__name__)

        # Other Objects - These are objects that are used by the class
        
    def generateSeed(self, seed):
        """
        This function will generate a seed for the world based on the user input.
        """
        if seed:
            # Use user-provided seed
            self.seed = seed
        else:
            # Generate random seed
            self.seed = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 64)))
        
        # Use the generated seed for world generation logic
        # ...
        self.logger.info(f"Generated seed: {self.seed}")
        return self.seed
    

class worldChunkGenerator:
    def __init__(self, chunkX, chunkY, seed, biomeData=None, blockData=None):
        # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logger = logging.getLogger(__name__)

        # Other Objects - These are objects that are used by the class
        self.chunkX = chunkX
        self.chunkY = chunkY
        self.seed = seed
        self.biomeData = biomeData if biomeData is not None else self.generateBiomeChunk()
        self.blockData = blockData if blockData is not None else self.generateBlockChunk()

        # Chunk limits
        self.chunkSize = 16
        self.worldSize = 100000
        self.chunkLimit = self.worldSize / self.chunkSize
        self.noiseScale = 100

    
    def generateBiomeChunk(self):
        """
        This function will generate a chunk of the world based on the user input.
        """
        # Generate chunk data
        
        random.seed(self.seed +self.chunkX  * 100000 + self.chunkY)
        _layerOneNoise = PerlinNoise(octaves=4, seed=random.randint(0, 100000))
        _layerTwoNoise = PerlinNoise(octaves=6, seed=random.randint(0, 100000))
        _layerThreeNoise = PerlinNoise(octaves=8, seed=random.randint(0, 100000))
        _biomeData = numpy.zeros((self.chunkSize, self.chunkSize), dtype=str)
        self.logger.info(f"Generated biome chunk data for chunk {self.chunkX}, {self.chunkY}")

        for x in range(self.chunkSize):
            for y in range(self.chunkSize):
                if not self.isWithinBorder(self.chunkX, self.chunkY):
                    _biomeData[x][y] = biome.TECTONIC_PLATE
                else:
                    nx, nx = (self.chunkX * self.chunkSize + x) / self.worldSize, (self.chunkY * self.chunkSize + y) / self.noiseScale
                    value = _layerOneNoise([nx, nx]) * 0.5 + _layerTwoNoise([nx, nx]) *  0.5 + _layerThreeNoise([nx, nx]) * 0.5
                    _biomeData[x][y] = self.mapBiome(value)
        return _biomeData
    
    def generateBlockChunk(self):
        """
        This function will generate a chunk of the world based on the user input.
        """
        _blockData = numpy.zeros((self.chunkSize, self.chunkSize), dtype=str)
        self.logger.info(f"Generated block chunk data for chunk {self.chunkX}, {self.chunkY}")
        _blockNoise = PerlinNoise(octaves=4, seed=self.seed + 100000)
        for x in range(self.chunkSize):
            for y in range(self.chunkSize):
                nx, ny = (self.chunkX * self.chunkSize + x) / self.worldSize, (self.chunkY * self.chunkSize + y) / self.noiseScale
                _biome = self.biomeData[x][y]
                self.logger.info(f"Biome selected: {_biome}")
                if _biome in BLOCK_VARIATIONS:
                    _blockValue = _blockNoise([nx, ny])
                    _blockList = BLOCK_VARIATIONS[biome]
                    _blockData[x][y] = _blockList[int((_blockValue + 1)/2 * len(_blockList)) % len(_blockList)]
                    self.logger.info(f"Block generated: {_blockData[x][y]}")
                else:
                    _blockData[x][y] = Block.NORMAL_DIRT
                    self.logger.error(f"Invalid biome: {biome}")

        self.logger.info(f"Block chunk data generated for chunk {self.chunkX}, {self.chunkY}")
        return _blockData
    def mapBiome(self, value, nx, ny):
        """
        This function will map a value to a biome. This is used in the generation of the world. It will also define the rarity of certain biomes.

        """
        self.logger.info(f"Mapping biome for value {value}")
        if value < -0.3:
            self.logger.info(f"Selected biome: {biome.OCEANS}")
            return self.selectRandom(biome.OCEANS)  # Oceans
        elif value < -0.2:
            self.logger.info(f"Selected biome: {biome.WASTELAND_SHORES}")
            return biome.WASTELAND_SHORES  # Wasteland Shores
        elif value < -0.1:
            self.logger.info(f"Selected biome: {biome.RIVERS}")
            return self.selectRandom(biome.RIVERS)  # Rivers
        elif value < 0.0:
            self.logger.info(f"Selected biome: {biome.PONDS}")
            return self.selectRandom(biome.PONDS)  # Ponds
        elif value < 0.1:
            self.logger.info(f"Selected biome: {biome.DESERTS}")
            return self.selectRandom(biome.DESERTS)  # Deserts
        elif value < 0.2:
            self.logger.info(f"Selected biome: {biome.NORMAL_WASTELAND}")
            return biome.NORMAL_WASTELAND  # Normal Wasteland
        elif value < 0.3:
            self.logger.info(f"Selected biome: {biome.RADIOACTIVE_WASTELAND}")
            return biome.RADIOACTIVE_WASTELAND  # Radioactive Wasteland
        elif value < 0.4:
            self.logger.info(f"Selected biome: {biome.GRASSLANDS}")
            return biome.GRASSLANDS  # Grasslands
        elif value < 0.5:
            self.logger.info(f"Selected biome: {biome.FORESTS}")
            return self.selectRandom(biome.FORESTS)  # Forests
        elif value < 0.55:
            self.logger.info(f"Selected biome: {biome.SWAMPS}")
            return self.selectRandom(biome.SWAMPS)  # Swamps
        elif value < 0.6:
            self.logger.info(f"Selected biome: {biome.VOLCANIC}")
            return self.rareBiome(biome.VOLCANIC, nx, ny)  # Volcanic Lands
        else:
            self.logger.info(f"Selected biome: {biome.MOUNTAINS}")
            return self.rareBiome(biome.MOUNTAINS, nx, ny)  # Mountains
    

    def selectRandom(self, biomes):
        """
        This function will select a random biome from a list of biomes.
        """
        return random.choice(biomes)
    
    def rareBiome(self, biome, nx, ny):
        """
        This function will determine if a rare biome should be generated.
        """
        if random.random() < 0.001:
            self.logger.info(f"Rare biome generated: {biome}")
            return biome
        else:
            return self.mapBiome(PerlinNoise.noise([nx, ny]), nx, ny) # Recalculate to avoid invalid assignment
        
    def isWithinBorder(self, x, y):
        """
        This function will check if a block is within the world border.
        """
        return 0 <= x < self.chunkSize and 0 <= y < self.chunkSize
    

# 
class chunkManager:
    def __init__(self, seed, filename="world"):
        # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.savePath = str(Path.home() / "Documents" / "Afterlight" / "saves")
        self.saveFolder = str(Path.home() / "Documents" / "Afterlight" / "saves" / filename)
        self.logger = logging.getLogger(__name__)

        # Other Objects - These are objects that are used by the class
        self.seed = seed
        self.filename = filename + ".hdf5"
        self.chunks = {}
        self.file = h5py.File(self.saveFolder / self.filename, "a")

        # Chunk limits
        self.chunkSize = 16
        self.worldSize = 100000
        self.chunkLimit = self.worldSize / self.chunkSize
        self.noiseScale = 100
    
    def isValidChunk(self, chunkX, chunkY):
        """
        This function will check if a chunk is valid.
        """
        return 0 <= chunkX < self.chunkLimit and 0 <= chunkY < self.chunkLimit
    
    def getChunk(self, chunkX, chunkY):
        """
        This function will get a chunk from the chunk manager.
        """

        if not self.isValidChunk(chunkX, chunkY):
            self.logger.error(f"Invalid chunk: {chunkX}, {chunkY}")
            return None # Return None if the chunk is invalid
        
        _chunkKey = f"chunk_{chunkX}_{chunkY}" # Generate chunk key
        self.logger.info(f"Getting chunk: {_chunkKey}") # Log the chunk key
        
        if _chunkKey in self.file:
            _chunk = worldChunkGenerator(chunkX, chunkY, self.seed) # Generate chunk
            self.file.create_dataset(_chunkKey, data=_chunk.data.astype("S")) 
            self.logger.info(f"Chunk generated: {_chunkKey}")
            self.chunks[(chunkX, chunkY)] = _chunk # Add chunk to chunks dictionary
        
        else: 
            _chunkData = self.file[_chunkKey][:].astype("U") # Load as unicode string

            _chunk = worldChunkGenerator(chunkX, chunkY, self.seed, data=_chunkData) # Generate chunk
            self.chunks[(chunkX, chunkY)] = _chunk
            self.logger.info(f"Chunk loaded: {_chunkKey}")
        
        return self.chunks[(chunkX, chunkY)]
    
    def updateBlock(self, chunkX, chunkY, x, y, value):
        """
        This function will update a block in a chunk.
        """
        if not self.isValidChunk(chunkX, chunkY):
            self.logger.error(f"Invalid chunk: {chunkX}, {chunkY}")
            return 
        
        _chunk = self.getChunk(chunkX, chunkY)
        if _chunk is None:
            return
        
        if _chunk.data[x, y] == biome.TECTONIC_PLATE:
            self.logger.error(f"Cannot update block: {chunkX}, {chunkY}, {x}, {y} is a tectonic plate - Unbreakable block")
            return 4 # Return 4 if the block is a tectonic plate
        
        _chunk.data[x][y] = value
        _chunkKey = f"chunk_{chunkX}_{chunkY}"
        self.file[_chunkKey][:] = _chunk.data.astype("S")
        self.logger.info(f"Block updated: {_chunkKey}, {x}, {y}, {value}")
    
    def saveWorld(self):
        """
        This function will save the world to a file.
        """
        self.logger.info(f"Saving world to file")
        for (chunkX, chunkY), chunk in self.chunks.items():
            _chunkKey = f"chunk_{chunkX}_{chunkY}"
            self.file[_chunkKey][:] = chunk.data.astype("S")
        self.file.close()
        self.logger.info(f"World saved to file")

    def loadWorld(self):
        """
        This function will load the world from a file.
        """
        self.logger.info(f"Loading world from file")
        self.file = h5py.File(self.saveFolder / self.filename, "r")
        for chunkKey in self.file.keys():
            _chunkX, _chunkY = map(int, chunkKey.split("_")[1:])
            _chunkData = self.file[chunkKey][:].astype("U")
            self.chunks[(_chunkX, _chunkY)] = worldChunkGenerator(_chunkX, _chunkY, self.seed, data=_chunkData)

        self.file.close()
        self.logger.info(f"World loaded from file")
    



        

        
    
    
        

        



        