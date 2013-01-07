#!/usr/bin/env python

import os
import sys
import getopt


def usage():
	print("Usage:  [-c] [-o <outfile>] <infile>\n")


try:
	result,s = getopt.getopt(sys.argv[1:],'co:vh',["help","version","outfile="])
except getopt.GetoptError as err:
	print(err)
	usage()
	sys.exit(2)

compile_only = None
outfile = None;



for o,a in result:
	if o =="-c":
		compile_only = True
	elif o in ("-h","--help"):
		usage()
		sys.exit()
	elif o in ("-o","--outfile"):
		outfile = a
	elif o in ("-v","--version"):
		print("This version is 0.0.1 write by kangness  ")
		sys.exit()
	else:
		assert False ,"unhandled option"


print("compile_only = ",compile_only)
print("outfile = ",outfile)
