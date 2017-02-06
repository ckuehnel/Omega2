#!/bin/sh

uptime > UPT
MSG=`cat UPT`
echo -n Uptime:
echo "$MSG"

# Send data as Twitter direct message via IFTTT
curl --data "value1=$MSG" https://maker.ifttt.com/trigger/Uptime/with/key/dy0QeH-N3Ezfa4Ilst-r4F
