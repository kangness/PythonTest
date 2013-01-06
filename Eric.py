#!/usr/bin/env  python
import ConfigParser as cparser
import sys


config = cparser.ConfigParser()
ret = config.read("data.conf")
if len(ret) >1:
    print("open file failed")
    sys.exit(-1)

for section in config.sections():
    print ("In section ",section)
    for key,value in config.items(section):
        print("key '%s' has value '%s' "%(key,value))
value = config.get("section_name","key_name")
           
