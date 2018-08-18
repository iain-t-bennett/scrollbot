# test IoT application
# read data from git file
# https://raw.githubusercontent.com/iain-t-bennett/scrollbot/master/example3.msg
# and show on scrollbot

import scrollphathd as sphd
import time
import pyowm

# contents of auth.py
# owm_api_key="api key from openweathermap.com"
from auth import owm_api_key

print(owm_api_key)

# create weather object

owm = pyowm.OWM(owm_api_key)

# as upside down in scrollbot
sphd.rotate(180)

str_len = 0
time_since_update = 20*60*10
scroll_x = 0

while True:
    # read data from owm website
    # get weather - only check every 5 minutes
    if time_since_update > 20*60*5:
        # 5 minutes since checked - get an update
        time_since_update = 0
        observation = owm.weather_at_place('Basel,CH')
        # current weather
        w = observation.get_weather()
        #  extract temperature
        w.temp = w.get_temperature('celsius')

        #  build message to scroll
        msg = "Temp" + str(((w.temp['temp_min'] + w.temp['temp_max'])/2)) + "c"
        # forecast
        fc = owm.three_hours_forecast('Basel,CH')

        if fc.will_have_rain():
            w.rain = fc.when_rain()[0]
            time.rain = w.rain.get_reference_time(timeformat='date')
            msg = msg + " rain at " + str(time.rain.hour) + "h"
        else:
            msg = msg + " No rain"

        # avoid immediate loop
        msg = msg + "     "
    # set message
    sphd.clear()
    str_len = sphd.write_string(msg)
    sphd.set_brightness(0.25)

    # do the scrolling
    sphd.scroll_to(scroll_x, 0)
    sphd.show()
    time.sleep(0.05)
    scroll_x += 1
    time_since_update += 1
    if scroll_x >= str_len:
        scroll_x = 0

# end of script
