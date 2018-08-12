# test to scroll a message

import scrollphathd as sphd
import time

# as upside down in scrollbot
sphd.rotate(180) 

# check it works - cycle every pixel

for x in range(17):
    sphd.clear()
    for y in range(7):
        sphd.set_pixel(x, y, 0.25)
    sphd.show()
    time.sleep(1/17.0)

# write a string

msg = 'This is a test'
sphd.write_string(msg)

for x in range(len(msg)*10):
    sphd.show()
    sphd.scroll(1)
    time.sleep(0.05)

# end of script
