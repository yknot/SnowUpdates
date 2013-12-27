from bs4 import BeautifulSoup
import requests


from pushbullet import PushBullet

from get_data import *


apiKey = open("api_key").read()
p = PushBullet(apiKey)
# Get a list of devices
devices = p.getDevices()

msg = getSnowStats('killington')

p.pushNote(devices[0]["id"], 'Killington Snow Report', msg)