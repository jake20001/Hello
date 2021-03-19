# -*- coding:utf-8 -*-
# -------------------------------
# ProjectName : autoDemo
# Author : zhangjk
# CreateTime : 2020/12/2 20:00
# FileName : day2.1
# Description : 
# --------------------------------
import socket
from contextlib import closing

import multitask


def client_handler(sock):
    with closing(sock):
        while True:
            data = (yield multitask.recv(sock,1024))
            if not data:
                break
            yield multitask.send(sock,data)

def echo_server(hostname,port):
    addrinfo = socket.getaddrinfo(hostname,port,socket.AF_UNSPEC,socket.SOCK_STREAM)
    (family,socktype,proto,canonname,sockaddr) = addrinfo[0]
    with closing(socket.socket(family,socktype,proto)) as sock:
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        sock.bind(sockaddr)
        sock.listen(5)
        while True:
            multitask.add(client_handler((yield multitask.accept(sock))[0]))

if __name__ == '__main__':
    import sys
    hostname = '127.0.0.1'
    port = 8888
    if len(sys.argv)>1:
        hostname = sys.argv[1]
    if len(sys.argv)>2:
        port = int(sys.argv[2])
    multitask.add(echo_server(hostname,port))
    try:
        multitask.run()
    except KeyboardInterrupt:
        pass


