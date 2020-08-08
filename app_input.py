import serial, json
from pynput.keyboard import Key, Controller

keys = [ #define keys that will be used
	'd',
	'f',
	'j',
	'k' ]
	
button_label = [ #label of the button, must be same as written on the arduino side
	'LeftO',
	'LeftI',
	'RightI',
	'RightO' ]

is_pressed = {} #declare a blank dict for state of the keys
	
for x,y in zip(button_label, keys) : #wrap the keys & button_label strings with single-quote
	x = "\'" + x + "\'"
	y = "\'" + y + "\'"

for x in keys : #populate the is_pressed dict with keys list and adding boolean
	is_pressed[x] = False
	
serial_port = input('Please enter your Arduino port: ')
baud_rate = input('Please enter the baud rate: ')
ser = serial.Serial(serial_port, baud_rate) #initiate serial
keyboard = Controller()

while True:
	try:
		data = json.loads(ser.readline().decode('utf-8')) #decode json from serial
		for button, key in zip(button_label, keys) : #iteration checking if the keys are pressed
			if data.get(button) and data.get(button) == "Hit" and not is_pressed[key] :
				keyboard.press(key) #hold the key until release
				is_pressed[key] = True #making sure keys wont pressed multiple time instead of holding it
			if data.get(button) and data.get(button) == "Off" and is_pressed[key] :
				keyboard.release(key) #release key when serial send 'Off' and is_pressed is true
				is_pressed[key] = False
	except KeyboardInterrupt:
		print('Exiting program..')
		exit()
	except Exception as err:
		print(err)
		pass