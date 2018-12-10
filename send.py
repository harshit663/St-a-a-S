# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:37:46 2018

@author: prjve
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
 
ip = "192.168.43.3"
port = 1234

data = input("Enter your data to send :- ")
x = data.encode('utf-8')
s.sendto(x, (ip, port))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.bind(("192.168.43.120", 2208))
y = s.recvfrom(30)
data1 = y[0].decode()
print(data1)