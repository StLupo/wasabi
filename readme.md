# wasabi

Raspberry Pi + 5" touch hdmi LCD digital alarm clock/picture frame

RPi configuration
-----------------
raspbian install from official image

Packages:
python
python-qt4
xserver-xorg
qt4-dev-tools

*config hdmi screen: https://learn.adafruit.com/adafruit-5-800x480-tft-hdmi-monitor-touchscreen-backpack/raspberry-pi-config
*config windowless gui on boot: https://www.raspberrypi.org/forums/viewtopic.php?p=344408
*config touch screen: https://blog.ask-a.ninja/?p=48
*disable screensaver: http://raspberrypi.stackexchange.com/questions/2059/disable-screen-blanking-in-x-windows-on-raspbian
      also add the following to .xinitrc
	    xset s off         # don't activate screensaver
      xset -dpms         # disable DPMS (Energy Star) features.
      xset s noblank     # don't blank the video device


