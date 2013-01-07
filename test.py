#!/usr/bin/env python
import os

def can_run(cmd):
	if isinstance(cmd, str):
		print("type is string")
		i = os.system("which "+cmd +">/dev/null")
		if i:	
			return None
		else :
			return 1;
	else: 
		return None



can_run("helloworld")



