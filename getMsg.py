from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET

def getXml(resort):
    # parse xml file for resort data
    root = ET.parse('resort_info.xml').getroot()
    return root.find(resort)


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


def initValues():
    # initialize names to search in xml
    names = ['trails', 'lifts', 'surface', 'day', 'two_day', 'week']

    # initialize labels for message data
    labels = {names[0] : 'Open Trails: ', names[1] : 'Open Lifts: ', names[2] : 'Surface: ', names[3] : '24 Hour Snow: ', names[4] : '48 Hour Snow: ', names[5] : '7 Day Snow: '}

    return names, labels


def getConditionsMsg(table, resort_data):
    # get names and labels
    names, labels = initValues()

    # get the stats location info from xml
    stats = resort_data.find('stats')
    
    # initialize blank message
    msg = ''    

    # loop through and get data and add to message
    for name in names:
        # get the stat in the xml
        stat = stats.find(name)

        # CHECK IF STAT IS THERE, IF NOT DON'T INCLUDE
        if not stat:
            continue

        # get the location information for the data
        tag = stat.find('tag').text
        n = int(stat.find('n').text)

        # get the data from the soup using the xml's location data
        data = table.find_all(tag)[n].contents[0]

        # add data to the message
        msg = msg + labels[name] + data + '\n'

    return msg





##############
### BROKEN ###
##############

def killingtonWeather():
    
    
    # get the Times
    loc2 = raw_text.find("TIME") + 17
    loc_end2 = raw_text.find("TEMP") - 28
    msg = msg + "Time\n" + raw_text[loc2:loc_end2] + '\n'

    # get the Temps
    loc3 = raw_text.find("TEMP") + 17
    loc_end3 = raw_text.find("WIND DIR") - 28
    msg = msg + "Temp\n" + raw_text[loc3:loc_end3] + '\n'    

    # get the Precip Perct
    loc4 = raw_text.find("PROB PRECIP") + 17
    loc_end4 = raw_text.find("SNOW AMT") - 28
    msg = msg + "Prec\n" + raw_text[loc4:loc_end4] + '\n'    

    # get the Snowfall amount
    loc4 = raw_text.find("SNOW AMT") + 17
    loc_end4 = raw_text.find("$$") - 32
    msg = msg + "Snow\n" + raw_text[loc4:loc_end4]    
    
    return msg