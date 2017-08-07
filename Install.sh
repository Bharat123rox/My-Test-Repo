#!/usr/bin/sh
if [ -f "/etc/arch-release" ]; then
  sudo pacman -S python-pip
  pip install requests
  pip install bs4
else
  sudo apt-get install python3-pip
  sudo pip3 install requests
  sudo pip3 install bs4
fi
