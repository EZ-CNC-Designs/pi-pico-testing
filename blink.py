from machine import Pin
import time
# Note that the file name needs to be "main.py" or it won't run

led = Pin("LED", Pin.OUT) # Sets Pin 16 as an output
light = Pin(16, Pin.OUT)


while True:
    led.value(1) # Turn LED "on"
    light.value(1)
    time.sleep(3) # Pause
    
    led.value(0) # Turn LED "off"
    light.value(0)
    time.sleep(3) # Pause