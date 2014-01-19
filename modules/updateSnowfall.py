from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import time

from getMsg import *

def updateSnowfall():

	# get resorts
	root = ET.parse('xml_files/resort_info.xml').getroot()

	for resort in root:

		# soup the resort
		soup = getSoup(resort.find('url').text)

		# get the table for the snow stats
		table = getStatsTable(soup, resort)

		stats = resort.find('stats')

		# get the stat in the xml
		stat = stats.find('day')

		# check if stat is there, if not don't include
		if stat is None:
			continue

		# get the location information for the data
		tag = stat.find('tag').text
		n = int(stat.find('n').text)

		# get the data from the soup using the xml's location data
		data = table.find_all(tag)[n].contents[0]

		# turn into int
		data = int(data[:data.find('"')])

		hour = time.strftime('%H')
		prev_hour = int(hour) - 1

		tree = ET.parse('xml_files/hourly.xml')
		hours = tree.getroot()
		prev_snow = hours.find('n' + str(prev_hour)).find(resort.tag).text

		hours.find('n' + hour).find(resort.tag).text = str(data)
		tree.write('xml_files/hourly.xml')

		if data - int(prev_snow) > 0:
			return 1
		else:
			return 0




