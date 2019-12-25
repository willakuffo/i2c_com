from smbus import SMBus
import time
bus = SMBus(1) #i2c port 1 /dev/12c-1

address = 0x8

while True:
	try:
		ledstate = input('Put LED in state : ')
		if ledstate == "1":
			bus.write_byte(address,0x1)#on
		elif ledstate =="0":
			bus.write_byte(address,0x0)
		elif ledstate =="b":
			while True:
				bus.write_byte(address,0x1)#on
				time.sleep(0.5)
				bus.write_byte(address,0x0)
				time.sleep(0.5)
				
		else:
			break
	except OSError:
		print("Possible disconnection of I/O pins") 
		break
		
		
