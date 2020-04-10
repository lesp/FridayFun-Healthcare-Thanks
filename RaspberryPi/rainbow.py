from gpiozero import LED
from time import sleep

red = LED(17)
yellow = LED(27)
blue = LED(22)


while True:
    blue.toggle()
    red.toggle()
    sleep(1)
    yellow.toggle()
    red.toggle()
    sleep(1)
    blue.toggle()
    yellow.toggle()
    sleep(1)