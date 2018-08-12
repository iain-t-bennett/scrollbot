# test IoT application
# read data from git file
# https://raw.githubusercontent.com/iain-t-bennett/scrollbot/master/example3.msg
# and show on scrollbot

import requests
import scrollphathd as sphd
import time

# as upside down in scrollbot
sphd.rotate(180) 

# check it works - cycle every pixel

for x in range(17):
    sphd.clear()
    for y in range(7):
        sphd.set_pixel(x, y, 0.25)
        time.sleep(0.05)        
        sphd.show()

# read string from website
link = "https://raw.githubusercontent.com/iain-t-bennett/scrollbot/master/example3.msg"
f = requests.get(link)

msg = f.text
sphd.write_string(msg)

for x in range(len(msg)*10):
    sphd.show()
    sphd.scroll(1)
    time.sleep(0.05)

# end of script
