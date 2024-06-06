"""
Author Block
Author: James Collum
Date Creation: 16/05/2024
Document Name: main.py
Purpose of Document: Acting as the main file to run the majority of the code from
Referenced Code:


"""

from src.ui import menu

import src.util.gamerunner 
import src.util.initialise as initialise
from src.util.misc import misc

from src.gameFunctions import world






def main():
    initialise.run()
    screen = src.util.gamerunner.startup()
    menu.menu().mainMenu(screen=screen)
    
    

if __name__ == "__main__":
    main()