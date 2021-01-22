#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from datetime import datetime

import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 21
humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
offscreen_canvas = self.matrix.CreateFrameCanvas()
graphics.DrawText(offscreen_canvas, graphics.Font(LoadFont("fonts/4x6.bdf")), 0, 11, graphics.Color(155, 0, 0),"Text")
#print(temperature)
#print(humidity)
temp=round(float((temperature*9/5)+32),1)
humidity=round(float(humidity),1)
print(temp, humidity)

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello World!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("fonts/4x6.bdf")
        textColor = graphics.Color(0, 155, 0)
        pos = 0 #offscreen_canvas.width
        now = datetime.now()
        DHT_SENSOR = Adafruit_DHT.DHT22
        DHT_PIN = 21
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        while True:
#            humidity = Adafruit_DHT.read_retry(DHT_SENSOR)
#            temperature = Adafruit_DHT.read_retry(DHT_PIN)

            if humidity is not None and temperature is not None:
                offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
                temperature = str(temperature)
                humidity = str(humidity)
                graphics.DrawText(offscreen_canvas, font, pos, 5, graphics.Color(0, 155, 0),now.strftime("%H:%M:%S"))
                graphics.DrawText(offscreen_canvas, font, pos, 11, graphics.Color(155, 0, 0),temperature)
                graphics.DrawText(offscreen_canvas, font, pos, 16, graphics.Color(0, 0, 155),humidity)
#                temp=round((temperature*9/5)+32,1)
#                humidity=round(humidity,1)
#                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f"{current_time} | {temperature}*C | {humidity}%")
#                print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
#                time.sleep(1) 
#                offscreen_canvas.Clear()    
            else:
                print("Failed to retrieve data from humidity sensor")
            time.sleep(1)    
# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
