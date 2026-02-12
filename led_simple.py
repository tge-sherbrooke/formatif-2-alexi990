# /// script
# requires-python = ">=3.9"
# dependencies = [
#   "adafruit-blinka",
#   "rpi-gpio"
# ]
# ///

import time
import board
import digitalio
import RPi.GPIO

# Définition des pins GPIO
led_rouge = digitalio.DigitalInOut(board.D17)
led_verte = digitalio.DigitalInOut(board.D27)
led_jaune = digitalio.DigitalInOut(board.D22)

# Mode sortie
led_rouge.direction = digitalio.Direction.OUTPUT
led_verte.direction = digitalio.Direction.OUTPUT
led_jaune.direction = digitalio.Direction.OUTPUT

while True:
    # Allume une LED à la fois
    led_rouge.value = True
    led_verte.value = False
    led_jaune.value = False
    time.sleep(1)

    led_rouge.value = False
    led_verte.value = True
    led_jaune.value = False
    time.sleep(1)

    led_rouge.value = False
    led_verte.value = False
    led_jaune.value = True
    time.sleep(1)