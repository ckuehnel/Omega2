#!/usr/bin/python3

# Reading weather data from openweathermap network

import urllib.request
import json, time

f = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Altendorf,CH&APPID=87286fed489ba6a8afcd81443138d510')
json_string = f.read()
parsed_json = json.loads(json_string)

#location = parsed_json['location']['city']
location = parsed_json['name']
temp_c  = parsed_json['main']['temp'] - 273.15
temp  = round(10*temp_c)/10
rel_hum = parsed_json['main']['humidity']
weather = parsed_json['weather'][0]['description']
station = parsed_json['id']
updated = parsed_json['dt']
print("Current temperature in {0:s} is {1:.1f} *C".format(location, temp))
print("Current relative humidity is {:d} %".format(rel_hum))
print("Weather is %s " % (weather))
print("Weather station is %s" % (station))
print("Last updated: ", end ="")
local_time = time.localtime(updated)
print(time.strftime("%Y-%m-%d %H:%M:%S", local_time)) 
f.close()

f = open("/home/TEMP","w")
f.write("{:.1f}".format(temp) + '\r\n')
f.close()

f = open("/home/HUMI","w")
f.write(str(rel_hum) + '\r\n')
f.close() 
