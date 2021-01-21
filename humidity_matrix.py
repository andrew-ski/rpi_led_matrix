#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from datetime import datetime
import time
now = datetime.now()

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

        while True:
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
            graphics.DrawText(offscreen_canvas, font, pos, 5, graphics.Color(0, 155, 0),now.strftime("%H:%M:%S"))
            graphics.DrawText(offscreen_canvas, font, pos, 11, graphics.Color(155, 0, 0),now.strftime("%H:%M:%S"))
            graphics.DrawText(offscreen_canvas, font, pos, 16, graphics.Color(0, 0, 155),"Text")
            time.sleep(1) 
    
# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
