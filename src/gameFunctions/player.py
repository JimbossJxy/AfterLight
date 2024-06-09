"""
Author Block
Author: James Collum
Date Creation: 28/05/2024
Document Name: player.py
Purpose of Document: This document will be used to handle player logic in the game.
Referenced Code:



"""
# Add's project root to path
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import configparser
import logging
import pathlib
import pickle
import pygame
import random
import subprocess
import shutil
import zipfile
from datetime import datetime
from pathlib import Path
from src.util.misc import misc
from src.variables import saveGame


class player:
    def __init__(self, positon=(0, 0), frameRate=60):
        # Boilerplate code
        self.misc = misc()
        self.warningPopup = self.misc.warningPopup
        self.errorPopup = self.misc.errorPopup
        self.defaultPath = str(Path.home() / "Documents" / "Afterlight")
        self.logger = logging.getLogger(__name__)


        # Other Objects - These are objects that are used by the class
        self.images = {
            "up": "Assets/Player/Up.png",
            "down": "Assets/Player/Down.png",
            "left": "Assets/Player/Left.png",
            "right": "Assets/Player/Right.png"
        }
        self.images = {direction: pygame.image.load(path) for direction, path in self.images.items()}
        self.image = self.images["down"]
        self.rect = self.image.get_rect(topleft=positon)
        self.mask = pygame.mask.from_surface(self.image)
        self.direction = "down"
        self.defaultSpeed = 5
        self.sprintSpeed = 10
        self.sprinting = False
        self.animations = { "idle": [], "walking": [], "running": [], "attacking": []}
        self.currentAnimation = "idle"
        self.animationFrame = 0
        self.animationSpeed = 0.1
        self.animationTimer = 0
        self.animationLength = len(self.animations[self.animation])
        self.framerate = frameRate

        # Player specific attributes
        self.maxHealth = 100
        self.health = self.maxHealth
        self.maxStamina = 100
        self.stamina = self.maxStamina
        

        # Stamina depletion and replenishment rates
        self.stanimaDeplationRate = self.maxStamina / (frameRate * 8.25)
        self.staminaReplenishmentDelay = frameRate * 2
        self.staminaReplenishmentTimer = 0
        self.staminaReplenishmentRate = self.calculateStaminaReplenishmentRate()

        #Idle timer

        self.idleTimer = 0
        self.idle_animation_delay = 4 * frameRate
    
    def calculateStaminaReplenishmentRate(self):
        replenishTime = random.uniform(6.25, 12.75)
        return self.maxStamina / (self.framerate * replenishTime)

    def updateDirection(self, keys):
        _moved = False
        # Update player direction based on pressed keys
        if keys[pygame.K_w]:
            self.direction = "up"
            self.image = self.images["up"]
            _moved = True
        elif keys[pygame.K_s]:
            self.direction = "down"
            self.image = self.images["down"]
            _moved = True
        elif keys[pygame.K_a]:
            self.direction = "left"
            self.image = self.images["left"]
            _moved = True
        elif keys[pygame.K_d]:
            self.direction = "right"
            self.image = self.images["right"]
            _moved = True
        
        if _moved:
            self.idleTimer = 0
            self.currentAnimation = "walking"
        else:
            self.idleTimer += 1
            if self.idleTimer >= self.idle_animation_delay:
                self.currentAnimation = "idle"
            

        self.mask = pygame.mask.from_surface(self.image)
    
    # This function will be used to move the player
    def move(self, keys):
        
        # Check if player is sprinting and update speed and stamina accordingly
        if keys[pygame.K_LSHIFT] and self.stamina > 0:
            self.sprinting = True
            
            self.stamina = max(self.stamina - self.stanimaDeplationRate, 0)
            self.staminaReplenishmentTimer = 0
        else:
            self.sprinting = False
            
        speed = self.sprintSpeed if self.sprinting else self.defaultSpeed

        # Move the player based on pressed keys
        if keys[pygame.K_w]:
            self.rect.y -= speed
        if keys[pygame.K_s]:
            self.rect.y += speed
        if keys[pygame.K_a]:
            self.rect.x -= speed
        if keys[pygame.K_d]:
            self.rect.x += speed

        # replenish stamina if not sprinting
        if not self.sprinting and self.stamina <= self.maxStamina:
            self.replenishStamina()

    # This function will be used to replenish the player's stamina
    def replenishStamina(self):
        if self.hunger > 0 and self.thirst > 0:
            # Replenish stamina if player is not sprinting
            if self.staminaReplenishmentTimer >= self.staminaReplenishmentDelay:
                self.stamina = min(self.stamina + self.staminaReplenishmentRate, self.maxStamina)
                self.hunger = max(self.hunger - 0.01, 0)
                self.thirst = max(self.thirst - 0.015, 0)

            # Update stamina replenishment rate
            else:
                self.staminaReplenishmentTimer += 1
                if self.staminaReplenishmentTimer == self.staminaReplenishmentDelay:
                    self.staminaReplenishmentRate = self.calculateStaminaReplenishmentRate()
    
    # This function will be used to update the player's animation
    def updateAnimation(self):
        self.animationTimer += self.animationSpeed
        if self.animationTimer >= 1:
            self.animationTimer = 0
            if self.currentAnimation in self.animations:
                self.animationIndex = (self.animationIndex + 1) % len(self.animations[self.currentAnimation])
                self.image = self.animations[self.currentAnimation][self.animationIndex]
    
    # This function will be used to let the player use an item
    def useItem(self, item):
        pass

    # This function will be used to let the player attack
    def attack(self, item=None):
        self.animationIndex = 0
        pass

    # This function will be used to let the player interact with an object
    def interact(self, obj, item=None):
        pass
    
    # This function will be used to let the player take damage
    def takeDamage(self, damage):
        self.health = max(self.health - damage, 0)
        if self.health == 0:
            self.die()
    
    # This function will be used to let the player die
    def die(self):
        pass

    # This function will be used to let the player respawn
    def respawn(self):
        self.health = self.maxHealth
        self.stamina = self.maxStamina
        self.logger.info("Player stats reset")
        self.staminaReplenishmentRate = self.calculateStaminaReplenishmentRate()
        self.logger.info("Player respawned")

    # this will draw the player to the screen
    
    # This function will be used to update the player

    
    # This function will be used to update the player's stats
    def getHealthPercentage(self):
        self.logger.info(f"Health: {self.health} Max Health: {self.maxHealth}")
        return self.health / self.maxHealth
     
    def getStaminaPercentage(self):
        self.logger.info(f"Stamina: {self.stamina} Max Stamina: {self.maxStamina}")
        return self.stamina / self.maxStamina
    

    
    # save the player's stats to saveGame variable in variables.py
    def savePlayer(self):
        saveGame["player"]["health"] = self.health
        saveGame["player"]["stamina"] = self.stamina
        saveGame["player"]["hunger"] = self.hunger
        saveGame["player"]["thirst"] = self.thirst
        saveGame["player"]["position"] = self.rect.topleft
        self.logger.info(f"Player stats saved to saveGame: {saveGame['player']}")

    # load the player's stats from saveGame variable in variables.py
    def loadPlayer(self):
        self.health = saveGame["player"]["health"]
        self.stamina = saveGame["player"]["stamina"]
        self.hunger = saveGame["player"]["hunger"]
        self.thirst = saveGame["player"]["thirst"]
        self.rect.topleft = saveGame["player"]["position"]
        self.logger.info(f"Player stats loaded from saveGame: {saveGame['player']}")
        self.staminaReplenishmentRate = self.calculateStaminaReplenishmentRate()


        
def test_player_functions():
    # Create a player object
    p = player()

    # Test updateDirection function
    keys = {pygame.K_w: True}
    p.updateDirection(keys)
    assert p.direction == "up"
    assert p.image == p.images["up"]

    keys = {pygame.K_s: True}
    p.updateDirection(keys)
    assert p.direction == "down"
    assert p.image == p.images["down"]

    keys = {pygame.K_a: True}
    p.updateDirection(keys)
    assert p.direction == "left"
    assert p.image == p.images["left"]

    keys = {pygame.K_d: True}
    p.updateDirection(keys)
    assert p.direction == "right"
    assert p.image == p.images["right"]

    keys = {}
    p.updateDirection(keys)
    assert p.currentAnimation == "walking"

    # Test move function
    keys = {pygame.K_w: True}
    p.move(keys)
    assert p.rect.y == -p.defaultSpeed

    keys = {pygame.K_s: True}
    p.move(keys)
    assert p.rect.y == 0

    keys = {pygame.K_a: True}
    p.move(keys)
    assert p.rect.x == -p.defaultSpeed

    keys = {pygame.K_d: True}
    p.move(keys)
    assert p.rect.x == 0

    # Test replenishStamina function
    p.hunger = 50
    p.thirst = 50
    p.staminaReplenishmentTimer = p.staminaReplenishmentDelay
    p.replenishStamina()
    assert p.thirst == 50 - 0.015

    p.staminaReplenishmentTimer = p.staminaReplenishmentDelay - 1
    p.replenishStamina()
    assert p.staminaReplenishmentTimer == p.staminaReplenishmentDelay

    # Test updateAnimation function
    p.currentAnimation = "idle"
    p.animationTimer = 0.9
    p.updateAnimation()
    assert p.animationTimer == 0
    assert p.animationIndex == 1
    assert p.image == p.animations[p.currentAnimation][p.animationIndex]

    # Test reduceHunger function
    p.hunger = 50
    p.reduceHunger(10)
    assert p.hunger == 40

    # Test reduceThirst function
    p.thirst = 50
    p.reduceThirst(10)
    assert p.thirst == 40

    # Test savePlayer and loadPlayer functions
    p.health = 80
    p.stamina = 90
    p.hunger = 70
    p.thirst = 60
    p.rect.topleft = (100, 100)
    p.savePlayer()

    p.health = 0
    p.stamina = 0
    p.hunger = 0
    p.thirst = 0
    p.rect.topleft = (0, 0)
    p.loadPlayer()

    assert p.health == 80
    assert p.stamina == 90
    assert p.hunger == 70
    assert p.thirst == 60
    assert p.rect.topleft == (100, 100)

    print("All player functions tested successfully.")

# Run the test function
test_player_functions()