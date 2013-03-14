import smtplib

from killington import *

# set up smtp server
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()

# get password from local file
password = open("password").read()

# login to server
server.login( 'snowupdates@gmail.com', password )

# get the message
msg = killingtonSnow()

# get number from local file
number = open("number").read()

# use number to send message
server.sendmail( 'SnowUpdates', number , str(msg))
