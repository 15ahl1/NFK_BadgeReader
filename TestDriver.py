#This is a sample program to show how the records are made and sent from producer to consumer.
#In another terminal, run Consumer.py before running this
from client.Producer import Producer
from client.RecordMaker import RecordMaker

#Creates the record maker and sets the machine name to be Test Machine 1
r = RecordMaker()

#Creates the Message Producer and points it to localhost on port 6969
p = Producer("localhost", 6969)

#Producer sends the message created by the record maker with badgeID 12345
p.sendRecord(r.createRecord(22, 12345))

print("Done")
