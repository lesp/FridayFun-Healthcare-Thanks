from gpiozero import LED
from time import sleep

red = LED(17)
green = LED(27)
blue = LED(22)


while True:
    blue.off()
    red.toggle()
    sleep(1)
    green.toggle()
    red.toggle()
    sleep(1)
    blue.toggle()
    green.toggle()
    sleep(1)