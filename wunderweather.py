#!/usr/bin/python

# Reading weather data from wunderground network

import urllib2
import json

f = urllib2.urlopen('http://api.wunderground.com/api/a50aba1a6119706f/geolookup/conditions/q/Switzerland/Altendorf.json')
json_string = f.read()
parsed_json = json.loads(json_string)

location = parsed_json['location']['city']
temp_c  = parsed_json['current_observation']['temp_c']
rel_hum = parsed_json['current_observation']['relative_humidity']
weather = parsed_json['current_observation']['weather']
station = parsed_json['current_observation']['station_id']
updated = parsed_json['current_observation']['observation_time_rfc822']
print("Current temperature in %s is: %s *C" % (location, temp_c))
print("Current relative humidity is: %s %%" % (rel_hum))
print("Weather is %s " % (weather))
print("Weather station is %s" % (station))
print("Last updated: %s" % (updated))

f.close()

f = open("TEMP","w")
f.write(str(temp_c))
f.close()

f = open("HUMI","w")
f.write(str(rel_hum))
f.close() 
