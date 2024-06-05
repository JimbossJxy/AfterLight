"""
Author Block
Author: James Collum
Date Creation: 29/05/2024
Document Name: button.py
Purpose of Document: This document will be used to handle buttons rendered on the screen.

"""

class Button:
    def __init__(self, image, pos, textInput, font, colour, hoverColour):
        self.image = image
        self.posX = pos[0]
        self.posY = pos[1]
        self.font = font
        self.baseColour = colour
        self.hoverColour = hoverColour
        self.textInput = textInput
        self.text = self.font.render(self.textInput, True, self.baseColour)
        if self.image is not None:
            self.image = self.image.convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.text.get_height(), self.text.get_height()))
