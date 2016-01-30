#!/usr/bin/env python
#-*- coding:utf8 -*-

import socket
import threading
import os

host = '0.0.0.0'
port = 7076

def HandleFunc(sock, addr):
    _clientip = sock.getpeername()[0]
    sock.send('Welcome:' + _clientip + '\r\n')  #write information to client
    while 1:
        data=sock.recv(4096) #get data from client save to buffer
        if data == 'exit' or not data:
            break
        else:
            data = data.replace('exit','')
            print data
            with open(_clientip, 'w') as f:
                f.write(str(data))
            from sh import jq
            print jq('.', _clientip)
    sock.close()

if __name__ == '__main__':

    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind((host,port))
        s.listen(5)
        print 'Resource is waiting for connection in %s:%d...' %(host, port)
        while 1:
            sock, addr = s.accept()
            #Init new sock from client, addr is client ip and port.
            threading.Thread(target=HandleFunc, args=(sock, addr)).start()

    except StandardError as msg:
        print 'Create socket failed due to %s' % msg
        exit(1)
