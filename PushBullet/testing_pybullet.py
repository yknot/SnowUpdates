from pushbullet import PushBullet

apiKey = open("api_key").read()
p = PushBullet(apiKey)
# Get a list of devices
devices = p.getDevices()

# Send a note
p.pushNote(devices[0]["id"], 'Hello world', 'Test body')

# Send a map location
p.pushAddress(devices[0]["id"], "Eiffel tower", "Eeiffel tower, france")

# Send a list
p.pushList(devices[0]["id"], "Groceries", ["Apples", "Bread", "Milk"])

# Send a link
p.pushLink(devices[0]["id"], "Google", "http://www.google.com")

# Send a file
#p.pushLink(devices[0]["id"], "filename")