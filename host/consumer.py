#Written by Alastair Lewis
#Consumes messages on localhost and dumps into a file
import os
import socket

class Consumer:
    path = ""
    port = -1

    #Instantiate with path to output file and port to listen on
    #Needs to be an Absolute Path to get proper saving functionality
    def __init__(self, path, port):
        self.path = path
        self.port = port

    #Call this function once and it will continuously process messages
    def consume(self):
        message = ""
        #Setting up Socket connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', self.port))

        while True:
            #Waiting for connection
            s.listen(1)
            print("Waiting for a connection...")
            connection, client_address = s.accept()

            #Accepting connection
            print('Connection Accepted from: ' + str(client_address[0]))
            message = connection.recv(1024)
            print("Recieved message: " + message.decode())

            #Write to file
            with open(self.path, 'a') as f:
                f.write(message.decode() + "\n")
                
            print("Message saved")
            message = ""

#Needs to be an Absolute Path to get proper saving functionality
c = Consumer("C:/Users/15ahl1/Desktop/Capstone/test.txt", 6969)
c.consume()
