#Written by Alastair Lewis
#Creates Records to send to the database
from datetime import datetime
import json

class RecordMaker:
    machineID = ""

    def __init__(self, machineID):
        self.machineID = machineID
    
    #Returns JSON of the form: {machine varchar(10), time dateTime, userID int};
    def createRecord(self, badgeNumber):
        #Creating the JSON structure using a dictionary
        record = {}
        record["machine"] = self.machineID
        record["time"] = str(datetime.now())
        record["userID"] = str(badgeNumber)
        #Function creates a JSON record and returns it as a string
        return json.dumps(record)

    



