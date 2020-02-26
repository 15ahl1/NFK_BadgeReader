#Written by Alastair Lewis
#Consumes messages on localhost and dumps into a file
import os
import socket

class Consumer:
    path = ""
    port = -1

    #Instantiate with path to output file and port to listen on
    def __init__(self, path, port):
        self.path = path
        self.port = port

    #Call this function once and it will continuously process messages
    def consume(self):
        message = ""
        #Setting up Socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', self.port))

        while True:
            #Waiting for connection
            s.listen(100)
            print("Waiting for a connection...")
            connection, client_address = s.accept()

            #Accepting connection
            print('Connection Accepted from: ' + str(client_address[1]))
            message = connection.recv(1024)

            #Write to file
            f = open(self.path, 'a')
            f.write(message.decode() + "\n")
            f.close()
            print("Message saved")
            message = ""

#c = Consumer("test.txt", 6969)
#c.consume()
