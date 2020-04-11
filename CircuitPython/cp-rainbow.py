import board
import time
from digitalio import DigitalInOut, Direction

red = DigitalInOut(board.A3)
green = DigitalInOut(board.A2)
blue = DigitalInOut(board.A1)


red.direction = Direction.OUTPUT
green.direction = Direction.OUTPUT
blue.direction = Direction.OUTPUT


while True:
    blue.value = False
    red.value = True
    time.sleep(1)
    red.value = False
    green.value = True
    time.sleep(1)
    green.value = False
    blue.value = True
    time.sleep(1)