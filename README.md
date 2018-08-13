# scrollbot
Web connected led display

## Preperation steps
* Download image from https://www.raspberrypi.org/downloads/raspbian/ and extract the zip file to get a .img file.
* Format SD card (overwrite format) using [SD formatter](https://www.sdcard.org/downloads/formatter_4/eula_mac/)
* Flash the image to the sd card using [Etcher](https://etcher.io/)
* Remove and reinsert sd card
* Save following files on boot volume
  * `ssh` empty with no extension
  * `wpa_supplicant.conf` with following contents
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
 
network={
	ssid="WiFi_SSID"
	psk="WiFi_Password"
}
```

## Initial login
General updates
* `passwd` to change default password
* `sudo raspi-config` to change settings
* `sudo apt-get update`
* `sudo apt-get upgrade -y`
* `sudo reboot`

Scrollbot libraries 
see https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-scroll-phat-hd
* `curl https://get.pimoroni.com/scrollphathd | bash`

Clone this repository to get the scripts
```
sudo apt install git
git clone https://github.com/iain-t-bennett/scrollbot
```
## Running a script
```
cd scrollbot
git pull
python example1.py
```
