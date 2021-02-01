import time
import Adafruit_DHT
import shutil

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 21

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
#        temperature = str(int(temperature))
#        humidity = str(int(humidity))
        with open("dht_source.csv", "a+") as f:
          f.write(f"{temperature},{humidity}\r\n")
          print("Written")
          shutil.move("dht_source.csv", "dht_data.csv")
    else:
        print("Failed to retrieve data from humidity sensor")

    time.sleep(5)
