#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from datetime import datetime
import time

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default=current_time)

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("fonts/tom-thumb.bdf")
        textColor = graphics.Color(0, 155, 0)
        pos = 0 #offscreen_canvas.width
#        current_time = now.strftime("%H:%M:%S")
#        my_text = now.strftime("%H:%M:%S")  #self.args.text

        while True:
#            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 5, textColor,now.strftime("%H:%M:%S"))
#            pos = 0
#            if (pos + len < 0):
#                pos = offscreen_canvas.width

#            time.sleep(1)
#            offscreen_canvas.Clear() 
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)
#            current_time=now.strftime("%H:%M:%S")
            graphics.DrawText(offscreen_canvas, font, pos, 11, graphics.Color(155, 0, 0),now.strftime("%H:%M:%S"))
            graphics.DrawText(offscreen_canvas, font, pos, 16, graphics.Color(0, 0, 155),"Text")
            time.sleep(1) 
#            pos = 0
    
# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
