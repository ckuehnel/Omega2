#!/bin/sh

uptime > UPT
MSG=`cat UPT`
echo -n Uptime:
echo "$MSG"

curl --data "value1=$MSG" https://maker.ifttt.com/trigger/Uptime/with/key/dy0QeH-N3Ezfa4Ilst-r4F
#curl -X POST -H "Content-Type: application/json" -d '{"value1":$msg}' https://maker.ifttt.com/trigger/Uptime/with/key/dy0QeH-N3Ezfa4Ilst-r4F