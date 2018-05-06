# kaku-pilight-switching
Simple setup to switch kaki switches using pilight


This is a simple method to switch light using the kaku protocol on the Raspberry Pi 3

Connect the cheap chinese transceiver combo to VCC/GND and and the signal wires to the sixth (GPIO0) and seventh (GPIO2) from the upper left row.

Now, install the required software:

Sudo apt-get update
Sudo apt-get install pilight
Sudo pip install schedule

Now edit the pin layout en attached pins for pilight in:

sudo nano /etc/pilight/config.json

Make it so that it corresponds to your RPi type and the pin numbers you use. 

Now, we need to now the identification number of our kaku switches. 

For this, you need to start the pilight daemon

Sudo su && pilight-daemon -D

Now press one of the buttons on your remote to turn a light on. Youĺl notice the arctech-protocol, this is the one kaku uses. Write down the long number (25567534).
Now edit the shell scripts so the device number after -i matches yours.

Now, all that is left is to exit daemon with ctrl+c
and switch on lights by sending:

pilight-send -p kaku_switch -i <device number> -u <switch number> -t

-t means on, -f means off.

Once, you have edited the shell scripts, you can switch light on by only using shell commands like ./lamp1aan.sh
Or use the python scheduler script to have set times at which lights will turn on or off. 
