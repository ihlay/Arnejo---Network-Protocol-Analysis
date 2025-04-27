import socket

HOST = '127.0.0.1'
PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print("Connected!")

# Trying to send POST request manually
request = "POST /verify HTTP/1.1\nHost: 127.0.0.1\n\nmagicNumber=123"
sock.sendall(request.encode())

response = sock.recv(4096)
print(response.decode())

sock.close()
