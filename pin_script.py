import socket

HOST = '127.0.0.1'
PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print("Connected!")

# Try sending random text
sock.sendall(b"Hello Server")

response = sock.recv(4096)
print(response.decode())

sock.close()
