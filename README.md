# esp32-micropython-installer
Easily install MicroPython on your ESP32 Board by running these commands:
```bash
pip install esp32-micropython-installer
esp32-micropython-installer <YourPort>
```
You can also make a script run on boot of the controller:
```bash
esp32-micropython-installer --bootfile <python-file>
```
or you can put a file:
```bash
esp32-micropython-installer --copy <file> <destination>
```
You can also get a file:
```bash
esp32-micropython-installer --get <file>
```

Finally on a Linux Machine, you can run an SMB server with the files so you can edit like it's a drive:
```bash
#Install samba and stuff
sudo esp32-micropython-installer --serverhost <PORT> <SHARENAME>
```

### NOTE: This is just a wrapper around ```esptool.py``` and ```ampy``` to simplify stuff into a single module.
