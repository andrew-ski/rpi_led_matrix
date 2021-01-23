from samplebase import SampleBase
from datetime import datetime
import Adafruit_DHT
import time

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 21

while True:

    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    temp = (temperature)
    print(temp, humidity)
    temp = str(temp)
    humidity = str(humidity)

    class RunText(SampleBase):
        def __init__(self, *args, **kwargs):
            super(RunText, self).__init__(*args, **kwargs)

        def run(self):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S:")
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            font = graphics.Font()
            font.LoadFont("fonts/4x6.bdf")
            color_yellow = graphics.Color(200,200, 0)
            color_red = graphics.Color(200, 0, 0)
            color_blue = graphics.Color(0, 0, 255)
            pos = 0
            graphics.DrawText(offscreen_canvas, font, pos, 5,color_yellow , current_time)
            graphics.DrawText(offscreen_canvas, font, pos, 11, color_red, temp)
            graphics.DrawText(offscreen_canvas, font, pos, 16, color_blue, humidity) 
            time.sleep(1)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

    run_text = RunText()
    run_text.process()
    time.sleep(2)
    
