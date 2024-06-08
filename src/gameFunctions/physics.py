"""
Author Block
Author: James Collum
Date Creation: 02/06/2024
Document Name: variables.py
Purpose of Document: This document will be used to processs physics for the game.

"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import configparser
import logging
import pathlib
import pickle
import pygame
import subprocess
import shutil
import zipfile
from datetime import datetime
from pathlib import Path
from src.util.misc import misc
from src.gameFunctions.world import biome


class physics:
    def __init__(self) :
        # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logger = logging.getLogger(__name__)

        # Other Objects - These are objects that are used by the class
    
    #class collisions:

    class gameObject:
        def __init__(self, imagePath, position, debug=False):
            # Boilerplate code
            self.misc = misc()
            self.warningPopup = self.misc.warningPopup
            self.errorPopup = self.misc.errorPopup
            self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
            self.logger = logging.getLogger(__name__)

            self.originalImage = pygame.image.load(imagePath).convert_alpha()
            self.image = self.originalImage
            self.rect = self.image.get_rect(topleft=position)
            self.mask = pygame.mask.from_surface(self.image)
            if debug:
                self.maskImage = self.mask.to_surface()

            self.direction = "right" #The direction the player is facing

        def draw(self, screen):
            screen.blit(self.image, self.rect.topleft)
        
        def updateDirection(self, keys):
            if keys[pygame.K_a] and self.direction != "left":
                self.direction = "left"
                self.image = pygame.transform.flip(self.image, True, False)
                self.rect = self.image.get_rect(topleft=self.rect.topleft)
                self.logger.info("Player is facing left")

            elif keys[pygame.K_d] and self.direction != "right":
                self.direction = "right"
                self.image = self.originalImage
                self.rect = self.image.get_rect(topleft=self.rect.topleft)
                self.logger.info("Player is facing right")

    class Biome:
        def __init__(self, name, rect, effect):
            self.name = name
            self.rect = pygame.Rect(rect)
            self.effect = effect
    
    class collisionCheck:
        def __init__(self, obj1, obj2):
            # Boilerplate code
            self.misc = misc()
            self.warningPopup = self.misc.warningPopup
            self.errorPopup = self.misc.errorPopup
            self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
            self.logger = logging.getLogger(__name__)

            self.obj1 = obj1
            self.obj2 = obj2

        def checkCollision(self):
            offset = (self.obj2.rect.x - self.obj1.rect.x, self.obj2.rect.y - self.obj1.rect.y)
            result = self.obj1.mask.overlap(self.obj2.mask, offset)
            if result:
                self.logger.info("Collision detected")
                return True
            else:
                return False
            
        def boundingBoxCollision(self, obj1, obj2):
            if obj1.rect.colliderect(obj2.rect):
                self.logger.info("Bounding Box Collision detected")
                return True
            else:
                return False
        
        def biomeCollision(self, player, biomes):
            for biome in biomes:
                if player.rect.colliderect(biome.rect):
                    self.logger.info(f"Player has entered {biome.name}")
                    return biome.effect
            return None
            
            
            
       


