from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import sys

# user imports
from pushBullet import PushBullet
from getMsg import *

# open users xml file to get api_key
root = ET.parse('users.xml').getroot()

if len(sys.argv) > 1:
	name = str(sys.argv[1])
else:
	name = 'Andrew Yale'

# set empy api key
apiKey = ''

for child in root:
	if child.attrib['name'] == name:
		user_data = child
		apiKey = child.find('api_key').text
		break

if apiKey == '':
	print 'User not found'
else:
	# make push bullet object with api key
	p = PushBullet(apiKey)
	# Get a list of devices
	devices = p.getDevices()

	# for each of those resorts the user has chosen
	for child in user_data.find('resorts'):
	    # set the resort value from the user_data
	    resort = child.text

        # get section of xml for the right resort
        resort_data = getXml(resort)

        # get the soup object of the website
        soup = getSoup(resort_data.find('url').text)

        # get the table for the snow stats
        table = getStatsTable(soup, resort_data)

        # get the conditions message
        msg = getConditionsMsg(table, resort_data)

    	# push the note to the device
    	p.pushNote(devices[0]['id'], resort_data.find('name').text + ' Snow Report', msg)