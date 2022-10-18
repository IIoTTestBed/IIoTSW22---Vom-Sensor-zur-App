from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy.font import proportional, LCD_FONT
from luma.core.legacy import text
import time
from PIL import Image, ImageDraw 


class MyMatrix:

    def __init__(self, cascaded=2):
        serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(serial, cascaded=cascaded, block_orientation=0, rotate=2, blocks_arranged_in_reverse_order=True)

        self.test = 'Hello'
        self.pixelList = list()
    
    def letter(self, letter, matrix=1):
        with canvas(self.device) as draw:
            text(draw, (((matrix-1)*8), 0), letter, fill="white", font=proportional(LCD_FONT))
    
    def setPixel(self, x, y):
        with canvas(self.device) as draw:
            draw.point((x,y), fill="white")

    def showPixels(self):
        with canvas(self.device) as draw:
            draw.point(tuple(self.pixelList), fill="white")

    def pixel(self, x, y, state):
        if state == True or state == 1:
            if (x,y) in self.pixelList:
                self.pixelList[self.pixelList.index((x,y))] = (x,y)
            else:
                self.pixelList.append((x,y))
        else:
            if (x,y) in self.pixelList:
                self.pixelList.remove((x,y))
        self.showPixels()

    def hello(self):
        return self.test

    def showMessage(self, textString, sleepTime = 0.1):
        print(self.device.width)
        #self.device.width
        for i in range((len(textString)*6)):
            with canvas(self.device) as draw:
                text(draw, (i*-1, 0), textString, fill="white", font=proportional(LCD_FONT))
            time.sleep(sleepTime)

    def clear(self):
        self.pixelList = list()
        self.device.clear()
    
    def brightness(self, brightness):
        self.device.contrast(brightness)