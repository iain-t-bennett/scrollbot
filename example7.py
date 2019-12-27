# test IoT application
# read data from twitter
# and show on scrollbot

import scrollphathd as sphd
import time
import sys
import requests

# as upside down in scrollbot
sphd.rotate(180)

# check it works - light every pixel

for x in range(17):
    for y in range(7):
        sphd.set_pixel(x, y, 0.25)
sphd.show()
time.sleep(0.5)
sphd.clear()
sphd.show()

msg = sys.argv[1]
# add blank space so no immediate repeat
msg = msg + '        '

sphd.write_string(msg)
sphd.set_brightness(0.2)

# assume 4 pixels per char then add 17 for width of display 
while True:
    # assume 4 pixels per char then add 17 for width of display
    for x in range(len(msg)*4+17):
        sphd.show()
        sphd.scroll(1)
        time.sleep(0.05)
