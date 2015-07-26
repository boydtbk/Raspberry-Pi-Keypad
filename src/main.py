import threading
import time
from lib_keypad import *

#
# Scan keyboard at a time interval.
# Must run this task in another thread.
#
def keyboard_scan():
	global keyboard
	
	while True:	
		# Read keyboard status
		key = keyboard.getKey()

		# Raise keyboard events
		if key[0] is True:
			keyboard_event(key[1], KEYPAD_TYPE_PRESSED)
		else:
			if key[1] is not None:
				keyboard_event(key[1], KEYPAD_TYPE_HOLDOWN)

		# Delay 50ms between each scan..
		time.sleep(0.05)

		# Quit keyboard
		if keyboard.valid is False:
			keyboard.quit()
			break

#
# Process keyboard events.
#
def keyboard_event(keycode, type):

	if type == KEYPAD_TYPE_PRESSED:
		#
		# Add your code here...
		#
		print 'Key pressed: ' + str(keycode)
		pass

	elif type == KEYPAD_TYPE_HOLDOWN:
		#
		# Becareful to print this event. 
		# This event happened about every 50ms.
		#
		# print 'Key hold-down: ' + str(keycode)
		pass


# --------------------------------------------------------------------------
# ---------------------- Init application ----------------------------------
# --------------------------------------------------------------------------

#
# Init a keypad 4x4
# A default return table is already implemented in library.
#
keyboard =  keypad(rowPins = [1, 2, 3, 4],			# BCM numbering
				   colPins = [5, 6, 7, 8])

#
# Or by this way to re-define return table.
#
# keyboard =  keypad(rowPins = [1, 2, 3, 4],		# BCM numbering
# 				   colPins = [5, 6, 7, 8],
# 				   table   =[[ 7  , 8 ,  9 , '/'],	# Table for calculator keypad
# 					 		 [ 4  , 5 ,  6 , 'x'],
# 					 		 [ 1  , 2 ,  3 , '-'],
# 					 		 ['ON', 0 , '=', '+']])

# Create new thread
keyThread = threading.Thread(target= keyboard_scan)
keyThread.start()


# --------------------------------------------------------------------------
# ---------------------- Main loop -----------------------------------------
# --------------------------------------------------------------------------
while(True):
	#
	# Keyboard processing
	#
	# Add your code here...
	pass


# --------------------------------------------------------------------------
# ---------------------- End Main loop -------------------------------------
# --------------------------------------------------------------------------