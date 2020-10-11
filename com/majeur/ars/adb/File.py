#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:23:21 2020

@author: puneet
"""
import AdbCommandBuilder

import os
class File:
    def __init__(self,_filename):
        self.__filename=_filename
        if not os.path.isfile(self.__filename):
            raise Exception("File ("+self.__filename+")does not exists")
            
    def getAbsolutePath(self):
        return self.__filename
    
f=File("/home/puneet/android.sh")
print(f.getAbsolutePath())