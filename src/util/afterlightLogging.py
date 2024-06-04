"""
Author Block
Author: James Collum
Date Creation: 02/06/2024
Document Name: logging.py
Purpose of Document: This document will be used to handle logging for the game.
Referenced Code:
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import logging
import logging.config
from pathlib import Path
from logging.handlers import RotatingFileHandler



def afterlightLogging():
    _loggerConfig = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - [%(levelname)s] - %(name)s - %(message)s'
            },
        },
        'handlers': {
            'default': {
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
            },
            'file': {
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': str(Path.home() / "Documents" / "Afterlight" / "Logs" / "game.log"),
                'maxBytes': 5242880,
                'backupCount': 5,
            },
        },
        'loggers': {
            '': {
                'handlers': ['default', 'file'],
                'level': 'DEBUG',
                'propagate': True
            }
        }
    }
    logging.config.dictConfig(_loggerConfig)


    
    
    
