#!/usr/bin/env bash
# transfer file using SCP
# ./0-transfer_file 1-install_nginx_web_server  18.210.14.47 ubuntu ~/.ssh/id_rsa

if [ "$#" -lt 3 ]; then
    echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
    exit
fi

PATH_TO_FILE=$1
IP=$2
USERNAME=$3
PATH_TO_SSH_KEY=$4

scp -o StrictHostKeyChecking=no -i "$PATH_TO_SSH_KEY" "$PATH_TO_FILE" "$USERNAME"@"$IP":~/
