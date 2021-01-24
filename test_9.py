#!/usr/bin/env python

import sys
import time
import Adafruit_DHT
# Requires rgbmatrix installed via special procedure from
# https://github.com/hzeller/rpi-rgb-led-matrix
from datetime import datetime, timedelta
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from random import randint 

def make_matrix() -> RGBMatrix:
  options = RGBMatrixOptions()

  options.rows = 16
  options.cols = 32
#  options.chain_length = 1
#  options.parallel = 1
#  options.row_address_type = 0
#  options.multiplexing = 0
#  options.pwm_bits = 11
  options.brightness = 70
#  options.pwm_lsb_nanoseconds = 130
#  options.led_rgb_sequence = 'RGB'
#  options.pixel_mapper_config = ''
#  options.gpio_slowdown = 1
  options.drop_privileges = False
  return RGBMatrix(options=options)


def loop():
  matrix = make_matrix()
  offscreen_canvas = matrix.CreateFrameCanvas()
  now = datetime.now()
  delta = timedelta(seconds = 15)
  continuum = 0
  first_run = True
  frame = 1
#  font = graphics.Font()
#  font.LoadFont("./fonts/4x6.bdf")
#  textColor = graphics.Color(255, 255, 0)
#  my_text = 'Hello world'
  trigger_time = now + delta

  while True:
#    current_time = datetime().now.strftime("%I:%M")
    if (first_run == True) or (datetime.now() > trigger_time):
#      print("Loop Complete")
      trigger_time = datetime.now() + delta
      DHT_SENSOR = Adafruit_DHT.DHT22
      DHT_PIN = 21
      humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
      temp = str(int((temperature*9/5)+32))
#    print(temp, humidity)
      humidity=str(int(humidity))
      first_run = False
 #      print(f"now:{str(datetime.now())} trigger:{str(trigger_time)}")
    now = datetime.now()
    current_time = now.strftime("%H")
    if int(current_time) > 11:
      current_time = (f"{now.strftime('%I:%M')}P")
    else:
      current_time = (f"{now.strftime('%I:%M')}A")
    font = graphics.Font()
#    font.LoadFont("fonts/tom-thumb.bdf")
    font.LoadFont("fonts/5x8.bdf") 
    pos = 10
    color_time = graphics.Color(200, 160, 15)
    color_temp = graphics.Color(255, 42, 0)
    color_humidity = graphics.Color(0, 60, 225)
#    color_background = graphics.Color(3, 8, 5)
#    color_background = graphics.Color(0, 2, 5)
#    color_background = graphics.Color(0, 0, 0)

#    i = 0
#    for i in range(0, 16):
#        graphics.DrawLine(offscreen_canvas, 0, i, 32, i, color_background)
#        i += 1
#    time.sleep(.01)
#    time.sleep(5 * 1000 / 1000000.0)
#    usleep(5 * 1000)
#    time.sleep(.05)
    continuum += 1
    continuum %= 3 * 15

    red = 0
    green = 0
    blue = 0

    if continuum <= 15:
        c = continuum
        blue = 15 - c
        red = c
    elif continuum > 15 and continuum <= 30:
        c = continuum - 16
        red = 15 - c
        green = c
    else:
        c = continuum - 31
        green = 15 - c
        blue = c

    offscreen_canvas.Fill(red, green, blue)
#draw_clock
#    graphics.DrawLine(offscreen_canvas, 0, 6, 0, 4, color_time)
#    graphics.DrawLine(offscreen_canvas, 4, 6, 4, 4, color_time)
#    graphics.DrawLine(offscreen_canvas, 1, 3, 3, 3, color_time)
#    graphics.DrawLine(offscreen_canvas, 1, 7, 3, 7, color_time)
#    graphics.DrawLine(offscreen_canvas, 2, 4, 2, 5, color_time)
#    graphics.DrawLine(offscreen_canvas, 3, 5, 3, 5, color_time)

#draw_fire
   # graphics.DrawLine(offscreen_canvas, 2, 9, 2, 9, graphics.Color(80,40,0))
    #graphics.DrawLine(offscreen_canvas, 1, 10, 3, 10, graphics.Color(100,60,0))
   # graphics.DrawLine(offscreen_canvas, 0, 11, 4, 11, graphics.Color(120,80,0))
  #  graphics.DrawLine(offscreen_canvas, 0, 12, 4, 12, graphics.Color(175,75,0))
 #   graphics.DrawLine(offscreen_canvas, 0, 13, 4, 13, graphics.Color(200,50,0))
#    graphics.DrawLine(offscreen_canvas, 1, 14, 3, 14, graphics.Color(255,0,0))
    if frame == 1:
      graphics.DrawLine(offscreen_canvas,3, 9, 3, 9, graphics.Color(200,160,0))
      frame = randint(1,3)
    elif frame == 2:
      graphics.DrawLine(offscreen_canvas,4, 10, 4, 10, graphics.Color(200,60,0))
      frame = randint(1,3) 
    elif frame == 3:
      graphics.DrawLine(offscreen_canvas,0, 10, 0, 10, graphics.Color(255,0,0))
      frame = randint(1,3)
    graphics.DrawLine(offscreen_canvas,2, 13, 2, 13, graphics.Color(randint(100,200),randint(100,150),0))
    graphics.DrawLine(offscreen_canvas,1, 14, 3, 14, graphics.Color(randint(100,200),randint(100,150),0))
    graphics.DrawLine(offscreen_canvas,2, 11, 4, 13, graphics.Color(255,0,0))
    graphics.DrawLine(offscreen_canvas,0, 13, 2, 11, graphics.Color(255,0,0))
    graphics.DrawLine(offscreen_canvas,2, 12, 4, 14, graphics.Color(200,60,0))
    graphics.DrawLine(offscreen_canvas,0, 14, 2, 12, graphics.Color(200,60,0))
#draw_raindrop
    graphics.DrawLine(offscreen_canvas, 19, 9, 19, 9, color_humidity)
    graphics.DrawLine(offscreen_canvas, 18, 10, 20, 10, color_humidity)
    graphics.DrawLine(offscreen_canvas, 17, 11, 21, 11, color_humidity)
    graphics.DrawLine(offscreen_canvas, 17, 12, 21, 12, color_humidity)
    graphics.DrawLine(offscreen_canvas, 17, 13, 21, 13, color_humidity)
    graphics.DrawLine(offscreen_canvas, 18, 14, 20, 14, color_humidity)
#    graphics.DrawCircle(offscreen_canvas, 1, 1, 1, color_red)
#    graphics.DrawLine(offscreen_canvas, 0, 5, 32, 5, color_blue)

    graphics.DrawText(offscreen_canvas, font, 1, 7, color_time ,current_time)
    graphics.DrawText(offscreen_canvas, font, 6, 15, color_temp, f"{temp}")
    graphics.DrawText(offscreen_canvas, font, 23, 15, color_humidity, f"{humidity}")

    offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)

# Main function
if __name__ == "__main__":
  try:
    # Start loop
    print("Press CTRL-C to stop")
    loop()
  except KeyboardInterrupt:
    print("Exiting\n")
    sys.exit(0)
