from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import sys
import os
import time

sys.path.append(os.getcwd() + '/modules')

# user imports
from pushBullet import PushBullet
from getMsg import *
from sendMsg import *
from updateSnowfall import *

def main():

	# update resorts snowfalls
	new_snow = updateSnowfall()

	if new_snow:
		# open users xml file to get api_key
		root = ET.parse('xml_files/users.xml').getroot()

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

			# RESORTS
			sendResortMsgs(user_data, p, devices)

			# WEATHER
			sendWeatherMsgs(user_data, p, devices)


if __name__ == '__main__':
	main()
