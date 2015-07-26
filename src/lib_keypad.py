import RPi.GPIO as GPIO
import time

# Constant definition

KEYPAD_TYPE_PRESSED 	 = 11
KEYPAD_TYPE_HOLDOWN 	 = 12


class keypad:

	"""keypad (M x N) library for python"""

	def __init__(self, **kwargs):
		self.valid 	 = False 				# Default: keypad is not valid to run
		self.prekey	 = None 				# Previous pressed keycode
		self.row 	 = 4
		self.col 	 = 4
		self.rowPins = [] 					# [1, 2, 3, 4] (BCM numbering)
		self.colPins = [] 					# [5, 6, 7, 8] (BCM numbering)

		self.table 	 =[[ 1 , 2 ,  3 , 'A'],	# Default table for keypad 4x4
					   [ 4 , 5 ,  6 , 'B'],
					   [ 7 , 8 ,  9 , 'C'],
					   ['*', 0 , '#', 'D']]

		for k, value in kwargs.iteritems():
			if   k == 'table'	: self.table 	= value
			elif k == 'rowPins' : self.rowPins  = value
			elif k == 'colPins' : self.colPins  = value

		# Check empty column/row pins
		if not self.rowPins or not self.colPins:
			print 'Error: Row/Col pins are NOT defined yet!'
			return 1
		
		# Check row/col size
		if len(self.rowPins) != len(self.table):
			print 'Error: Row size not match!'
			return 1

		# Check row/col size
		if len(self.colPins) != len(self.table[0]):
			print 'Error: Column size not match!'
			return 1

		self.valid = True
		self.row   = len(self.rowPins)
		self.col   = len(self.colPins)

		# Set up GPIO using BCM numbering
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

		# Rows input
		# Enable pull-up resitors
		for pin in self.rowPins:	
			GPIO.setup(pin, GPIO.IN, pull_up_down= GPIO.PUD_UP)

		# Columns output: HIGH
		for pin in self.colPins:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin, GPIO.HIGH)

	#
	# Read keypad status.
	#
	# Return:
	# 	(True , keycode)	: Valid key with code
	#	(False, keycode)	: Key is pressed but still hold-down
	#	(False, None)		: No key is pressed
	#
	def getKey(self):
		
		# Check if keypad is valid
		if self.valid is False:
			return 1

		colIndex = 0
		rowIndex = 0

		for colIndex in range(0, self.col):

			# All columns: HIGH
			for pin in self.colPins:
				GPIO.output(pin, GPIO.HIGH)

			# Just 1 column: LOW
			GPIO.output(self.colPins[colIndex], GPIO.LOW)

			# Delay 10us
			# time.sleep(0.00001)

			# Read row pins status
			for rowIndex in range(0, self.row):
				if not GPIO.input(self.rowPins[rowIndex]):		# Row is LOW

					# Read key code			
					keycode = self.table[rowIndex][colIndex]					

					if keycode != self.prekey:
						# Pin default: HIGH
						GPIO.output(self.colPins[colIndex], GPIO.HIGH)

						self.prekey = keycode
						return (True, keycode)					# A valid key code
					else:
						return (False, keycode)					# Key is still hold-down

		# All columns: HIGH
		for pin in self.colPins:
			GPIO.output(pin, GPIO.HIGH)

		# No key is pressed
		self.prekey = None
		return (False, None)
	
	#
	# Free pins resource for another application.
	# Return:
	#	0 	: Clean success
	#	1 	: Nothing to do
	#
	def quit(self):
		# Check if keypad is valid
		if self.valid is False:
			return 1

		# Release pins
		for pin in self.rowPins:
			GPIO.cleanup(pin)

		for pin in self.colPins:
			GPIO.cleanup(pin)

		# Success
		return 0
	