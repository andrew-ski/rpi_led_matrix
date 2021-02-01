import os
import time
import Adafruit_DHT
import csv

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 21

#f = open('/home/pi/Projects/Matrix/test.csv', 'w')

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        csvOpen = open('/home/pi/Projects/Matrix/test.csv', 'w')
        c = csv.writer(csvOpen, dialect='excel')
        c.writerows([["test1","test2"],[str(int(humidity)),str(int(temperature))]])
#        f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
        print("written")
#        csvOpen.close()
    else:
        print("Failed to retrieve data from humidity sensor")

    time.sleep(1)
