import os, platform
os.system("clear")
print("\x1b[1;92m[+] Checking Updates..."+"\n")
#os.system("git pull")
os.system("git pull")
bit = platform.architecture()[0]
if bit == '64bit':
	if not os.path.exists("Fahad.so"):		
		os.system(f'curl -L https://github.com/FADII143/FAHAD-XD/blob/main/Fahad.cpython-311.so?raw=true > Fahad.so')
		import Fahad
	else:
		import Fahad
else:
	print('\n\x1b[1;91m[×] Your Device is Not Supported This Tool !');exit()
  
