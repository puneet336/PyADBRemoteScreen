#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 00:13:50 2020

@author: puneet
"""

class AdbDevice:
    serial: str;
    available: bool;
    product: str;
    model: str;
    device: str;
    
    def __init__(self,_line):
        
        
    