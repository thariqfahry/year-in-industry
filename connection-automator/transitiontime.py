# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 14:15:29 2021

@author: tfahry
"""

from lxml import etree as et
import RSXParser as rp

ruletree = rp.read('rules.xml')

def calculateTurnaround(param):
    
    turnaroundtime = param
    return turnaroundtime