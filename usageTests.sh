#!/bin/bash

HTTP=$(which http)

if [ ! -x "$HTTP" ]; then
    echo 'You need HTTPie to run this script!'
    echo 'sudo pip3 install httpie'
    exit 1
fi

URL=:8080

set -x

http PUT :8080/default/default CHAOSHUB-TOKEN:123 < sample-journal.json
