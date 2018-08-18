# test IoT application
# read data from git file
# https://raw.githubusercontent.com/iain-t-bennett/scrollbot/master/example3.msg
# and show on scrollbot

#import scrollphathd as sphd
import time
import pyowm

from auth import owm_api_key

print(owm_api_key)

# create weather object

owm = pyowm.OWM(owm_api_key)

# as upside down in scrollbot
#sphd.rotate(180) 


# read data from owm website
# get weather

observation = owm.weather_at_place('Basel,CH')

w = observation.get_weather()

w.temp = w.get_temperature('celsius')

msg = "Temperature: " + str(w.temp['temp_min']) + " - " + str(w.temp['temp_max']) + " c"

print()
print(msg)

# add blank space so no immediate repeat
msg = msg + '         '

# sphd.write_string(msg)
# sphd.set_brightness(0.25)

# assume 4 pixels per char then add 17 for width of display 
# for x in range(len(msg)*4+17):
#    sphd.show()
#    sphd.scroll(1)
#    time.sleep(0.05)

print(msg)
# end of script
