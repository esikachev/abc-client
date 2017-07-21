#!/bin/bash -xe

git clone https://github.com/esikachev/abc-server
cd abc-server
tox -e venv -- abc-server -e ${GITHUB_USERNAME} -p ${GITHUB_PASSWORD} &> /tmp/server.log &
while true
do
  if [ -f /tmp/server.log ]
  then
    if [[ "$(grep -c "Running on" /tmp/server.log)" == 1 ]]; then break; fi
  fi
  sleep 2
cd -
fi
