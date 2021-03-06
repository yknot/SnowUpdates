from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET

from pushBullet import PushBullet
from getResortMsg import *
from getWeatherMsg import *

def sendResortMsgs(user_data, p, devices):
	# for each of those resorts the user has chosen
	for child in user_data.find('resorts'):
	    # set the resort value from the user_data
	    resort = child.text

        # get section of xml for the right resort
        resort_data = getXml(resort, 1)

        # get the soup object of the website
        soup = getSoup(resort_data.find('url').text)

        # get the table for the snow stats
        table = getStatsTable(soup, resort_data)

        # get the conditions message
        msg = getConditionsMsg(table, resort_data)

    	# push the note to the device
        p.pushNote(devices[0]['id'], resort_data.find('name').text + ' Snow Report', msg)



def sendWeatherMsgs(user_data, p, devices):
    # for each o the weather locations the user has chosen
    for child in user_data.find('weather'):
        # set the weather location from the user_data
        weather = child.text

        # get section of xml for the right weather location
        weather_data = getXml(weather, 0)

        # get the tree and root object of the website
        tree, root = getTreeRoot(weather_data.find('url').text)

        # get the weather info
        stats = getWeatherStats(root)

        # get weather message
        #msg = getWeatherMsg(table, weather_data)

        # push the note to the device
        #p.pushNote(devices[0]['id'], weather_data.find('name').text + ' Weather Report', msg)


