#!/bin/sh

echo "Send data to Thingspeak Server"

#Thingspeak
api_key='CRPX6X538QZ1DZHY'

DATE=date
read TEMP < /home/TEMP		
echo "Temperature   = $TEMP *C"
read HUMI < /home/HUMI		
echo "Rel. Humidity = $HUMI %"

curl --data \
     "api_key=$api_key&field1=$TEMP&field2=$HUMI&field3=$DATE" \
     https://api.thingspeak.com/update > log 2>&1
