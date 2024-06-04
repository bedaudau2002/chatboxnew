# import required modules
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import os
import tkinter.filedialog as filedialog
import cryptoFunction
# Function to get the local IP address of the machine
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connect to a public IP address to get the local IP
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
    finally:
        s.close()
    return local_ip

# Get the local IP address and assign it to HOST
HOST = get_local_ip()
PORT = 1234 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client .py

# Như mình đã nói ở trên thì chúng ta không truyền tham số vào vẫn ok
s = socket.socket()
s.connect((HOST, PORT)) 

# 1024 là số bytes mà client có thể nhận được trong 1 lần
# Phần tin nhắn đầu tiên
msg = s.recv(1024)

# Phần tin nhắn tiếp theo 
while msg:
  print("Recvied ", msg.decode())
  msg = s.recv(1024)

s.close()
