#!/usr/bin/env python
#
# Info
# * http://pycurl.io/docs/latest/index.html
# * http://pycurl.io/docs/latest/quickstart.html
#
# * https://stackoverflow.com/questions/34192093/python-socket-get
#
# * https://wiki.ubuntuusers.de/Internetradio/Streamadressen_ermitteln/
# * http://www.radio-browser.info/gui/#/
# * http://www.radio-browser.info/webservice#station_url
# * http://www.radio-browser.info/webservice
# * http://www.radio-browser.info/backups/

import os
import os.path
import requests
import xml.etree.ElementTree as ET



#===============================================================================
#
#===============================================================================

# Variables
obj_request = ""



#===============================================================================
#
#===============================================================================

# Constants
DIC_PAYLOAD = {
    "name": "",
    "value": "",
    "stationcount": ""
}
#STR_URL = "http://www.radio-browser.info/webservice/xml/tags/jazz"
STR_URL = "http://www.radio-browser.info/webservice/xml/tags/jungle"

# Retrieve data from URL
obj_request = requests.post(STR_URL, data=DIC_PAYLOAD)

# Print parsed data
xml_root = ET.fromstring(obj_request.text.encode("utf-8"))
for child in xml_root:
    print (child.tag, child.attrib)



# Constants
DIC_PAYLOAD = {
    "id": "",
    "name": "",
    "url": "",
    "homepage": "",
    "favicon": "",
    "tags": "",
    "country": "",
    "state": "",
    "language": "",
    "votes": "",
    "negativevotes": "",
    "codec": "",
    "bitrate": "",
    "hls": "",
    "lastcheckok": "",
    "lastchecktime": "",
    "lastcheckoktime": "",
    "clicktimestamp": "",
    "clickcount": "",
    "clicktrend": "",
    "lastchangetime": "",
    "ip": ""
}
STR_URL = "http://www.radio-browser.info/webservice/xml/stations/bycountry/germany"

# Retrieve data from URL
obj_request = requests.post(STR_URL, data=DIC_PAYLOAD)
# Print parsed data
xml_root = ET.fromstring(obj_request.text.encode("utf-8"))

# Create path
str_path_dir = os.path.join(os.path.expanduser("~"), "Downloads")
if os.path.exists(str_path_dir):
    if os.path.isdir(str_path_dir):
        str_path_file = os.path.join(str_path_dir, "germany.txt")
# Write URLs to file
if str_path_file:
    with open(str_path_file, "w") as obj_file:
        for child in xml_root:
            #print (child.tag, child.attrib)
            #print (child.attrib["url"])
            #obj_file.write(child.attrib["name"] + "\t" + child.attrib["url"])
            obj_file.write(child.attrib["url"])
            #pass



#STR_URL = "http://www.radio-browser.info/webservice/xml/stations"







