#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 00:13:50 2020

@author: puneet
"""
import re
import adb.Utils as Utils

class AdbDevice:
    serial: str;
    available: bool;
    product: str;
    model: str;
    device: str;
    
    def __init__(self,_line):
        self.serial=_line.split()[0]
        for _att in _line.split()[1:]:
            if _att == "device":
                self.available=True
        
        for _att in _line.split():
            if re.match("product:",_att):
                self.product=_att.split(":")[1]
            elif re.match("model:", _att):
                self.model=_att.split(":")[1]
            elif re.match("device:", _att):
                self.device=_att.split(":")[1]
        
        if self.available == False:
            model=self.serial[0:5]+"... (UNAVAILABLE)"
            
    def getReadableName(self):
        return self.model
    
    def isAvailable(self):
        return self.available
    
    def __eq__(self,_object):
        if isinstance(_object, AdbDevice):
            return (self.serial == _object.serial) and (self.available == _object.available)
        return False
    
    def __lt__(self,_object):
        if isinstance(_object, AdbDevice):
            return self.serial < _object.serial
        
        raise Exception("incompatible object types")
        
        
    def __str__(self):
        return self.model if self.available else "unavailable ["+ self.serial + "]"
        
        
    
if __name__=="__main__":
    d1=AdbDevice("ZF6223R2KK             device usb:1-3 product:chef model:motorola_one_power device:chef_sprout transport_id:19")
    d2=AdbDevice("ZF6223R2KK             device usb:1-3 product:chef model:motorola_one_power device:chef_sprout transport_id:19")
    d3=AdbDevice("A6T4C15916001549       device usb:1-1 product:Che1-L04 model:Che1_L04 device:Che1 transport_id:12")
    
   
    l=list()
    l.append(d1)
    l.append(d2)
    l.append(d3)
    l.sort()
    
    m=list()
    d4=AdbDevice("ZF6223R2KK             device usb:1-3 product:chef model:motorola_one_power device:chef_sprout transport_id:19")
    d5=AdbDevice("ZF6223R2KK             device usb:1-3 product:chef model:motorola_one_power device:chef_sprout transport_id:19")
    d6=AdbDevice("A6T4C15916001549       device usb:1-1 product:Che1-L04 model:Che1_L04 device:Che1 transport_id:12")
    m.append(d4)
    m.append(d5)
    m.append(d6)

    m.sort()
    print(Utils.Utils.equalsOrder(l,m))
    
    
    