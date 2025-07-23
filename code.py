import board
import displayio
import framebufferio
import rgbmatrix
import math
import random
import time
import adafruit_imageload
displayio.release_displays()
MATRIX = rgbmatrix.RGBMatrix(
    width=32, height=16, bit_depth=6, tile=1, serpentine=True,
     rgb_pins=[board.IO7, board.IO8, board.IO9, board.IO10, board.IO11, board.IO12],
    addr_pins=[board.IO18, board.IO17, board.IO16],
    clock_pin=board.IO13,
    latch_pin=board.IO15,
    output_enable_pin=board.IO14,)

# Associate matrix with a Display to use displayio features
DISPLAY = framebufferio.FramebufferDisplay(MATRIX, auto_refresh=False,
                                           rotation=0)


# Load BMP image, create Group and TileGrid to hold it
#FILENAME = "ruby.bmp"
FILENAME = "ruby.bmp"
# CircuitPython 6 & 7 compatible
BITMAP = displayio.OnDiskBitmap(open(FILENAME, "rb"))
TILEGRID = displayio.TileGrid(
    BITMAP,
    pixel_shader=getattr(BITMAP, 'pixel_shader', displayio.ColorConverter()),
    tile_width=BITMAP.width,
    tile_height=BITMAP.height
    
)

# # CircuitPython 7+ compatible
# BITMAP = displayio.OnDiskBitmap(FILENAME)
# TILEGRID = displayio.TileGrid(
#     BITMAP,
#     pixel_shader=BITMAP.pixel_shader,
#     tile_width=BITMAP.width,
#     tile_height=BITMAP.height
# )

GROUP = displayio.Group()
GROUP.append(TILEGRID)
DISPLAY.root_group = GROUP
DISPLAY.refresh()

# Nothing interactive, just hold the image there
while True:
    pass