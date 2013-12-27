from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET

from pushBullet import PushBullet
from getMsg import *

def sendResortMsgs(user_data, p, devices):
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

