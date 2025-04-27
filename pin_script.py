import socket

HOST = '127.0.0.1'
PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

data = "magicNumber=123"
request = (
    "POST /verify HTTP/1.1\r\n"
    "Host: 127.0.0.1\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    f"Content-Length: {len(data)}\r\n"
    "Connection: close\r\n"
    "\r\n"
    f"{data}"
)

sock.sendall(request.encode())

response = b""
while True:
    chunk = sock.recv(1024)
    if not chunk:
        break
    response += chunk

print(response.decode())

sock.close()