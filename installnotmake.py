#!/usr/bin/env python

import os

#用于判断命令是否存在，若不存在，返回None 否则返回 1
def can_run(cmd):
	if isinstance(cmd, str):
			##将产生的信息丢进垃圾桶内			
		i = os.system("which "+cmd +">/dev/null")
		if i:	
			return None
		else :
			return 1;
	else: 
		return None


#解决依赖关系，若pacman中有这个软件，则安装并且返回 1，否则返回 2
def reslove_dep(software):
	#判断进入函数内的变量是不是str
	if isinstance(software,str):
		#若存在变量，则返回 1
		if can_run(software) ==1:
			return 1;
		else:
		#若不存在，则进行安装
		#查看pacman中有没有这个软件
			i = os.system("sudo pacman -Ss "+software+">/dev/null")
			if i==0:
			#安装
				i = os.system("sudo pacman -S "+software+" --noconfirm >>/dev/null")
				if i == 0:
					return 1
				else :
					return 2
			else :
				return 2

		
def sh_c(cmd):
	i = os.system(cmd);
	if i == 0:
		return 1
	else :
		return 0





print(reslove_dep("nginx"))
