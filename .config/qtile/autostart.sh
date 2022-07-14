#!/bin/bash

/usr/bin/nitrogen --restore &
/usr/bin/picom &

# REDSHIFT
/usr/lib/geoclue-2.0/demos/agent &
#redshift -t 6500:3100 &

# BLUETOOTH
/usr/bin/blueman-applet &

# KEYBOARD SPEED
/usr/bin/xset r rate 200 60

# KEYBOARD MAPPINGS
/usr/bin/xmodmap -e "keycode 134 = Escape"

# TRIPPLE MONITOR SETUP
/usr/bin/xrandr --output DP-4 --auto --primary --output HDMI-0 --auto --left-of DP-4 --output DP-0 --auto --right-of DP-4

