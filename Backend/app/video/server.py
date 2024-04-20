# import socketio

# sio = socketio.Server(cors_allowed_origins='*')
# app = socketio.WSGIApp(sio)

# @sio.event
# def connect(sid, environ):
#     print('connect ', sid)
    
# @sio.event
# def disconnect(sid):
#     print('disconnect ', sid)
    
# @sio.event
# def message(sid, data):
#     print('message ', data)
#     sio.emit('response', room=sid)

# if __name__ == '__main__':
#     import eventlet
#     import eventlet.wsgi
#     eventlet.wsgi.server(eventlet.listen(('192.168.0.101', 5000)), app)

# import socket 
# host='192.168.0.101'
# port=9090

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((host, port))

# s.listen(5)

# while True:
#     c, addr = s.accept()
#     print('Got connection from', addr)
#     c.send('Thank you for connecting'.encode('utf-8'))
#     message = c.recv(1024).decode('utf-8')
#     c.send('Server: I received your message'.encode('utf-8'))
#     print(f"Client: {message}")
#     c.close()
    
    
import threading
import socket
import time

host = '192.168.0.101'
port=9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
      print(f"Broadcasting: {message}")
      client.send(message)
        
        
 
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('utf-8'))
            nicknames.remove(nickname)
            break
          

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        
        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat".encode('utf-8'))
        client.send('Connected to the server'.encode('utf-8'))
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
print("Server is listening...")

receive()