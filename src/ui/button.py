"""
Author Block
Author: James Collum
Date Creation: 29/05/2024
Document Name: button.py
Purpose of Document: This document will be used to handle buttons rendered on the screen.

"""
import pygame
import logging

class Button:
    def __init__(self, image, pos, textInput, font, colour, hoverColour):
        self.posX = pos[0]
        self.posY = pos[1]
        self.font = font
        self.baseColour = colour
        self.hoverColour = hoverColour
        self.textInput = textInput
        self.text = self.font.render(self.textInput, True, self.baseColour)
        self.logger = logging.getLogger(__name__)
        if image is None:
            self.image = self.text
        else:
            self.image = image
        self.rect = self.image.get_rect(center=(self.posX, self.posY))
        self.textRect = self.text.get_rect(center=(self.posX, self.posY))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
            self.logger.debug("Button image drawn")

        screen.blit(self.text, self.textRect)
        self.logger.debug("Button text drawn")
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.logger.debug("Button clicked")
            return True
        return False
    
    def changeColour(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.textInput, True, self.hoverColour)
            self.logger.debug("Button colour changed")
        else:
            self.text = self.font.render(self.textInput, True, self.baseColour)
            self.logger.debug("Button colour reset")
    

