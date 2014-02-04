from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import urllib

def getXml(location, resort):
    if resort:
        # parse xml file for resort data
        root = ET.parse('xml_files/resort_info.xml').getroot()
    else:
        # parse xml file for weather data
        root = ET.parse('xml_files/weather_info.xml').getroot()

    return root.find(location)

def getSoup(url):
    # get the page
    r = requests.get(url)

    # soup the data
    data = r.text
    return BeautifulSoup(data)


def getStatsTable(soup, resort_data):
    # get the appropriate table for the data
    tag = resort_data.find('tag').text
    tag_id = resort_data.find('tag_id').text
    # if the tag has an id use it not use just the tag
    if tag_id == '':
        table = soup.find(tag)
    else:
        table = soup.find(tag, id=tag_id)

    return table


def initResortValues():
    # initialize names to search in xml
    names = ['trails', 'lifts', 'surface', 'day', 'two_day', 'week']

    # initialize labels for message data
    labels = {names[0] : 'Open Trails: ', names[1] : 'Open Lifts: ', names[2] : 'Surface: ', names[3] : '24 Hour Snow: ', names[4] : '48 Hour Snow: ', names[5] : '7 Day Snow: '}

    return names, labels


def getConditionsMsg(table, resort_data):
    # get names and labels
    names, labels = initResortValues()

    # get the stats location info from xml
    stats = resort_data.find('stats')
    
    # initialize blank message
    msg = ''    

    # loop through and get data and add to message
    for name in names:
        # get the stat in the xml
        stat = stats.find(name)

        # check if stat is there, if not don't include
        if stat is None:
            continue

        # get the location information for the data
        tag = stat.find('tag').text
        n = int(stat.find('n').text)

        # get the data from the soup using the xml's location data
        data = table.find_all(tag)[n].contents[0]

        # add data to the message
        msg = msg + labels[name] + data + '\n'

    return msg



def getTreeRoot(url):

    # get xml file
    urllib.urlretrieve(url, 'xml_files/weather.xml')

    # get tree and root
    tree = ET.parse('xml_files/weather.xml')
    root = tree.getroot()

    return tree, root


def getWeatherTable(tree, root, weather_data):
    # get the appropriate table for the data
    tag = weather_data.find('tag').text
    tag_id = weather_data.find('tag_id').text
    # if the tag has an id use it not use just the tag
    if tag_id == '':
        table = root.find(tag)
    else:
        table = root.find(tag, id=tag_id)

    return table


###################
### Not Working ###
###################


def initWeatherValues():
    # initialize names to search in xml
    names = ['Time', 'Temp', 'Wind Dir', 'Precip', 'Snow Amt']

    # initialize labels for message data
    ##labels = {names[0] : 'Open Trails: ', names[1] : 'Open Lifts: ', names[2] : 'Surface: ', names[3] : '24 Hour Snow: ', names[4] : '48 Hour Snow: ', names[5] : '7 Day Snow: '}

    return names, labels


def getConditionsMsg(table, resort_data):
    # get names and labels
    names, labels = initResortValues()

    # get the stats location info from xml
    stats = resort_data.find('stats')
    
    # initialize blank message
    msg = ''    

    # loop through and get data and add to message
    for name in names:
        # get the stat in the xml
        stat = stats.find(name)

        # check if stat is there, if not don't include
        if stat is None:
            continue

        # get the location information for the data
        tag = stat.find('tag').text
        n = int(stat.find('n').text)

        # get the data from the soup using the xml's location data
        data = table.find_all(tag)[n].contents[0]

        # add data to the message
        msg = msg + labels[name] + data + '\n'

    return msg
