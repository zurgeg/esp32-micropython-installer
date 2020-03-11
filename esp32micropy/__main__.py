import os
import sys
from warnings import warn, Warning
import urllib.request

try:
    os.system('ampy')
except:
    warnings.warn('AMPY is not installed or Python is not on PATH. Now installing', Warning)
    os.system('pip install adafruit-ampy')
try:
    os.system('esptool.py')
except:
    warnings.warn('ESPTool is not installed or Python is not on PATH. Now installing',Warning)
    os.system('pip install esptool')

print('Checked for dependencies.')

#Process commands
if "--bootfile" in sys.argv:
    tempoargs = sys.argv
    tempoargs.remove('--bootfile')
    print('Putting {} on ESP32 memory as the boot file'.format(tempoargs[1]))
    os.system('ampy {} put {} main.py'.format(tempoargs[1],tempoargs[2]))
    print('Put the file on memory!')
elif "--copy" in sys.argv":
   tempoargs = sys.argv
   tempoargs.remove('--copy')
   print('Putting {} on ESP32 memory'.format(tempoargs[1]))
   os.system('ampy {} put {} {}'.format(tempoargs[1], tempoargs[2],tempoargs[3]))
   print('Put that on memory!')
elif "--get" in sys.argv:
    tempoargs = sys.argv
    tempoargs.remove('--get')
    print('Getting that file')
    out = os.system('ampy {} get {}'.format(tempoargs[1],tempoargs[2]))
    print(out)
else:
    print('Installing MicroPython')
    f = input('Please Confirm. Yes: 1. No: 0')
    if int(f) == 1:
        print('Installing MicroPython... Do not unplug your board')
        print('Erasing Flash... Do not unplug your board')
        os.system('esptool.py --port {} erase_flash'.format(sys.argv[1]))
        print('Erased Flash. Downloading MicroPython... Do not unplug your board')
        
        
                  
