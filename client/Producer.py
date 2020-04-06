#Written by Alastair Lewis
#Produces messages and sends to Destination via Sockets
import os
import socket

class Producer:
    ipAddress = ""
    port = -1

    #Initialize with destination IP Address and Port
    def __init__(self, destinationIP, destinationPort):
        self.ipAddress = destinationIP
        self.port = destinationPort

    #Call this function with the record as the argument everytime you want to send a message
    def sendRecord(self, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ipAddress, self.port))
            s.sendall(message.encode('utf-8'))
            #print("Sending: " + message)
        except:
            print("Something went wrong trying to connect to server.")
        s.close()


# p = Producer("localhost", 6969)
# p.sendRecord("Test 02")
