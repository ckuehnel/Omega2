#!/bin/sh

DISPLAY=/dev/ttyUSB0
stty < $DISPLAY 9600 # MicroView initialization in SeriaDisplay.ino

if [ "$(ls $DISPLAY)" ]; then
  read TEMP < /home/TEMP
  read HUMI < /home/HUMI
  echo "D $TEMP $HUMI" > $DISPLAY
fi







