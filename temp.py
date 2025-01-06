import board
import time
from analogio import AnalogIn
import pwmio

pot = AnalogIn(board.A0)
y = 65535
x = 0

while True:
    p = pot.value
    a = (p/y) * 3.3
    x = (a-0.5) * 100
    b = x * (1.8) + 32.0
    print(b)
    time.sleep(0.3)
