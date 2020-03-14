# esp32-micropython-installer
Stable: [![Build Status](https://travis-ci.com/zurgeg/esp32-micropython-installer.svg?branch=latest-stable)](https://travis-ci.com/zurgeg/esp32-micropython-installer)
Master: [![Build Status](https://travis-ci.com/zurgeg/esp32-micropython-installer.svg?branch=master)](https://travis-ci.com/zurgeg/esp32-micropython-installer)
Weekly: [![Build Status](https://travis-ci.com/zurgeg/esp32-micropython-installer.svg?branch=latest-weekly)](https://travis-ci.com/zurgeg/esp32-micropython-installer)
Easily install MicroPython on your ESP32 Board by running these commands:
```bash
pip install esp32-micropython-installer
esp32micropy <YourPort>
```
Or the latest build of esp32-micropython-installer (may be unstable):
```
pip install https://www.github.com/zurgeg/esp32-micropython-installer/master.tar.gz
```
Finally the weekly build
```
pip install https://www.github.com/zurgeg/esp32-micropython-installer/weekly_<MMDDYY>_<version>.tar.gz
```
You can also make a script run on boot of the controller:
```bash
esp32micropy --bootfile <port> <python-file>
```
or you can put a file:
```bash
esp32micropy --copy <port> <file> <destination>
```
You can also get a file:
```bash
esp32micropy --get <port> <file>
```

Finally on a Linux Machine, you can run an SMB server with the files so you can edit like it's a drive:
```bash
#Install samba and stuff
sudo esp32-micropy --serverhost <PORT> <SHARENAME>
```


### NOTE: This is just a wrapper around ```esptool.py``` and ```ampy``` to simplify stuff into a single module.
