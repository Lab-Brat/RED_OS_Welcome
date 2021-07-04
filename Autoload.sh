#!/bin/bash

# for RED_OS
#if [ "$1" -eq "0" ]; then
#    sed -i "s/X-MATE-Autostart-Enabled=true/X-MATE-Autostart-Enabled=false/" /home/$USER/.config/autostart/run.sh.desktop;
#else
#    sed -i "s/X-MATE-Autostart-Enabled=false/X-MATE-Autostart-Enabled=true/" /home/$USER/.config/autostart/run.sh.desktop;
#fi

# for Ubuntu 21.04
if [ "$1" -eq "0" ]; then
    sed -i "s/X-GNOME-Autostart-enabled=true/X-GNOME-Autostart-enabled=false/" /home/$USER/.config/autostart/redos.desktop;
else
    sed -i "s/X-GNOME-Autostart-enabled=false/X-GNOME-Autostart-enabled=true/" /home/$USER/.config/autostart/redos.desktop;
fi
