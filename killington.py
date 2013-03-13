import urllib
import BeautifulSoup
import smtplib

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()

password = open("password").read()

server.login( 'snowupdates@gmail.com', password )

url = "http://feeds.feedburner.com/KillingtonSnowReport?format=xml"

raw_text = urllib.urlopen(url).read()

text = BeautifulSoup.BeautifulSoup(raw_text)
items = text.findAll("item")
result = items[0].find("description").text

msg = "Killington Snow Update\n"

# number of trails
loc1 = result.find("/&gt;Open Trails: ") + 18
loc_end1 = result.find("&lt;br /&gt;Open Lifts: ")
msg = msg + "Number of Trails " + result[loc1:loc_end1] + '\n'

# 24 hour snowfall
loc2 = result.find("/&gt;24 Hour Snowfall: ") + 23
loc_end2 = result.find("&amp;quot;&lt;br /&gt;48 Hour Snowfall: ")
msg = msg + "24 Hour Snowfall " + result[loc2:loc_end2] + '"\n'

# 48 hour snowfall
loc3 = result.find("/&gt;48 Hour Snowfall: ") + 23
loc_end3 = result.find("&amp;quot;&lt;br /&gt;7 Day Snowfall: ")
msg = msg + "48 Hour Snowfall " + result[loc3:loc_end3] + '"\n'

# 7 day snowfall
loc4 = result.find("/&gt;7 Day Snowfall: ") + 21
loc_end4 = result.find("&amp;quot;&lt;br /&gt;&lt;br")
msg = msg + "7 Day Snowfall " + result[loc4:loc_end4] + '"\n'

number = open("number").read()
server.sendmail( 'SnowUpdates', number , str(msg))
