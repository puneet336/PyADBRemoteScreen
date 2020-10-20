#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:14:55 2020

@author: puneet
"""

import subprocess
import threading;
import abc;
class CommandExec:
    
    class Callback(abc.ABC):
        @abc.abstractmethod
        def callback(data):
            pass
    
    @staticmethod
    def execute(command):
        process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        _stdout,_stderr=process.communicate()
        _returncode=process.returncode
        return _stdout,_stderr,_returncode
    
    @staticmethod
    def execAsyncTask(command,callback):
        _stdout,_stderr,_rc=CommandExec.execute(command)
        if callback !=None:
            callback.callback()
        
        
    @staticmethod
    def execAsync(command,callback):
        threading.Thread(target=CommandExec.execAsyncTask,args=(command,callback))
