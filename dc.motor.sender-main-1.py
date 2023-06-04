# Imports go at the top
from microbit import *
import radio
radio.config(group=2)
from ultrasonic import Ultrasonic
ultrasonic_sensor = Ultrasonic()
while True:

    distance_value = ultrasonic_sensor.measure_distance_cm()
    if distance_value>15:
        pin0.write_digital(1)
        pin1.write_digital(0)

    elif distance_value<=15:
        pin0.write_digital(0)
        pin1.write_digital(1)
        radio.send('danger')
        
        
    
        