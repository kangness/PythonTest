#!/usr/bin/env python

s = input("plase enter an integer:")
try:
	i = int(s)
	print("Valid integer entered:",i)
except ValueError as err:
	print(err)
