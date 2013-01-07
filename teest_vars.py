#!/usr/bin/env python

import os
import sys

vars = []
buf = []
file = open("test.conf")
lines = file.readlines()
for line in lines:
    i = line.find("#")
    if i!= -1:
        line = line[:i]
    buf = line.split("=")
    if len(buf) < 2:
        continue
    i = buf[1].find(";")
    if i!= -1:
        buf[1] = buf[1][:i] 
    buf[1] = buf[1].strip()
    buf[0] = buf[0].strip() 
    vars.append(buf)
print(vars)
file.close()