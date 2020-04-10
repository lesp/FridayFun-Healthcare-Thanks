import board
import time
from digitalio import DigitalInOut, Direction

red = DigitalInOut(board.A0)
yellow = DigitalInOut(board.A3)
blue = DigitalInOut(board.A6)


red.direction = Direction.OUTPUT
yellow.direction = Direction.OUTPUT
blue.direction = Direction.OUTPUT


while True:
    blue.value = False
    red.value = True
    time.sleep(1)
    red.value = False
    yellow.value = True
    time.sleep(1)
    yellow.value = False
    blue.value = True
    time.sleep(1)
