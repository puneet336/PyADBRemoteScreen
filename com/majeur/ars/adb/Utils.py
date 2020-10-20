#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 13:24:13 2020

@author: puneet
"""
import enum
import platform
import pathlib

class Utils:
    
    @staticmethod
    def getRunningPyExePath():
        return pathlib.Path(__file__).parent.absolute()
        
    @staticmethod
    def equalsOrder(_c1,_c2):
#        if type(c1) != type(c2):
#            raise Exception("incompatibe types, cannot compare")
         if _c1  == None or _c2 == None or (len(_c2) != len(_c1)):
             return False
         
         for i in range(0,len(_c1)):
             if _c1[i] != _c2[i]:
                 return False
         
         return True
    @staticmethod
    def isEmpty(_str):
        if _str == None:
            return False
        return True
    
    def toString(d):
        if isinstance(d,float):
            return str(".3f"%d)
        
        _builder=""
        for t in d:
            _builder+=t;
            _builder=_builder+", "
        _builder=_builder+")"
        return _builder;
    
    @staticmethod
    def sleep(_event,_time):
         _event.wait(_time)
         
    class OS:
        class OSName(enum.Enum):
            WINDOWS=1
            LINUX=2
            MAC=3
        name: OSName;
        @classmethod
        def setOSName(cls):
            if platform.system() == "Linux":
                cls.name=cls.OSName.LINUX
            elif platform.system() == "Windows":
                cls.name==cls.OSName.WINDOWS
            else:
                cls.name==cls.OSName().MAC
        
        
         
         