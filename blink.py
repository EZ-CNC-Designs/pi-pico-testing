from machine import Pin
import time
# Note that the file name needs to be "main.py" or it won't run (when saved on the Pico)

led = Pin("LED", Pin.OUT) # Sets LED as an output


while True:
    led.value(1) # Turn LED "on"
    time.sleep(3) # Pause
    
    led.value(0) # Turn LED "off"
    time.sleep(3) # Pause