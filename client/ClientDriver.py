# Driver Program to run on Raspberry Pi Bootup
# Written by Alastair Lewis


from Producer import *
from RecordMaker import *
from Wiegand import *
import pigpio

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


if __name__ == "__main__":
    # Remove later --- left in here to show whats needed
    print("run")
    pi = pigpio.pi()

    def callback(facilty, card, error):
        print(card)
        clientDriver.send_message(facilty, card)

        if error:
            print(error)

    clientDriver = ClientDriver()

    w = Wiegand(pi, 17, 18, callback)

    time.sleep(300)

    w.cancel()

    pi.stop()

