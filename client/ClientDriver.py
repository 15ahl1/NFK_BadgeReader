# Driver Program to run on Raspberry Pi Bootup
# Written by Alastair Lewis & JD

import os
import configparser
from Producer import *
from RecordMaker import *
from Wiegand import *
import pigpio

class ClientDriver():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('../config.ini')
        # NEED TO BE SET TO HOST IP AND PORT
        self.HOSTIP = self.config["Server"]["IP"]
        self.HOSTPORT = int(self.config["Server"]["Port"])

        # Creating RecordMaker and Producer Objects
        self.r = RecordMaker()
        self.p = Producer(self.HOSTIP, self.HOSTPORT)

    def send_message(self, facilityCode, badgeNumb):
        # Checking for non-zero values
        if facilityCode != 0:
            record = self.r.createRecord(facilityCode, badgeNumb)
            self.p.sendRecord(record)
            print(record + " Sent")


if __name__ == "__main__":
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Remove later --- left in here to show whats needed
    print("run")
    pi = pigpio.pi()

    def callback(facilty, card, error):
        print(card)
        clientDriver.send_message(facilty, card)

        if error:
            print(error)

    clientDriver = ClientDriver()

    data0 = int(clientDriver.config["Pi"]["Data0"])
    data1 = int(clientDriver.config["Pi"]["Data1"])

    w = Wiegand(pi, data0, data1, callback)

    while True:
        pass

    w.cancel()

    pi.stop()

