#!/usr/bin/python3

# Get temperatur data from DS18B20
# Source: https://bigl.es/ds18b20-temperature-sensor-with-python-raspberry-pi/
# Install library: pip3 install w1thermsensor

import time, os
from w1thermsensor import W1ThermSensor
from OmegaExpansion import oledExp

print('Measuring temperature by DS18B20 sensor...')

status  = oledExp.driverInit()
if (status != 0):
    print('OLED init failed')
    exit()
status = oledExp.setTextColumns()

sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    print("DS18B20 temperature is {:2.1f} *C".format(temperature))
    status = oledExp.setCursor(6,0)
    status |= oledExp.write('DS18B20: '+format(temperature, '.1f')+' *C')
    if (status != 0):
        print('OLED output failed')
        break

    time.sleep(1)
