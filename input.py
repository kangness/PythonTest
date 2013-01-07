#!/usr/bin/env python

print ("Type integers, each followed by Enter; or just Enter to finish")

total = 0
count = 0

while True:
	line = input("integer:")
	print(line)
	if line:
		try:
			number = int(line)
		except ValueError as err:
			print(err)
			continue
		total += number
		count +=1
	else:
		break
if count:
	print("count = ",count,"total = ",total,"mean = ",total/count)
