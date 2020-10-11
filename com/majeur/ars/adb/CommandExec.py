#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:14:55 2020

@author: puneet
"""

import subprocess

class CommandExec:
    def execute(self,command):
        process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        _stdout,_stderr=process.communicate()
        _returncode=process.returncode
        return _stdout,_stderr,_returncode
        
        
