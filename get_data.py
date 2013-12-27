from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET

def getSnowStats(resort):

    # parse xml file
    root = ET.parse('resort_info.xml').getroot()
    resort_data = root.find(resort)
    url = resort_data.find('url').text

    # get the page
    r = requests.get(url)

    # soup the data
    data = r.text
    soup = BeautifulSoup(data)

    # get the stats table
    tag = resort_data.find('tag').text
    tag_id = resort_data.find('tag_id').text
    if tag_id == '':
        table = soup.find(tag)
    else:
        table = soup.find(tag, id=tag_id)

    msg = ''    

    stats = resort_data.find('stats')

    # get Open Trails
    trails = stats.find('trails')
    tag = trails.find('tag').text
    n = int(trails.find('n').text)
    msg = msg + 'Open Trails: ' + table.find_all(tag)[n].contents[0] + '\n'

    # get Open Lifts
    lifts = stats.find('lifts')
    tag = lifts.find('tag').text
    n = int(lifts.find('n').text)
    msg = msg + 'Open Lifts: ' + table.find_all('td')[1].contents[0] + '\n'
    
    # get Surface Conditions
    surface = stats.find('surface')
    tag = surface.find('tag').text
    n = int(surface.find('n').text)
    msg = msg + 'Surface: ' + table.find_all('td')[4].contents[0] + '\n'

    # get 24 snow
    day = stats.find('day')
    tag = day.find('tag').text
    n = int(day.find('n').text)
    msg = msg + '24 Hour: ' + table.find_all('td')[5].contents[0] + '\n'

    # get 48 snow
    two_day = stats.find('two_day')
    tag = two_day.find('tag').text
    n = int(two_day.find('n').text)
    msg = msg + '48 Hour: ' + table.find_all('td')[6].contents[0] + '\n'

    # get 7 days snow
    week = stats.find('week')
    tag = week.find('tag').text
    n = int(week.find('n').text)
    msg = msg + '7 Days: ' + table.find_all('td')[7].contents[0]

    return msg

### BROKEN ###
def killingtonWeather():
    
    # get url and read in
    url = "http://www.erh.noaa.gov/btv/mountain/point/KILLINGTON.txt"
    raw_text = urllib.urlopen(url).read()
    
    
    
    msg = "Killington Weather Update\n"

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