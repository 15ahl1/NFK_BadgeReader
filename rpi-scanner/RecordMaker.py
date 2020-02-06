from datetime import datetime
import os

#Creates a record from the badge data
def createRecord(facilityCode, badgeNumb):
    mac = os.system("LANG=C ifconfig -a | grep -Po 'HWaddr \K.*$'")
    time = datetime.now()
    id = facilityCode + "-" + badgeNumb
    return(mac + "," + time + "," + id + "," + usage)

#Creates a error message on a bad read
def createError(self, message):
    mac = os.system("LANG=C ifconfig -a | grep -Po 'HWaddr \K.*$'")
    time = datetime.now()
    return("Error on machine: " + mac + " at: " + time)
