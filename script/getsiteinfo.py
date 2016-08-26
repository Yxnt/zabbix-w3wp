#!/usr/bin/env python
# -*- coding:utf-8 -*-

import psutil
import argparse
import subprocess
from os import chdir

parser = argparse.ArgumentParser(description="通过进程PID来获取进程的一些信息")


def getpidbysitename(iisname):
    chdir('C:/Windows/System32/inetsrv')
    command = "appcmd list wp"
    result = subprocess.Popen(command,stdout=subprocess.PIPE)
    resultlist = []
    for i in result.stdout.readlines():
        i = str(i)
        resultlist.append(i)

    for line in resultlist:
        sitepid = line.split("\"")[1]
        sitename = line.split(":")[1].split(")")[0]
        if iisname == sitename:
            return sitepid

class process():

    def __init__(self,pid):
        self.__pid = pid

    def processinfo(self):
            return psutil.Process(int(self.__pid))

    def getmemory(self):
        try:
            return self.processinfo().memory_info().rss
        except:
            return None
    def getcpucounter(self):
        try:
            return self.processinfo().cpu_percent(1)
        except:
            return None
    def getthread(self):
        try:
            return len(self.processinfo().threads())
        except:
            return None

parser.add_argument('-m',help="获取进程内存使用 -m sitename")
parser.add_argument('-c',help="获取进程CPU使用    -c sitename")
parser.add_argument('-t',help="获取进程Thread   -t sitename")
args = parser.parse_args()

if args.m != None:
    print(process(getpidbysitename(args.m)).getmemory())
elif args.c != None:
    print(process(getpidbysitename(args.c)).getcpucounter())
elif args.t !=None:
    print(process(getpidbysitename(args.t)).getthread())

