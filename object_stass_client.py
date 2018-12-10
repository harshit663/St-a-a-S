# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:54:29 2018

@author: prjve
"""
import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
 
ip_cmd = "ifconfig | grep inet | head -1 | awk '{print $2}'"
server_ip = "192.168.43.3" #server ip
server_port = 1111 #server portno


print("\t\t\tWelcome to my Private Staas service")
print("""
What do you want to do ?
1: Create a Drive
2: Extend Drive 
3: Exit     
""")

ch = int(input("Enter your choice :- "))
if ch == 1:
    uname = input("Enter your username :- ")
    pasw = input("Enter your password")
    size = input("Enter the size of the new drive in GB:- ")
    print("Creating your personal drive PLEASE WAIT...")
    task = "create"
    task = task.encode("utf-8")
    buname = uname.encode("utf-8")
    bsize = size.encode('utf-8')
    
    s.sendto(task, (server_ip, server_port))
    s.sendto(buname, (server_ip, server_port))
    s.sendto(bsize, (server_ip, server_port))
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    
    #ip1 = "192.168.43.211" #get client ip(by command )
    ip_out = subprocess.getstatusoutput(ip_cmd)
    port1 = 2222 #predefined port no
    s.bind((ip_out[0], port1))

    status = s.recvfrom(20)
    status = status[0].decode()
    
    if status == 'success':
        print("Creating a drive...")
        mk = "mkdir /media/{}".format(uname)
        mk_out = subprocess.getstatusoutput(mk)
        if mk_out[0] == 0:
            print("Drive Created Successfully")
        else:
            print("Drive already exists")
        print("Mounting the drive...")
        s1 = "mount 192.168.43.3:/cloud/[}  /media/{}".format(uname, uname)
        s_out = subprocess.getstatusoutput(s1)
        if s_out[0] == 0:
            print("Drive Succesfully Mounted ")
        else:
            print("Mounting Drive Failed")
    else:
        print("Error in creating drive")
    
elif ch == 2:
    uname = input("Enter your username :- ")
    size = input("Enter size to extend :- ")
    print("Extending your personal drive...")
    task = "extend"
    task = task.encode("utf-8")
    buname = uname.encode("utf-8")
    bsize = size.encode('utf-8')
    
    s.sendto(task, (server_ip, server_port))   
    s.sendto(buname, (server_ip, server_port))
    s.sendto(bsize, (server_ip, server_port))
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    
    #ip1 = "192.168.43.211" #get client ip(by command )
    ip_out = subprocess.getstatusoutput(ip_cmd)
    port1 = 2222 #predefined port no
    s.bind((ip_out[0], port1))
    
    status = s.recvfrom(20)
    status = status[0].decode()
    
    if status == 'extended':
        print("Drive Extended")
    else:
        print("Error in extending drive")
    
    
elif ch == 3:
    exit()
    
else:
    print("Invalid option")
    
