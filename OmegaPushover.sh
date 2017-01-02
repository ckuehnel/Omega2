#!/bin/sh

#set -- "${1:-$(</dev/stdin)}" "${@:2}"

if [ $# -lt 1 ] 
then
  echo "Usage: ./OmegaPushover.sh <message>"
else
  msg=$1
  echo [$msg] will be pushed to mobile device

  curl -s \
    --form-string "token=aifqrmauecdjd7gwbj21mujnpjech3" \
    --form-string "user=uojfahpyozqtj6gbgccg61e5jngg93" \
    --form-string "message=$msg" \
    https://api.pushover.net/1/messages.json
    echo
fi
