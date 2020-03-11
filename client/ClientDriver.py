# Driver Program to run on Raspberry Pi Bootup
# Written by Alastair Lewis

from client.Producer import Producer
from client.RecordMaker import RecordMaker


class ClientDriver():
    def __init__(self):
        # NEED TO BE SET TO HOST IP AND PORT
        self.HOSTIP = "192.168.2.14"
        self.HOSTPORT = 6969

        # Creating RecordMaker and Producer Objects
        self.r = RecordMaker()
        self.p = Producer(self.HOSTIP, self.HOSTPORT)

    def send_message(self, facilityCode, badgeNumb):
        # Checking for non-zero values
        if facilityCode != 0:
            record = self.r.createRecord(facilityCode, badgeNumb)
            self.p.sendRecord(record)
            print(record + " Sent")
