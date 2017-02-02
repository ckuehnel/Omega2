#!/bin/sh

#MQTT
BROKER="m20.cloudmqtt.com"
BRUSER="rawyjpid"
BRPASSW="ah52k3gjd8JS"
BRPORT=12394
TEMPTOP="OMEGA2/WU/temperature"
HUMITOP="OMEGA2/WU/humidity"

echo "Send data to MQTT Broker"

DATE="$(date +"%d-%m-%Y")"
read TEMP < /home/TEMP		
echo "Temperature   = $TEMP *C"
read HUMI < /home/HUMI		
echo "Rel. Humidity = $HUMI %"

mosquitto_pub -h $BROKER -u $BRUSER -P $BRPASSW -p $BRPORT -t $TEMPTOP -m $TEMP
mosquitto_pub -h $BROKER -u $BRUSER -P $BRPASSW -p $BRPORT -t $HUMITOP -m $HUMI
 

