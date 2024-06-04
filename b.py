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
LISTENER_LIMIT = 5
active_clients = [] 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(1) # 1 ở đây có nghĩa chỉ chấp nhận 1 kết nối
print("Server listening on port", PORT)

c, addr = s.accept()
print("Connect from ", str(addr))

#server sử dụng kết nối gửi dữ liệu tới client dưới dạng binary
c.send(b"Hello, how are you")
c.send(b"Bye")
c.close()

