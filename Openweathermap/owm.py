#!/usr/bin/python3

# File: owm.py
# Reading weather data from openweathermap network and compare with temperature local measured by DS18B20 sensor
# Install library: pip3 install w1thermsensor
# Data will be saved at Google spreadsheet 
# Claus Kuehnel 2019-04-14 info@ckuehnel.ch

import urllib.request
import urllib.parse
import json, time, os, datetime
from w1thermsensor import W1ThermSensor
from OmegaExpansion import oledExp

print('Get weather data from OpenWeatherMap....')

status  = oledExp.driverInit()
if (status != 0):
    print('OLED init failed')
    exit()

status = oledExp.drawFromFile("/root/onion.lcd")
time.sleep(1)
status = oledExp.clear()
status = oledExp.setTextColumns()

now = datetime.datetime.now()
#time_now = (now.year, now.month, now.day, now.hour, now.minute, now.second)
time_now = '{0:4d}-{1:2d}-{2:2d} {3:2d}:{4:2d}'.format(now.year, now.month, now.day, now.hour, now.minute)
print('Time is ' + time_now)

f = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Altendorf,CH&APPID=87286fed489ba6a8afcd81443138d510')
json_string = f.read()
parsed_json = json.loads(json_string)

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

status = oledExp.setCursor(0,0)
status |= oledExp.write(time_now)
status = oledExp.setCursor(2,0)
status |= oledExp.write('Temp: '+format(temp, '.1f')+' *C')
status = oledExp.setCursor(3,0)
status |= oledExp.write('Humi: '+format(rel_hum, 'd')+' %r.H.')

print('Measuring temperature by DS18B20 sensor...')

sensor = W1ThermSensor()

temperature = sensor.get_temperature()
print("DS18B20 temperature is {:2.1f} *C".format(temperature))
status = oledExp.setCursor(6,0)
status |= oledExp.write('DS18B20: '+format(temperature, '.1f')+' *C')
if (status != 0):
	print('OLED output failed')

print('Send data to Google Spreadsheet via IFTTT...')

# URL: maker.ifttt.com/trigger/{event}/with/key/{key}?value1=123,value2=456
f = urllib.request.urlopen('https://maker.ifttt.com:443/trigger/OpenWeatherMap/with/key/cH2dAcDITUgU6arFVkraet?value1=' + format(temp, '.1f') + '&value2=' + format(temperature, '.1f'))
print(f.read().decode())

print('Send data to Thingspeak for visualization...')

delta = temp - temperature
f = urllib.request.urlopen('https://api.thingspeak.com/update?api_key=81PB0NN208TQRTG1&field1=' + format(temp, '.1f') + '&field2=' + format(temperature, '.1f') + '&field3=' + format(delta, '.1f'))
print(f.read().decode())

print('Done.')
    
exit()
