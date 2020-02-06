# This runs when the raspberry pi startup
import pigpio
import Kafka
import RecordMaker, Wiegand

def handleSwipe(facility, card, err):
    if !err:
        RecordMaker.createRecord(facility, card)
    else:
        RecordMaker.createError(err)

if __name__ == "__main__":

    # Wiegand
    pi = pigpio.pi()
    w = Wiegand(pi, 14, 15, handleSwipe)