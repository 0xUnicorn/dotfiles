#!/usr/bin/env bash

TERMINAL=alacritty
INPUT=$HOME/Documents/vault/infrastructure/servers.txt

SERVER=$(printf '%s\n' "$(cat $INPUT)" | dmenu -i -l 10 -p 'Select host:')

IP=$(echo $SERVER | cut -d ' ' -f 3)

COMMAND="tmux new -A -s default"

$TERMINAL -e ssh -t $IP $COMMAND

