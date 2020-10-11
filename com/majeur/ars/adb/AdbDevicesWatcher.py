#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:14:25 2020

@author: puneet
"""
import AdbHelper;
import AdbCommandBuilder;
import threading ;
import time
import CommandExec;
import File;
import re;

class AdbDevicesWatcher(threading.Thread):
    __madbHelper: AdbHelper;
    __mWatchThread: threading.Thread;
    __mPreviouslyConnectedDevices=""
    
    
    def __init__(self,adbHelper):
        self.__madbHelper=adbHelper
#    def __init__(self):
        threading.Thread.__init__(self)
        self.__mWatchThread=self
        self._dts=list()
        
    def startWatch(self):
 #       self.__mWatchThread=threading.Thread(target=run)
        self.__running=True
        self.__mWatchThread.start()
        
    def stopWatch(self):
        self.__running=False
        
    def fin(self):
        return self._dts
    def run(self):
        print(str(threading.currentThread().ident)+":device watching started")
        while self.__running == True:
            devices=list()
            commandBuilder=self.__madbHelper.getCommandBuilder();
            _stdout,_stderr,_returncode=CommandExec.CommandExec().execute(commandBuilder.buildDevicesCommand())
            time.sleep(10)
            
            if _returncode == 0:
                print(_stdout)
                for _line in _stdout.decode('utf-8').splitlines():
                    if re.match("^List",_line):
                        print("skip:",_line)
                        continue
                    if re.match("^ *$",_line):
                        print("skip:",_line);
                        continue
                    if re.match("^\*",_line):
                        print("skip:",_line);
                        continue
                    print("device:",_line)
                
#                devices.add(AdbDevice(line))
            else:
                print(_stderr)
                break
            #
        print(str(threading.currentThread().ident)+":device watching stopped")
            
            
    
#if __name__=='__main__':
#    _file=File.File("/home/puneet/Android/Sdk/platform-tools/adb")    
#    _ah=AdbHelper.AdbHelper(_file)
#    _dw=AdbDevicesWatcher(_ah)
#    print("main starts"+str(threading.currentThread().ident))
#    _dw.startWatch()
#    time.sleep(30)
#    _dw.stopWatch()
#    print("main exits"+str(threading.currentThread().ident),_dw.fin())
