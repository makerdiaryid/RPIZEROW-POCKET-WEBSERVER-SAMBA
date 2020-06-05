import RPi.GPIO as GPIO

import time

import os

 

# Use the Broadcom SOC Pin numbers

# Setup the pin with internal pullups enabled and pin in reading mode.

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

 

# Our function on what to do when the button is pressed

def Shutdown(channel):

    print("Shutting Down")

    time.sleep(5)

    os.system("sudo shutdown -h now")

 

# Add our function to execute when the button pressed event happens

GPIO.add_event_detect(21, GPIO.FALLING, callback=Shutdown, bouncetime=2000)

 

# Now wait!

while 1:

    time.sleep(1)