# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:06:38 2018

@author: prjve
"""

import socket
import subprocess


def create_user():
    
    uname = user_name[0].decode()
    size = size_drive[0].decode()
    print(user_name)
    print(size_drive)
    
    print("Creating Logical Volume...")
    lv_create = "lvcreate --size {}G --name {} myvg".format(size, uname)
    create_out = subprocess.getstatusoutput(lv_create)
    if create_out[0] == 0:
        print("Logical Volume Created Succesfully")
    else:
        print("Error in creating Logical Volume")
    
    print("Formatting the logical volume...")
    lv_format = "mkfs.ext4 /dev/myvg/{}".format(uname)
    format_out = subprocess.getstatusoutput(lv_format)
    if format_out[0] == 0:
        print("Drive Formatted Succesfully")
    else:
        print("Error in Formatting Drive")
    
    print("Creating Directory...")
    create_user_dir = "mkdir /cloud/{}".format(uname)
    user_dir_out = subprocess.getstatusoutput(create_user_dir)
    if user_dir_out[0] == 0:
        print("Directory Created Succesfully ")
    else:
        print("Error in Creating drive")
        
    print("Mounting Drive...")
    mount_cloud_dir = "mount /dev/myvg/{} /cloud/{}".format(uname, uname)
    mnt_out = subprocess.getstatusoutput(mount_cloud_dir)
    if mnt_out[0] == 0:
        print("Mounted drive Successfully")
    else:
        print("Error in mounting drive")
        
    write_expt = "echo '/cloud/{} 192.168.43.211(rw, no_root_squash)' >> /etc/exports"
    write_output = subprocess.getoutput(write_expt)
    if write_output[0] != 0:
        print("Error in entering client info in /etc/exports")
    
    print("Staring NFS...")
    print(serivice_out = subprocess.getoutput("systemctl restart nfs"))
    
    s1= 'success'
    suc = s1.encode('utf-8')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    user_port = 2222
    s.sendto(suc, (client_ip, user_port)) #get ip from above
    
def extend_user():
    user = user_name.decode()
    size = size_drive.decode()
    print("Extending the drive...")
    lv_out = subprocess.getstatusoutput("lvextend --size +{}G /dev/cloudvg/{}".format(size, user))
    if lv_out[0] == 0:
        print("Drive extended Succesfully")
    else:
        print("Error in Extending the drive")
    print("Resizing the drive...")
    resize_out = subprocess.getstatusoutput("resize2fs /dev/cloudvg/{}".format(user))
    if resize_out == 0:
        print("Resizing done")
    else:
        print("Error in resizing")
    
    s1= 'extended'
    suc = s1.encode('utf-8')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    user_port = 2222
    s.sendto(suc, (client_ip, user_port))
    
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) 
    ip = "192.168.43.3"
    port = 1111
    s.bind((ip, port))
 
    btask = s.recvfrom(20)
    user_name = s.recvfrom(20)
    size_drive = s.recvfrom(20)
    client_ip  = btask[1][0]
    task = btask[0].decode()
    if task == 'create':
        create_user()
    elif task == 'extend':
        extend_user()
        