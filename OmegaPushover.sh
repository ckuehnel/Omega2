#!/bin/sh

#set -- "${1:-$(</dev/stdin)}" "${@:2}"

if [ $# -lt 1 ] 
then
  echo "Usage: ./OmegaPushover.sh <message>"
else
  msg=$1
  echo [$msg] will be pushed to mobile device

  curl -s \
    --form-string "token=aifqr........pjech3" \ # change to your data
    --form-string "user=uojfa.........jngg93" \ # change to your data
    --form-string "message=$msg" \
    https://api.pushover.net/1/messages.json
    echo
fi
