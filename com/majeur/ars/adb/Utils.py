#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 13:24:13 2020

@author: puneet
"""

class Utils:
    @staticmethod
    def equalsOrder(_c1,_c2):
#        if type(c1) != type(c2):
#            raise Exception("incompatibe types, cannot compare")
         if _c1  == None or _c2 == None or (len(_c2) != len(_c1)):
             print("p1")
             return False
         
         for i in range(0,len(_c1)):
             if _c1[i] != _c2[i]:
                 return False
         
         return True
    @staticmethod
    def sleep(_event,_time):
         _event.wait(_time)
         
         