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
#function to listen for messages from clients

private_key = None
def check_private_key_file():
    if private_key:
        if os.path.exists(private_key):
            print("Private key file exists.")
        else:
            print("Private key file does not exist.")
            messagebox.showerror("Error", "Private key file does not exist.")
    else:
        print("Private key is not set.")
        messagebox.showerror("Error", "Private key is not set.")


def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)

def connect():

    # try except block
    try:

        # Connect to the server
        client.connect((HOST, PORT))
        print("Successfully connected to server")
        add_message("[SERVER] Successfully connected to the server")
    except:
        messagebox.showerror("Unable to connect to server", f"Unable to connect to server {HOST} {PORT}")

    username = username_textbox.get()
    if username != '':
        client.sendall(username.encode())
        print("SEND : ", username.encode() )
    else:
        messagebox.showerror("Invalid username", "Username cannot be empty")

    if private_key != '':
        #client.sendall(private_key.encode())
        print("SEND : ", private_key )
        print(private_key )
    else:
        messagebox.showerror("Invalid username", "Username cannot be empty")

    threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()

    #tk
    username_textbox.config(state=tk.DISABLED)
    username_button.config(state=tk.DISABLED)
    username_button.pack_forget()
    username_textbox.pack_forget()
    file_label.config(state=tk.DISABLED)
    file_button.config(state=tk.DISABLED)
    file_button.pack_forget()
    file_label.pack_forget()
    username_label['text']= "Welcome " + username + " to our secure room"
    username_label.pack(side=tk.LEFT)


def open_file_dialog():
    global private_key
    private_key = filedialog.askopenfilename()
    print(private_key)  # Replace this with your own logic

def send_message():
    message = message_textbox.get()
    if message != '':
        message_textbox.delete(0, len(message))
        
        # Encrypt the message
        messageCopy =cryptoFunction.encryptMessage(message.encode("utf-8"))
        client.sendall(messageCopy.encode("utf-8"))
        print("SEND : ", messageCopy.encode() )
        
        print("This message has been delivered")
    else:
        messagebox.showerror("Empty message", "Message cannot be empty")

def listen_for_messages_from_server(client):
    message = client.recv(2048).decode('utf-8')

    print("RECV : ", message)
        #####
    if message != '':
        message = cryptoFunction.decryptMessage(message.encode("utf-8"))
    messagebox.showerror("Error", "Message recevied from client is empty")











DARK_GREY = '#485460'
MEDIUM_GREY = '#1e272e'
OCEAN_BLUE = '#60a3bc'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)

root = tk.Tk()
root.geometry("600x600")
root.title("Messenger Client")
root.resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)

top_frame = tk.Frame(root, width=800, height=100, bg=DARK_GREY)
top_frame.grid(row=0, column=0, sticky=tk.NSEW)

bellow_topframe = tk.Frame(root, width=800, height=100, bg=DARK_GREY)
bellow_topframe.grid(row=1, column=0, sticky=tk.NSEW)

middle_frame = tk.Frame(root, width=600, height=400, bg=MEDIUM_GREY)
middle_frame.grid(row=2, column=0, sticky=tk.NSEW)

bottom_frame = tk.Frame(root, width=600, height=100, bg=DARK_GREY)
bottom_frame.grid(row=3, column=0, sticky=tk.NSEW)

username_label = tk.Label(top_frame, text="Enter your alias:", font=FONT, bg=DARK_GREY, fg=WHITE)
username_label.pack(side=tk.LEFT, padx=10)

username_textbox = tk.Entry(top_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
username_textbox.pack(side=tk.LEFT)

username_button = tk.Button(top_frame, text="Join", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=connect)
username_button.pack(side=tk.LEFT, padx=15)

file_label = tk.Label(bellow_topframe, text="Enter your private key path:", font=FONT, bg=DARK_GREY, fg=WHITE)
file_label.pack(side=tk.LEFT, padx=10)
file_button = tk.Button(bellow_topframe, text="Choose File", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=open_file_dialog)
file_button.pack(side=tk.LEFT, padx=15)

message_textbox = tk.Entry(bottom_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=38)
message_textbox.pack(side=tk.LEFT, padx=10)

message_button = tk.Button(bottom_frame, text="Send", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=send_message)
message_button.pack(side=tk.LEFT, padx=10)

message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=MEDIUM_GREY, fg=WHITE, width=67, height=26.5)
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP)


# main function
def main():
    #print("CODE :", server.getMethod())
    root.mainloop()
    
if __name__ == '__main__':
    main()