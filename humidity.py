import Adafruit_DHT
from datetime import datetime
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 21

while True:
	humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
	if humidity is not None and temperature is not None:
		temp=round((temperature*9/5)+32,1)
		humidity=round(humidity,1)
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		print(f"{current_time} | {temp}*F | {humidity}%")
		time.sleep(10)
	else:
		print("Failed to retrieve data from humidty sensor")
