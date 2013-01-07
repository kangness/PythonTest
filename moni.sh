#!/bin/sh

########### 不使用expect实现passwd与su的自动执行 ###########
# 1. 站在 `自动telnet' 的肩膀上，......
# 2. 假定对用户test未设口令，否则需要更改此脚本
# 3. 未对普通用户su其他用户执行命令进行测试，估计没问题
#                                ver:2005.04.01(草稿)

time4link=2
address=127.0.0.1
username=test
password="\n"
time4run=2
commandstr='passwd'

(
  echo "HelloWorld"
  sleep $time4link    # 等待telnet联接成功后允许登录
  echo  $username     # 输入登录用户名
  sleep $time4link    # 等待允许输入登录口令
  echo  $password     # 输入登录口令
  sleep $time4link    # 等待允许确认终端类型
  echo  ""            # 采用默认终端类型
  sleep $time4link    # 等待命令输入允许
  sleep $time4link    # 由于设置终端类型所需的时间稍长，故在此增加等待时间
  echo  $commandstr   # 输入要执行的命令
  sleep $time4run     # 等待命令执行完毕
  echo  at12345             # 选择：Pick a password
  sleep $time4run     # 等待
  echo  q1w2e3       # 输入新密码
  sleep $time4run     # 等待
  echo  q1w2e3       # 再次输入新密码
) | ssh $address   # 以括号内子shell的输出作为telnet的输入
