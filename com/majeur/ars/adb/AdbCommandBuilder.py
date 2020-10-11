# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import File
import AdbHelper

class AdbCommandBuilder:
    __file: File;
    __mAdbHelper: AdbHelper;
    
    def __init__(self,adbHelper):
        self.__mAdbHelper=adbHelper;

    
    def buildTapCommand(self,x,y):
        command=buildInputCommand()
        command.append("tap")
        command.append(str(x))
        command.append(str(y))
        return command;
    
    def buildKeyEventCommand(self,keyCode):
        command=buildInputCommand
        command.append("keyevent")
        command.append(str(keyCode))
        return command;
    
    def buildSwipeCommand(x1,y1,x2,y2,dt):
        command=buildInputCommand();
        command.append("swipe")
        command.append(str(x1))
        command.append(str(y1))
        command.append(str(x2))
        command.append(str(y2))
        command.append(str(dt))
        return command;
   
    def buildInputCommand():
        command=buildShellCommand();
        command.append("input")
        return command;
    
    def buildShellCommand():
        command=buildDeviceSpecificCommand();
        command.add("shell")
        return command;
    
    def buildScreenCapCommand(self):
        command=self.buildDeviceSpecificCommand();
        command.append("exec-out")
        command.append("screencap")
        command.append("-p")
        return command;
    def buildDeviceSpecificCommand(self):
        command=self.buildAdbCommand()
        command.append("-s")
        command.append(self.__mAdbHelper.getCurrentDevice().serial)
        return command
        
    def buildDevicesCommand(self):
        command=self.buildAdbCommand();
        command.append("devices")
        command.append("-l")
        return command;
    
    def buildKillServerCommand(self):
        command=self.buildAdbCommand();
        command.append("kill-server")
        command.append("-l")
        return command;
    
    def buildAdbCommand(self):
        command=list()
        command.append(self.__mAdbHelper.getAdbPath())
        return command; 
        
#obj=AdbHelper("/home/puneet/adb.exe")
#cb=AdbCommandBuilder(obj)
#print(cb.buildScreenCapCommand())