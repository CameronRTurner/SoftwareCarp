#!\usr\bin\env python 

import sys 

try:
	sys.argv[1] = float
	
except: 
	print(oh shiiittttt, that's not a number dude)



print('...converting fahrenheight to celcius')

celcius = float(sys.argv[1]) * (9 / 5) + 32
	
print(celcius)