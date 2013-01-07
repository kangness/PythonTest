#!/usr/bin/env  python

import os

def git(source,dist):
    if isinstance(source, str) and isinstance(dist,str) :
        i = os.system("git clone "+source+" "+dist)
        if i:    
            return None
        else :
            return 1;
    else: 
        return None

def sh(cmd):
    if isinstance(cmd,str):
        os.system(cmd)
        return 1
    else:
        return None

