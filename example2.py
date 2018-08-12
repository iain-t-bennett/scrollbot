# source https://learn.pimoroni.com/tutorial/tanya/santabot-xmas-timer
import datetime
import time
import signal
import scrollphathd
from scrollphathd.fonts import font5x7

str_len = 0
scroll_x = 0

while True:
    xmas = datetime.datetime(2018, 12, 25) - datetime.datetime.now()
    daysleft = xmas.days
    hoursleft = xmas.seconds/3600

    scrollphathd.set_brightness(0.5)
    scrollphathd.clear()

    str_len = scrollphathd.write_string("Ho ho ho! It's %i days and %i hours until xmas!" %(daysleft, hoursleft), x=0, y=0, font=font5x7)
    scrollphathd.scroll_to(scroll_x, 0)
    scrollphathd.show()
    time.sleep(0.05)
    scroll_x += 1
    if scroll_x >= str_len:
        scroll_x = 0
