from samplebase import SampleBase
from rgbmatrix import graphics
from datetime import datetime
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 21
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    temp = round(float((temperature*9/5)+32),1)
    humidity = round(float(humidity),1)
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
        textColor = graphics.Color(255, 0, 0)
        pos = 0
        my_text = now.strftime("%H:%M:%S:")
        while True:
#            offscreen_canvas.Clear()
            answer = "Hello world"
            graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, temp)
            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
