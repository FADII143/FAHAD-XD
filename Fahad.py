import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from Fahad import Hxw_Main

    Hxw_Main()
