from datetime import datetime
import os

class RecordMaker:
    #Creates link to the machine class and the kafka class
    def __init__(self, machineInput, kafkaInput):
        global machine = machineInput
        global kakfa = kafkaInput

    #Creates and sends a record from the badge data
    def createRecord(self, facilityCode, badgeNumb):
        mac = os.system("LANG=C ifconfig -a | grep -Po 'HWaddr \K.*$'")
        time = datetime.now()
        id = facilityCode + "-" + badgeNumb
        inUse = self.machine.inUse
        kafka.sendRecord(mac + "," + time + "," + id + "," + inUse)

    #Creates and sends a error message on a bad read
    def createError(self, message):
        mac = os.system("LANG=C ifconfig -a | grep -Po 'HWaddr \K.*$'")
        time = datetime.now()
        kakfa.sendRecord("Error: " + mac + " at time: " + time)
