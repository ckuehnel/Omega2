#!/bin/sh -e

echo "Initialize OLED..."
oled-exp -i
oled-exp -c

echo "Draw logo..."
oled-exp draw /root/onion.lcd
sleep 1
oled-exp -c

echo "Show date & time..."
d=`date +%d-%m-%Y`
t=`date +%H:%M`
oled-exp write $d 
oled-exp cursor 0,11 write $t


oled-exp cursor 2,0 write "Temp:"
read T < /home/TEMP
oled-exp cursor 2,7 write $T
oled-exp cursor 2,12 write "*C"

oled-exp cursor 3,0 write "Humi:"
read H < /home/HUMI
oled-exp cursor 3,7 write $H 
oled-exp cursor 3,10 write "% r.H."





