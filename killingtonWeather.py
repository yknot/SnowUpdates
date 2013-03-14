import urllib

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
