#Stub Class for Database written by: Alastair Lewis
#Michael Reinhart needs to update this file with any Database code that he needs

class Database:
    path = ""

    def __init__(self, path):
        self.path = path

    def writeRecord(self, record):
        print("Uploading " + record + " to Database")

