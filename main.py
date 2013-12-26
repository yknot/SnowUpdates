from bs4 import BeautifulSoup
import requests


from pushbullet import PushBullet

from killingtonSnow import *
#from killingtonWeather import *


apiKey = open("api_key").read()
p = PushBullet(apiKey)
# Get a list of devices
devices = p.getDevices()

msg = killingtonSnow()

p.pushNote(devices[0]["id"], 'Killington Snow Report', msg)