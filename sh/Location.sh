#!/bin/bash
if [ "$1" -eq "1" ]; then
    dconf write /org/gnome/system/location/enabled true
else
    dconf write /org/gnome/system/location/enabled false
fi
