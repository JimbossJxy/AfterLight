"""
Author Block
Author: James Collum
Date Creation: 18/05/2024
Document Name: player.py
Purpose of Document: The purpose of this document is to provide the code for the play class
Referenced Code:


"""

import pygame
import sys

class player:
    def __init__(self, x, y, width, height):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def main(self, display):
        pygame.draw.rect(display, (255,0,0), (self.x, self.y, self.width, self.height))