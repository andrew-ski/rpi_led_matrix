#!/usr/bin/env python

import sys,argparse,csv
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
  options.brightness = 65
#  options.pwm_lsb_nanoseconds = 130
#  options.led_rgb_sequence = 'RGB'
#  options.pixel_mapper_config = ''
  options.gpio_slowdown = 4
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
  ch = 100
  ch_d = True
  f_y_r = 150
  f_y_d = True

  trigger_time = now + delta

  while True:

    with open ('dht_data.csv') as csv_file:
      csv_reader=csv.DictReader(csv_file,delimiter=',')
      line_count=0
      for row in csv_reader:
        temp=row["temperature"]
        humidity=row["humidity"]
      csv_file.close()

    now = datetime.now()
    current_time = now.strftime("%H")
    if int(current_time) > 11:
      current_time = (f"{now.strftime('%I:%M')}P")
    else:
      current_time = (f"{now.strftime('%I:%M')}A")
    font = graphics.Font()

    font.LoadFont("/home/pi/Projects/Matrix/fonts/5x8.bdf") 
    pos = 10
    color_time = graphics.Color(200, 160, 15)
    color_temp = graphics.Color(255, 42, 0)


    f_y_g = f_y_r/1.3
    f_yellow = graphics.Color(f_y_r, f_y_g, 0)

    if f_y_r > 200:
      f_o_r = randint(150,255)
    else:
      f_o_r = randint(75,150)

    f_o_g = f_o_r/4.25 
    f_orange = graphics.Color(f_o_r, f_o_g, 0)

    if f_y_r > 200:
      f_r_r = randint( 150, 255)

    else:
      f_r_r = randint(50, 150)
    f_r_g = f_r_r/25.5
    f_red = graphics.Color(f_r_r, f_r_g, 0)

    if f_y_r > 175:
      graphics.DrawLine(offscreen_canvas, 4, 12, 4 ,12, f_orange)       

    if f_y_r > 200:
      graphics.DrawLine(offscreen_canvas, 1, 8, 1, 8, f_red)

    if f_y_r > 225:
      graphics.DrawLine(offscreen_canvas, 0, 11, 0, 11, f_red)
   
    graphics.DrawLine(offscreen_canvas,2, 9, 2, 9, f_red)
    graphics.DrawLine(offscreen_canvas,1, 10, 1, 10, f_red)
    graphics.DrawLine(offscreen_canvas,0, 12, 0, 12, f_red)

    graphics.DrawLine(offscreen_canvas,3, 11, 3,12, f_orange)
    graphics.DrawLine(offscreen_canvas,2, 10, 2, 10, f_orange)
    graphics.DrawLine(offscreen_canvas,1, 12, 1, 11, f_orange)
    graphics.DrawLine(offscreen_canvas,0, 13, 0, 13, f_orange)

    graphics.DrawLine(offscreen_canvas,1, 14, 3, 14, f_yellow)
    graphics.DrawLine(offscreen_canvas,2, 11, 2, 11, f_yellow)
    graphics.DrawLine(offscreen_canvas,2, 12, 3, 12, f_yellow)
    graphics.DrawLine(offscreen_canvas,1, 13, 4, 13, f_yellow)
    graphics.DrawLine(offscreen_canvas,1, 14, 3, 14, f_yellow)

    if f_y_d == True and f_y_r < 255:
      f_y_r += 15
      if f_y_r ==  255:
         f_y_d = False
    if f_y_d == False and f_y_r > 90:
      f_y_r -= 15
      if f_y_r == 90:
        f_y_d = True
#draw_raindrop

#    for ch in range(10, 230):
    color_humidity = graphics.Color(0, (ch/3.75), ch)
    graphics.DrawLine(offscreen_canvas, 19, 9, 19, 9, color_humidity)
    graphics.DrawLine(offscreen_canvas, 18, 10, 20, 10, color_humidity)
    graphics.DrawLine(offscreen_canvas, 17, 11, 21, 11, color_humidity)
    graphics.DrawLine(offscreen_canvas, 17, 12, 21, 12, color_humidity)
    graphics.DrawLine(offscreen_canvas, 17, 13, 21, 13, color_humidity)
    graphics.DrawLine(offscreen_canvas, 18, 14, 20, 14, color_humidity)

    if ch_d == True and ch < 220:
      ch += 10
      if ch == 220:
        ch_d = False
    elif ch_d == False and ch > 100:
      ch -= 10
      if ch == 100:
        ch_d = True
#    graphics.DrawCircle(offscreen_canvas, 1, 1, 1, color_red)
#    graphics.DrawLine(offscreen_canvas, 0, 5, 32, 5, color_blue)

    graphics.DrawText(offscreen_canvas, font, 1, 7, color_time ,current_time)
    graphics.DrawText(offscreen_canvas, font, 6, 15, color_temp, f"{temp}")
    graphics.DrawText(offscreen_canvas, font, 23, 15, graphics.Color(0,60,225), f"{humidity}")

    offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
    time.sleep(5)
    offscreen_canvas.Clear()

# Main function
if __name__ == "__main__":
  try:
    # Start loop
    print("Press CTRL-C to stop")
    loop()
  except KeyboardInterrupt:
    print("Exiting\n")
    sys.exit(0)

