#!/bin/sh

echo 'Abfrage Wetterdaten Altendorf SZ'

#./start.sh
./openweather.py
./oled.sh
#./send_message