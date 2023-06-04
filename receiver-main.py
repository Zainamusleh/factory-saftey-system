# Imports go at the top
from microbit import *
import radio


radio.config(group=2)
radio.on()

while True:
    message = radio.receive()
    if message:
        display.scroll(message)  
        pin0.write_digital(1)
        sleep(2000)
