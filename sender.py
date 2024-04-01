import socket

# Set up sender socket
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sender_socket.bind(('0.0.0.0', 9999))  # Sender's IP and port
sender_socket.listen(1)

# Accept incoming connection from receiver
receiver_socket, receiver_address = sender_socket.accept()

# Send message
message = "Hello from VM1!"
receiver_socket.send(message.encode())

# Close sockets
sender_socket.close()
receiver_socket.close()
