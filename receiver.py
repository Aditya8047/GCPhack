import socket

# Set up receiver socket
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_socket.connect(('VM1_IP', 9999))  # VM1's IP and port

# Receive message
message = receiver_socket.recv(1024)
print("Received message:", message.decode())

# Close socket
receiver_socket.close()
