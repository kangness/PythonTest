#!/usr/bin/env python

import os


file =  open("test.conf")
try:
    lines = file.readlines()
    for line in lines:
        print(line)
finally:
    file.close()
