#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:11:03 2020

@author: puneet
"""
import AdbCommandBuilder;
import AdbDevicesWatcher;
import AdbDevice;
import abc
from typing import List
import os
import File
import atexit
import time

class AdbHelper:
    INVALID_DEVICE_INDEX = -1;
    __mAdbPath : str;
    __mCommandBuilder : AdbCommandBuilder;
    __mDeviceWatcher : AdbDevicesWatcher;
#    __mAttachedDevicesChangedListener : OnAttachedDevicesChangedListener;
#    __mattachedDevices: List[AdbDevice] = [];
    __mattachedDevices="";
    __mCurrentDeviceIndex: int;
    
    
    def __init__(self, adbFile):
        self.__mAdbPath=adbFile.getAbsolutePath();
        self.__mCommandBuilder=AdbCommandBuilder.AdbCommandBuilder(self)
        atexit.register(self.executeCommand,self.__mCommandBuilder.buildKillServerCommand())
        self.__mDeviceWatcher=AdbDevicesWatcher.AdbDevicesWatcher(self)
        self.__mDeviceWatcher.startWatch();
    
    def release(self):
        self.__mDeviceWatcher.stopWatch();
    
    def getCommandBuilder(self):
        return self.__mCommandBuilder;
        
        
    def getAdbPath(self):
        return self.__mAdbPath;
	
    def executeCommand (command):
        print (command)
        pass
        
    class OnAttachedDevicesChangedListener(abc.ABC):
        @abc.abstractmethod 
        def onAttachedDevicesChanged():
            pass

if __name__=="__main__":
    _file=File.File("/home/puneet/Android/Sdk/platform-tools/adb")    
    _ah=AdbHelper(_file)
    time.sleep(30)
    _ah.release()
