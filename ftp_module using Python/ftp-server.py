# server

import socket                   # Import socket module

port = 4999                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server is listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got a connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename = 'mytext.txt'
    with open(filename, 'rb') as f:
        in_data = f.read(1024)
        while in_data:
            conn.send(in_data)
            print('Sent ', repr(in_data))
            in_data = f.read(1024)

    print('Done sending')
    conn.send('Thank you for connecting')
    conn.close()


# client side server

import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 4999                    # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")

with open('received_file', 'wb') as f:
    print('File opened')
    while True:
        print('Recieving the data.....')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('File Recieved Successfully')
s.close()
print('The Connection is Closed')