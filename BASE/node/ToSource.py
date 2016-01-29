#!/usr/bin/python -O
#-*- coding:utf8 -*-

import socket
import getinfo

addr = ('127.0.0.1', 7076)
infos = getinfo.SysInfo()
try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)
    print s.recv(1024)
    s.send(str(infos))
    s.send('exit')
    s.close()
except Exception as e:
    print 'Connection error, %s' %e
    exit()
finally:
    print 'Connection Over.'
