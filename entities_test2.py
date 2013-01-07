#!/usr/bin/env python

import os
import sys

type_list = [""]
entities_type  = {}
command_type = {}
file = open("test.conf")
lines = file.readlines()

#定义用于解析含有type的依赖关系

    
    
    
for line in lines:
    line = line.strip()
    if len(len) > 7 and line not in type_list:
        continue
    if line.find("#")!= -1 :
        continue