from site import PREFIXES
from time import sleep
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT
text = "Hello World!"
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=2, block_orientation=90, rotate=0, blocks_arranged_in_reverse_order=False)


show_message(device, text , fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)
sleep(1)


"""

import time
import argparse

from luma import led_matrix
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy.font import proportional, LCD_FONT

#def demo(w, h, block_orientation, rotate):
# create matrix device
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=8, height=8, rotate=0, block_orientation=-90)
matrix = led_matrix()

print("Created device")



with canvas(device) as draw:
  draw.rectangle(device.bounding_box, outline="white")
  text(draw, (2, 2), "Hello", fill="white", font=proportional(LCD_FONT))
  text(draw, (2, 10), "World", fill="white", font=proportional(LCD_FONT))

time.sleep(300)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='matrix_demo arguments',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--width', type=int, default=8, help='Width')
    parser.add_argument('--height', type=int, default=8, help='height')
    parser.add_argument('--block-orientation', type=int, default=-90, choices=[0, 90, -90], help='Corrects block orientation when wired verticall')
    parser.add_argument('--rotate', type=int, default=0, choices=[0, 1, 2, 3], help='Rotation factor')

    args = parser.parse_args()
"""

