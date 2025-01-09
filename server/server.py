"""
    Python File:
    Purpose:
    Notes
"""

import socket

class BaseServer:


    def __init__(self):

        self.host = '127.0.0.1'
        self.port = 80
    
    def start(self):
        
        # create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket object to the address and port
        s.bind((self.host, self.port))

        # Start listening for connections
        s.listen(5)


        print("Listening at", s.getsockname())

        while True:
            # accept any new connection
            conn, addr = s.accept()

            print("Connected by", addr)

            # read the data sent by the client
            # for the sake of this tutorial, 
            # we'll only read the first 1024 bytes
            data = conn.recv(1024)

            # send back the data to client
            conn.sendall(data)

            # close the connection
            conn.close()


'''
Chatgpt generated
import socket
import signal
import sys

class TCPServer:
    host = '127.0.0.1'  # address for our server
    port = 8888  # port for our server

    def __init__(self):
        self.server_socket = None

    def start(self):
        # Create a socket object
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket object to the address and port
        self.server_socket.bind((self.host, self.port))
        # Start listening for connections
        self.server_socket.listen(5)

        print("Listening at", self.server_socket.getsockname())

        while True:
            try:
                # Accept any new connection
                conn, addr = self.server_socket.accept()

                print("Connected by", addr)

                # Read the data sent by the client
                data = conn.recv(1024)

                # Send back the data to the client
                conn.sendall(data)

                # Close the connection
                conn.close()

            except Exception as e:
                print(f"Error: {e}")
                break

    def shutdown(self):
        """Gracefully shuts down the server."""
        if self.server_socket:
            self.server_socket.close()
            print("Server socket closed.")

def handle_shutdown_signal(signum, frame):
    """Handler for the shutdown signal."""
    print("\nShutting down the server...")
    server.shutdown()
    sys.exit(0)

if __name__ == '__main__':
    server = TCPServer()

    # Set up signal handler for SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, handle_shutdown_signal)

    # Start the server
    server.start()

'''