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
