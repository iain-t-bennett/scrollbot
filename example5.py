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
        msg = str(round((w.temp['temp_min'] + w.temp['temp_max'])/2, 0))
        # forecast

    # set message and flash to show awake
    sphd.clear()
    sphd.write_string(msg)
    sphd.set_brightness(0.25)
    sphd.show()
    time.sleep(0.1)

    sphd.clear()
    sphd.write_string(msg)
    sphd.set_brightness(0.25)
    sphd.set_pixel(14, 1, 0.25)
    sphd.show()
    time.sleep(0.1)

    time_since_update += 1

# end of script
