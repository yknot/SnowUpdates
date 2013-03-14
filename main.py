import smtplib

from killingtonSnow import *
from killingtonWeather import *

# set up smtp server
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()

# get password from local file
password = open("password").read()

# login to server
server.login( 'snowupdates@gmail.com', password )

# get the killington snow report msg
# msg = killingtonSnow()

# get the killington weather report msg
msg = killingtonWeather()

# get number from local file
number = open("number").read()

# use number to send message
server.sendmail( 'SnowUpdates', number , str(msg))
