# Import required modules
import socket
import threading
import secrets
from tkinter import E

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

#function to listen for messages from clients

