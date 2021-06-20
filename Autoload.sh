#!/bin/bash
if [ "$1" -eq "0" ]; then
    sed -i "s/X-MATE-Autostart-Enabled=true/X-MATE-Autostart-Enabled=false/" /home/$USER/.config/autostart/run.sh.desktop;
else
    sed -i "s/X-MATE-Autostart-Enabled=false/X-MATE-Autostart-Enabled=true/" /home/$USER/.config/autostart/run.sh.desktop;
fi
