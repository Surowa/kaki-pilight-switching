#!/bin/bash

sudo pilight-send -p kaku_switch -i 25544186 -u 0 -f
sleep 2
mpg123 lamp1uit.mp3
exit