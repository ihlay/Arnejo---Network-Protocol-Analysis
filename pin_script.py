import socket

HOST = '127.0.0.1'
PORT = 8888

def try_pin(pin):
    data = f"magicNumber={pin}"
    request = (
        "POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(data)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{data}"
    )
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.sendall(request.encode())

    response = b""
    while True:
        chunk = sock.recv(1024)
        if not chunk:
            break
        response += chunk

    sock.close()
    
    return response.decode()

print(try_pin(123))
