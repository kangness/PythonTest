#!/usr/bin/env python

def get_init(msg):
	while True:
		try:
			i = int (msg)
			return i
		except ValueError as err:
			print(err)

print(get_init(input()))
