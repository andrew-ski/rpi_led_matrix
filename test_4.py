#!/usr/bin/env python

import sys
import time
import Adafruit_DHT
# Requires rgbmatrix installed via special procedure from
# https://github.com/hzeller/rpi-rgb-led-matrix
from datetime import datetime
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics


def make_matrix() -> RGBMatrix:
  options = RGBMatrixOptions()

  options.rows = 16
  options.cols = 32
#  options.chain_length = 1
#  options.parallel = 1
#  options.row_address_type = 0
#  options.multiplexing = 0
#  options.pwm_bits = 11
  options.brightness = 100
#  options.pwm_lsb_nanoseconds = 130
#  options.led_rgb_sequence = 'RGB'
#  options.pixel_mapper_config = ''
#  options.gpio_slowdown = 1
  options.drop_privileges = False
  return RGBMatrix(options=options)


def loop():
  matrix = make_matrix()
  offscreen_canvas = matrix.CreateFrameCanvas()
#  font = graphics.Font()
#  font.LoadFont("./fonts/4x6.bdf")
#  textColor = graphics.Color(255, 255, 0)
#  my_text = 'Hello world'

  while True:
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 21
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    temp = (temperature*9/5)+32
    print(temp, humidity)
    temp=int(temp)
    humidity=int(humidity)
    temp = str(temp)
    humidity = str(humidity)
    now = datetime.now()
    current_time = now.strftime("%I:%M")
    font = graphics.Font()
    font.LoadFont("fonts/tom-thumb.bdf")
    color_time = graphics.Color(200, 160, 15)
    color_temp = graphics.Color(171, 28, 0)
    color_humidity = graphics.Color(0, 40, 150)
#    color_background = graphics.Color(3, 8, 5)
#    color_background = graphics.Color(0, 2, 5)
    color_background = graphics.Color(0, 0, 0)

    i = 0
    for i in range(0, 16):
        graphics.DrawLine(offscreen_canvas, 0, i, 32, i, color_background)
        i += 1
    pos = 10
#draw_clock
    graphics.DrawLine(offscreen_canvas, 4, 3, 4, 1, color_time)
    graphics.DrawLine(offscreen_canvas, 8, 3, 8, 1, color_time)
    graphics.DrawLine(offscreen_canvas, 5, 0, 7, 0, color_time)
    graphics.DrawLine(offscreen_canvas, 5, 4, 7, 4, color_time)
    graphics.DrawLine(offscreen_canvas, 6, 1, 6, 2, color_time)
    graphics.DrawLine(offscreen_canvas, 7, 2, 7, 2, color_time)

#draw_fire
    graphics.DrawLine(offscreen_canvas, 6, 5, 6, 5, graphics.Color(75,40,0))
    graphics.DrawLine(offscreen_canvas, 5, 6, 7, 6, graphics.Color(100,60,0))
    graphics.DrawLine(offscreen_canvas, 4, 7, 8, 7, graphics.Color(125,40,0))
    graphics.DrawLine(offscreen_canvas, 4, 8, 8, 8, graphics.Color(175,30,0))
    graphics.DrawLine(offscreen_canvas, 5, 9, 7, 9, graphics.Color(255,0,0))

#draw_raindrop
    graphics.DrawLine(offscreen_canvas, 6, 10, 6, 10, color_humidity)
    graphics.DrawLine(offscreen_canvas, 5, 11, 7, 11, color_humidity)
    graphics.DrawLine(offscreen_canvas, 4, 12, 8, 12, color_humidity)
    graphics.DrawLine(offscreen_canvas, 4, 13, 8, 13, color_humidity)
    graphics.DrawLine(offscreen_canvas, 5, 14, 7, 14, color_humidity)
#    graphics.DrawCircle(offscreen_canvas, 1, 1, 1, color_red)
#    graphics.DrawLine(offscreen_canvas, 0, 5, 32, 5, color_blue)

    graphics.DrawText(offscreen_canvas, font, pos, 5, color_time ,current_time)
    graphics.DrawText(offscreen_canvas, font, pos, 10, color_temp, f"{temp}F")
    graphics.DrawText(offscreen_canvas, font, pos, 15, color_humidity, f"{humidity}%")

    time.sleep(30)
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
