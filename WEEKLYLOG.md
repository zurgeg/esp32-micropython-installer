# This file logs each weekly build
## weekly_031220_0_1.tar.gz
Added full support for server
Also running needs to look like this:
```
esp32micropy --serverhost <PATH_TO_FOLDER> <PORT>
```
Where PATH_TO_FOLDER is the folder you are sharing.
You finally need to edit the samba config for your share to include:
```
[MYSHARENAME]
#Configure your share...
path: <PATH_TO_FOLDER>
```

