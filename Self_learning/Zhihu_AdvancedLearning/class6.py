import socket
import threading
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('0.0.0.0',8000))
server.listen()

def handle_sock(sock,addr):
    while True:
        data = sock.recv(1024)
        data = data.decode("utf8")
        if data.lower == "exit" or data.lower == "bye":
            break
        re_data = input()
        sock.send(re_data.encode("utf8"))
    sock.close()

while True:
    sock, addr = server.accept()
    
    client_thread = threading.Thread(target=handle_sock,args = (sock,addr))
    client_thread.start()