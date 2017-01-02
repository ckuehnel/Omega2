#!/bin/sh

uptime > UPT
MSG=`cat UPT`
echo -n Uptime:
echo "$MSG"

/home/OmegaPushover.sh "$MSG"
