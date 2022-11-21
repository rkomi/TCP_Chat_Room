import threading
import socket
from colorama import Fore

print(Fore.LIGHTGREEN_EX + "Welcome to the chatroom!")

nickname = input(Fore.LIGHTGREEN_EX + "Enter a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 55555))


# Receive / listen thread
def receive():
    while True:
        try:
            # Receive message from server
            # If 'NICK' send nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close connection when error
            print("An error occured!")
            client.close()
            break


def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


# Start receive thread
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Start write thread
write_thread = threading.Thread(target=write)
write_thread.start()


# Receive / listen thread
def receive():
    while True:
        try:
            # Receive message from server
            # If 'NICK' send nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(input("Enter a nickname: ").encode('ascii'))
            else:
                print(message)
        except:
            # Close connection when error
            print("An error occured!")
            client.close()
            break
