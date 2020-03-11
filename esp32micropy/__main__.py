import os
import sys
from warnings import warn, Warning

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
    print('Putting {} on ESP32 memory'.format(tempoargs[1]))
    os.system('ampy {} main.py'.format(tempoargs[1]))
    print('Put the file on memory')
elif "--":
   ...
