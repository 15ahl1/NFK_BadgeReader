#Written by Alastair Lewis
#Creates Records to send to the database
from datetime import datetime
import json
import re
import uuid

class RecordMaker:
    machineID = ""

    def __init__(self):
        #Gets the MAC Address of the Scanner
        self.machineID = (':'.join(re.findall('..', '%012x' % uuid.getnode()))) 
    
    #Returns JSON of the form: {machine varchar(10), time dateTime, userID int};
    def createRecord(self, facilityCode, badgeNumber):
        #Creating the JSON structure using a dictionary
        record = {}
        record["machine"] = self.machineID
        record["time"] = str(datetime.now())
        record["userID"] = str(facilityCode) + "-" + str(badgeNumber)
        #Function creates a JSON record and returns it as a string
        return json.dumps(record)

    



