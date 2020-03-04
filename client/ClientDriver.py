#Driver Program to run on Raspberry Pi Bootup
#Written by Alastair Lewis
from Producer import Producer
from RecordMaker import RecordMaker

#Stub method to simulate badge scans
import random as rand
def badgeScan():
    if rand.randint(0, 10) == 0:
        return (123, 54321)
    return (0,0)

#NEED TO BE SET TO HOST IP AND PORT
HOSTIP = "127.0.0.1"
HOSTPORT = 6969

#Creating RecordMaker and Producer Objects
r = RecordMaker()
p = Producer(HOSTIP, HOSTPORT)

while True:
    #On Callback function run:
    facilityCode, badgeNumb = badgeScan()

    #Checking for non-zero values
    if facilityCode != 0:
        record = r.createRecord(facilityCode, badgeNumb)
        p.sendRecord(record)
        print(record + " Sent")

