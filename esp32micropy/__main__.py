import os
import sys
from warnings import warn 
import urllib.request

try:
    import ampy
except:
    print('AMPY is not installed or Python is not on PATH. Now installing')
    os.system('pip install adafruit-ampy')
try:
    import esptool
except:
    print('ESPTool is not installed or Python is not on PATH. Now installing')
    os.system('pip install esptool')

print('Checked for dependencies.')

#Process commands
if "--bootfile" in sys.argv:
    tempoargs = sys.argv
    tempoargs.remove('--bootfile')
    print('Putting {} on ESP32 memory as the boot file'.format(tempoargs[1]))
    os.system('ampy {} put {} main.py'.format(tempoargs[1],tempoargs[2]))
    print('Put the file on memory!')
elif "--copy" in sys.argv:
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
elif "--serverhost" in sys.argv:
    tempoargs = sys.argv
    tempoargs.remove('--serverhost')
    print('Now running...')
    prevf = None
    while True:
        f = open(tempoargs[1] + '/main.py')
        if f.readlines() == prevf:
            os.system('ampy {} put {} main.py'.format(tempoargs[2],tempoargs[1]+'/main.py'))
            prevf = f.readlines()
        else:
            #No Changes!
            pass
elif "--test" in sys.argv:
    os.system('ampy --help')
    os.system('esptool.py --help')
else:
    print('Installing MicroPython')
    f = input('Please Confirm. Yes: 1. No: 0')
    if int(f) == 1:
        print('Installing MicroPython... Do not unplug your board')
        print('Erasing Flash... Do not unplug your board')
        p1 = os.system('esptool.py --port {} erase_flash'.format(sys.argv[2]))
        print('Erased Flash. Downloading MicroPython... Do not unplug your board')
        url = 'http://micropython.org/resources/firmware/esp32-idf3-20191220-v1.12.bin'
        urllib.request.urlretrieve(url, 'micropython.bin')
        print('MicroPython Version: IDF3, Year: 2019, Month: 12, Day: 20')
        print('Downloaded MicroPython. Flashing MicroPython... DO NOT UNPLUG YOUR BOARD!')
        p2 = os.system('esptool.py --port {} --baud 460800 write_flash --flash_size=detect 0 micropython.bin'.format(sys.argv[1]))
        
                  
