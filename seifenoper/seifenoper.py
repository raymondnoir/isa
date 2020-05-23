

import time
import grovepi
import random

#button

button = 3

grovepi.pinMode(button,"INPUT")

while True:
    try:
        print(grovepi.digitalRead(button))
        if grovepi.digitalRead(button) == 1:
            print("hit!")
        time.sleep(2)

    except IOError:
        print ("Error")

