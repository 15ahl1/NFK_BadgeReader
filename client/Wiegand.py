#!/usr/bin/env python
# Reads and converts wiegand codes to decimal format
import time
import pigpio

FAC_PAR_MASK = 0b10000000000000000000000000
FACILITY_MASK = 0b01111111100000000000000000
CARD_MASK = 0b00000000011111111111111110
CARD_PAR_MASK = 1


def bit_count(int_type):
    """
 Counts the number of bits in the passed in number
 :param int_type:
 :return:
 """
    count = 0
    while int_type:
        int_type &= int_type - 1
        count += 1
    return count


class Wiegand:
    """
    A class to read Wiegand codes of an arbitrary length.
    """
    def __init__(self, pi, gpio_0, gpio_1, callback, bit_timeout=5):
        """
        Instantiate with the pi, gpio for 0 data0 and gpio for data1
        """

        self.pi = pi
        self.gpio_0 = gpio_0
        self.gpio_1 = gpio_1

        self.callback = callback

        self.bit_timeout = bit_timeout

        self.in_code = False

        self.pi.set_mode(gpio_0, pigpio.INPUT)
        self.pi.set_mode(gpio_1, pigpio.INPUT)

        self.pi.set_pull_up_down(gpio_0, pigpio.PUD_UP)
        self.pi.set_pull_up_down(gpio_1, pigpio.PUD_UP)

        self.cb_0 = self.pi.callback(gpio_0, pigpio.FALLING_EDGE, self._cb)
        self.cb_1 = self.pi.callback(gpio_1, pigpio.FALLING_EDGE, self._cb)

        self.error_msg = None
        self.facility = None
        self.card = None

    def _cb(self, gpio, level, tick):
        """
        Accumulate bits until both gpios 0 and 1 timeout.
        """

        if level < pigpio.TIMEOUT:

            if self.in_code == False:
                self.num = 0

                self.in_code = True
                self.code_timeout = 0
                self.pi.set_watchdog(self.gpio_0, self.bit_timeout)
                self.pi.set_watchdog(self.gpio_1, self.bit_timeout)
            else:
                self.num = self.num << 1

            if gpio == self.gpio_0:
                self.code_timeout = self.code_timeout & 2  # clear gpio 0 timeout
            else:
                self.code_timeout = self.code_timeout & 1  # clear gpio 1 timeout
                self.num = self.num | 1

        else:

            if self.in_code:

                if gpio == self.gpio_0:
                    self.code_timeout = self.code_timeout | 1  # timeout gpio 0
                else:
                    self.code_timeout = self.code_timeout | 2  # timeout gpio 1

                if self.code_timeout == 3:  # both gpios timed out
                    self.pi.set_watchdog(self.gpio_0, 0)
                    self.pi.set_watchdog(self.gpio_1, 0)
                    self.in_code = False

                    # Call the call back

                    facility = (self.num & FACILITY_MASK) >> 17
                    card = (self.num & CARD_MASK) >> 1

                    fac_par = (self.num & FAC_PAR_MASK) >> 25
                    # even parity
                    fac_par_ok = (bit_count(facility) + fac_par) % 2 == 0

                    card_par = self.num & CARD_PAR_MASK
                    # odd parity
                    card_par_ok = (bit_count(card) + card_par) % 2 == 1

                    if fac_par_ok and card_par_ok:
                        self.facility = facility
                        self.card = card
                    else:
                        self.error_msg = "Error: Parity Check Failed"

                    self.callback(self.facility, self.card, self.error_msg)

    def cancel(self):
        """
        Cancel the Wiegand decoder.
        """

        self.cb_0.cancel()
        self.cb_1.cancel()



# if __name__ == "__main__":
#     # Remove later --- left in here to show whats needed
#     pi = pigpio.pi()

#     def callback(facilty, card, error):
#         print(card)
#         clientDriver.send_message(facilty, card)

#         if error:
#             print(error)

#     clientDriver = ClientDriver()

#     w = Wiegand(pi, 17, 18, callback)

#     time.sleep(300)

#     w.cancel()

#     pi.stop()
