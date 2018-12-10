# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:41:59 2018

@author: prjve
"""

import socket
#import subprocess as sp


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

ip = "192.168.43.3"
port = 2222
s.bind((ip,port))

data = s.recvfrom(20)

print(data[0].decode())