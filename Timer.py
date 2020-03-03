# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:05:40 2020

@author: jarr1
"""

import time

slides = 24
slidesIndex = 1

def secTimer(delay):
    while delay > 0:
        print(delay)
        time.sleep(.100)
        delay = delay - 100
        
while True:
    
    print("Slide - {0}".format(slidesIndex))
    delay = 2500
    secTimer(delay)
    if slidesIndex < slides:
        slidesIndex = slidesIndex + 1
    else:
        slidesIndex = 1
    

