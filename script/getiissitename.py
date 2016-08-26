#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import subprocess
directory = 'C:/Windows/System32/inetsrv'
command = 'appcmd list wp'

os.chdir(directory)
result = subprocess.Popen(command,stdout=subprocess.PIPE)
resultlist = []

for i in result.stdout.readlines():
    i = str(i)
    resultlist.append(i)

n = 1
number = len(resultlist)
print('{"data":[')
for line in resultlist:
    sitepid = line.split("\"")[1]
    sitename = line.split(":")[1].split(")")[0]
    siteinfo = "%s_%s" % (sitepid, sitename)
    print('{"{%s}":"%s","{%s}":"%s"}' % ("#SITENAME",sitename,"#SITEINFO",siteinfo))
    if n != number:
        print(',')
    n+=1

print(']}')
