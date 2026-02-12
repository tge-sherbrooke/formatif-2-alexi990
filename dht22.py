# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "adafruit-circuitpython-dht>=4.0.10",
#     "rpi-gpio>=0.7.1",
# ]
# ///
import board
import adafruit_dht
import time

# Configuration du capteur
DHT_PIN = board.D4
dht = adafruit_dht.DHT22(DHT_PIN)

while True:
    try:
        temperature = dht.temperature
        humidite = dht.humidity

        print(f"Température: {temperature:.1f} °C")
        print(f"Humidité: {humidite:.1f} %RH")

        time.sleep(2)  # Minimum 2 secondes entre les lectures
    except RuntimeError as e:
        print(f"Erreur de lecture: {e}")
        time.sleep(2)
