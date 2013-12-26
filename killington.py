from bs4 import BeautifulSoup
import requests

def killingtonSnow():
    
    # get the page
    url = 'http://www.killington.com/winter/mountain/conditions/index.html'
    r = requests.get(url)

    # soup the data
    data = r.text
    soup = BeautifulSoup(data)

    # get the stats table
    table = soup.find('table', id='snow_report_stats')

    msg = ''    

    # get Open Trails
    msg = msg + 'Open Trails: ' + table.find_all('td')[0].contents[0] + '\n'

    # get Open Lifts
    msg = msg + 'Open Lifts: ' + table.find_all('td')[1].contents[0] + '\n'
    
    # get Surface Conditions
    msg = msg + 'Surface: ' + table.find_all('td')[4].contents[0] + '\n'

    # get 24 snow
    msg = msg + '24 Hour: ' + table.find_all('td')[5].contents[0] + '\n'

    # get 48 snow
    msg = msg + '48 Hour: ' + table.find_all('td')[6].contents[0] + '\n'

    # get 7 days snow
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