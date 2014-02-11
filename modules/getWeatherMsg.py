from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import urllib

def getTreeRoot(url):

    # get xml file
    urllib.urlretrieve(url, 'xml_files/weather.xml')

    # get tree and root
    tree = ET.parse('xml_files/weather.xml')
    root = tree.getroot()

    return tree, root


def getWeatherStats(root):
    # get the data tag
    data = root.find('data')
    # get the param tag
    param = data.find('parameters')

    # set up empty lists for the data
    time_periods = []
    maxs = []
    mins = []
    temps = []
    precip = []
    weather = []


    # get the names of the time periods
    for i in data.find('time-layout').findall('start-valid-time'):
        time_periods.append(i.attrib['period-name'])


    # get the max and min temps
    for i in param.findall('temperature'):
        for j in i.findall('value'):
            if i.attrib['type'] == 'maximum':
                maxs.append(int(j.text))
            else:
                mins.append(int(j.text))

    # make a temps array based maxes and mins mixed
    longer = max([maxs, mins], key=len)
    shorter = min([maxs, mins], key=len)

    j = 0
    k = 0
    # for i in the range of number of time_periods
    for i in range(len(time_periods)):
        if i % 2:
            temps.append(shorter[j]) 
            j += 1
        else:
            temps.append(longer[k])
            k += 1

    # get the probability of precip
    for i in param.find('probability-of-precipitation').findall('value'):
        if i.text is None:
            precip.append(0)
        else:
            precip.append(int(i.text))

    # get the text weather
    for i in param.find('weather').findall('weather-conditions'):
        weather.append(i.text)

    # create stats dictionary
    stats = {'time_periods':time_periods, 'temps':temps, 'precip':precip, 'weather':weather}

    return stats



###################
### Not Working ###
###################


def initWeatherValues():
    # initialize names to search in xml
    names = ['Time', 'Temp', 'Wind Dir', 'Precip', 'Snow Amt']

    # initialize labels for message data
    ##labels = {names[0] : 'Open Trails: ', names[1] : 'Open Lifts: ', names[2] : 'Surface: ', names[3] : '24 Hour Snow: ', names[4] : '48 Hour Snow: ', names[5] : '7 Day Snow: '}

    return names, labels


def getWeatherMsg(stats):
    # get names and labels
    names, labels = initResortValues()

    
    # initialize blank message
    msg = ''    

    # loop through and get data and add to message
    for i in range(len(stats['time_periods'])):
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
