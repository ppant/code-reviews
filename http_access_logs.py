# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:20:08 2021

@author: Pradeep
"""

import logging 

logger = logging.getLogger(__name__) 
...

def view(request, arg): 
    print(logger.info('Testing condition') )
    if something_bad: 
        print(logger.warning('Something bad happened')) 

 