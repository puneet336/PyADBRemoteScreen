#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 23:41:22 2020

@author: puneet
"""

import threading
import sys
import File
import os
import stat
from os import path
from adb.Utils import Utils
import time
import adb.AdbCommandBuilder as AdbCommandBuilder
import PyQt5
import tempfile


class AdbRemoteScreen(threading.Thread):
    ARGS=None;
    def __init__(self,ARGS):
        threading.Thread.__init__(self)
        self.ARGS=ARGS

        
    @staticmethod
    def main():
        ARGS={}
        for _arg in sys.argv:
            if "=" in _arg:
                ARGS[_arg.split('=')[0]]=_arg.split('=')[1]
            else:
                ARGS[_arg]=""

        _ars=AdbRemoteScreen(ARGS)
        _ars.start()
        _ars.join()
    
    def run(self):
        skipSysLookAndFeel=True if "--use-default-theme" in self.ARGS.keys() else False
        
        if skipSysLookAndFeel is True:
            _qappstyle=self.ARGS["--use-default-theme"]
        
        customAdbPath=""
        if "--adb-path" in self.ARGS.keys():
            customAdbPath=self.ARGS["--adb-path"]
        
        adbExecutable=self.loadCustomAdbExecutable(customAdbPath)
        if adbExecutable==None:
            adbExecutable=self.loadInternalAdbExecutable()
            if adbExecutable == None:
                print("Adb Executable not found")
                return 
            print("adb exe-",adbExecutable)
        
        
        
    def loadCustomAdbExecutable(self,_path):
        if _path==None or _path=="":
            return None
        
        if path.exists(_path):
            return File(_path)
        else:
            return None
    
    def loadInternalAdbExecutable(self):
        adbExecutableURL=None
        Utils.OS.setOSName()
        if (Utils.OS.name == Utils.OS.OSName.WINDOWS):
            adbExecutableURL=os.path.join(   os.path.dirname(  os.path.abspath(__file__)) , "adb_win.exe")
        elif (Utils.OS.name == Utils.OS.OSName.LINUX):
            adbExecutableURL= os.path.join(  os.path.dirname(os.path.abspath(__file__)) , "adb_lin.bin")
                                           
                                           
        elif (Utils.OS.name == Utils.OS.OSName.MAC):
            _qtErrorApp=PyQt5.QtWidgets.QApplication([])    
            _qtErrorDialog=PyQt5.QtWidgets.QErrorMessage()
            _qtErrorDialog.showMessage("no MAC support yet :"+adbExecutableURL, str)
            _qtErrorApp.exec_()
            return None
         
        tempfile.tempdir=os.path.join(Utils.getRunningPyExePath(),"Temp")
        if not os.path.exists(tempfile.tempdir):
            os.mkdir(tempfile.tempdir)
            
        tempDirectory=tempfile.TemporaryDirectory(prefix="tmp",suffix="tmp")
        
        try:
            tempAdbExecutable=open(  os.path.join(tempDirectory.name, "adb"),"wb"   );
            tempAdbExecutable.close()
        
            self.createTempExecutable(adbExecutableURL,tempAdbExecutable.name)
            return tempAdbExecutable.name
        except Exception as e:
            print("Error")
            print(e)
            _qtErrorApp=PyQt5.QtWidgets.QApplication([])
            _qtErrorDialog=PyQt5.QtWidgets.QErrorMessage()
            _qtErrorDialog.showMessage(str(e))
            _qtErrorApp.exec_()
            raise e
        
        
        
        if not os.path.isdir(tempDirectory.name):
            os.makedirs(tempDirectory)
        
        
    def createTempExecutable(self,adbSourceExecutableURL,destFile):
        _is=open(adbSourceExecutableURL,"rb")
        _os=open(destFile,"wb")
        _chunkSize=2048
        
        while True:
            _data=_is.read(_chunkSize)
            if _data == "" or len(_data) == 0:
                break
            _os.write(_data)
            
        _os.close()
        _is.close()
        
        if Utils.OS.name == Utils.OS.OSName.LINUX:
            _st=os.stat(destFile)
            os.chmod(destFile, _st.st_mode|stat.S_IEXEC)
            
        
        
        
        
        
if __name__=='__main__':
    AdbRemoteScreen.main()
    

