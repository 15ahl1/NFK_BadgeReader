#Stub Class for Database written by: Alastair Lewis
#Michael Reinhart needs to update this file with any Database code that he needs
from host.app import writeUsageRecord
from host.app import machineStatus
import json

class Database:
    path = ""

    def __init__(self, path):
        self.path = path

    def writeRecord(self, record):
        record = json.loads(record)
        machine = record["machine"]
        time = record["time"]
        userID = record["userID"]
        writeUsageRecord(machine, time, userID)
        machineStatus(machine)
