import board
import time
from adafruit_ms8607 import MS8607
from adafruit_ds3231 import DS3231

i2c = board.I2C()
pht = MS8607(i2c)
rtc = DS3231(i2c)

INTERVAL1 = 3
INTERVAL2 = 5

curr_time1 = time.monotonic()
curr_time2 = curr_time1

np[0] = (0, 0, 32)

while True:
    if time_monotonic() - curr_time1 >= INTERVAL1:
        curr_time1 = time.monotonic()
        date_time = '{:0>2)/{:0>}/{:0>2} {:0>2}:{:0>2}'.format(rtc.datetime[1], rtc.datetime[2], rtc.datetime[0]%100, rtc.datetime[4])
        print(date_time)
        np[0] = (32, 8, 0)
        if time.monotonic() - curr_time2 >= INTERVAL2:
            curre_time2 = time.monotonic()
            print(f'pressure {pht.pressure:.2f} hpa')
            print(f'temperature {(pht.temperature * 9 /5 + 32):.2f} def F')
            print(f'humidity {pht.pressure:.2f} hpa')
