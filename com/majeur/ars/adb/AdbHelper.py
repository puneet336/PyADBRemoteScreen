#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:11:03 2020

@author: puneet
"""
import adb.AdbCommandBuilder as AdbCommandBuilder;
import adb.AdbCommandBuilder as AdbDevicesWatcher;
import adb.AdbDevice as AdbDevice;
import adb.CommandExec as CommandExec;
import abc
from typing import List
import os
import File
import atexit
import time
from io import BytesIO
import PIL.Image as Image


class AdbHelper:
    INVALID_DEVICE_INDEX = -1;
    __mAdbPath : str;
    __mCommandBuilder : AdbCommandBuilder;
    __mDeviceWatcher : AdbDevicesWatcher;
#    __mAttachedDevicesChangedListener : OnAttachedDevicesChangedListener;
#    __mattachedDevices: List[AdbDevice] = [];
    __mAttachedDevicesChangedListener=""
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
        
    def getCurrentDevice(self):
        return self.__mattachedDevices[self.__mattachedDevices]
    
    def getAttachedDevices(self):
        return tuple(i for i in self.__mattachedDevices)
    
    def setAttachedDevicesChangedListener(self,listener):
        self.__mAttachedDevicesChangedListener=listener;
    
    def setCurrentDevice(self,_index):
        pass
#        return self.__mCurrentDeviceIndex=int(_index)
    
    def getAdbPath(self):
        return self.__mAdbPath;
    
    def getCommandBuilder(self):
        return self.__mCommandBuilder;
        
    def onDevicesChanged(self,newDevices):
        self.__mCurrentDeviceIndex=self.INVALID_DEVICE_INDEX;
        self.__mattachedDevices=newDevices;
        if self.__mAttachedDevicesChangedListener is not None :
            self.__mAttachedDevicesChangedListener.onAttachedDevicesChanged()

    def performInputKey(self,keyCode):
        if self.__mCurrentDeviceIndex == self.INVALID_DEVICE_INDEX:
            return
        print("Key Pressed %d"%(keyCode))
        self.executeCommand(self.__mCommandBuilder.buildKeyEventCommand(keyCode))
        
    def performClick(self,x,y):
        if self.__mCurrentDeviceIndex == self.INVALID_DEVICE_INDEX:
            return
        print("Click at %.1f x %.1f"%(x,y))
        self.executeCommand(self.__mCommandBuilder.buildTapCommand(x,y))
    
    def performSwipe(self,x1,y1,x2,y2,duration):
        if self.__mCurrentDeviceIndex == self.INVALID_DEVICE_INDEX:
            return
        print("Swipe from %.1f x %.1f to %.1f x %.1f during %d ms"%(x1,y1,x2,y2,duration))
        self.executeCommand(self.__mCommandBuilder.buildSwipeCommand(x1,y1,x2,y2,duration))
    
    def retreiveScreenshot(self):
        if self.__mCurrentDeviceIndex == self.INVALID_DEVICE_INDEX:
            return None
        
        _data,_stderr,_rc=CommandExec.execute(self.__mCommandBuilder.buildScreencapCommand())
        if _data == None:
            print("Error:" + _stderr)
            return None
        inputstream=BytesIO(_data)
        return Image(inputstream)
    
    def executeCommand (self,command):
        CommandExec.execAsync(command,None)
    
        
    class OnAttachedDevicesChangedListener(abc.ABC):
        @abc.abstractmethod 
        def onAttachedDevicesChanged():
            pass

if __name__=="__main__":
    _file=File.File("/home/puneet/Android/Sdk/platform-tools/adb")    
    _ah=AdbHelper(_file)
    time.sleep(30)
    _ah.release()
