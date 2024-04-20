import socket
import time

host = '192.168.0.101'
port=9090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

time.sleep(2)
def recive():
  while True:
    message = s.recv(1024).decode('utf-8')
    print(f"Server: {message}")
    s.send('Client: I received your message'.encode('utf-8'))
    time.sleep(2)
    s.send('Hello, Server'.encode('utf-8'))
    time.sleep(2)
    break
  
recive()