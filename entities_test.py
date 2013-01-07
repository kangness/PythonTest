#!/usr/bin/env python

import os
import sys

def tree():
    return defaultdict(tree)

entities = {}
buf = []
two_split_list = ["sh","test","git"]
command = ["git","file","running","dir","dep","test","env","always","sh","debuginfo","prog","pacman","fetch","tarball","cpan","error","yum","cwd"]
file = open("test.conf.t")
lines = file.readlines()
for line in lines:
    if line.find("#")!= -1 :
        continue
    i = line.find("{")
    if i != -1:
        temp = line[:i]
        temp = temp.strip()
        continue
    else:
        i = line.find("}")
        if i!=-1:
            temp = None
            continue
        buf = line.split()
        if len(buf) <2:
            continue
         
        i = buf[len(buf)-1].find(";")
        if i!=-1:
            buf[len(buf)-1] = buf[len(buf)-1][:i]
        for buffer in buf:
            buffer = buffer.strip()
        if buf[0] not in command:
            print("command <  > not found",buf[0])
            sys.exit(1)
        if buf[0] in two_split_list:
            line = line.strip()
            line = line.strip(";\n")
            buf = line.split(" ",1)
            if len(buf) <2 :
                continue
            buf[0] = buf[0].strip()
            buf[1] = buf[1].strip(" ;")
        if temp not in entities:
            entities[temp] = {}
        if buf[0] not in entities[temp]:
            entities[temp][buf[0]] = []
        for buffer in buf[1:]:
            entities[temp][buf[0]].append(buffer)        
        
for buffer in entities:
    for buf in entities[buffer]:
        for buff in entities[buffer][buf]:
            print(buffer,"  ",buf," = ",buff)
file.close()

