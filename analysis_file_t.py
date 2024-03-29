#!/usr/bin/env python

import ConfigParser
import string
import os
import sys

cf = ConfigParser.ConfigParser()
cf.read("test.conf")
s = cf.sections()
print ("section:",s)
o = cf.options("db")

print ("options:",o)

v = cf.items("db")

print("db:",v)

db_host = cf.get("db","db_host")
db_port = cf.getint("db","db_port")
db_user = cf.get("db","db_user")
db_pass = cf.get("db","db_pass")

threads = cf.getint("concurrent","thread")
processors = cf.getint("concurrent","processor")
print("db_host:", db_host)
print("db_port:", db_port)
print("db_user:", db_user)
print("db_pass:", db_pass)

print("thread:", threads)
print("processor:", processors)


cf.set("db","db_pass","zhaowei")
cf.write(open("test.conf","w"))
