# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:09:18 2020

@author: krish
"""

import logging



logging.basicConfig(filename='drive_app_server.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.info('This will get logged to a file')
logger=logging.getLogger()

logging.info("I save it..")



