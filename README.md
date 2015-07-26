# Raspberry Pi Keypad (M x N)
A simple and useful keypad (M x N) library for Raspberry Pi using python language.

## Usage

*Note: Pin definition in library is in BCM numbering.*

**Initialize a default keypad 4x4 is very simple.**

```
keyboard =  keypad(rowPins = [1, 2, 3, 4],			# BCM numbering
				   colPins = [5, 6, 7, 8])

```

**Or by this way to re-define return table.**

```
keyboard =  keypad(rowPins = [1, 2, 3, 4],		# BCM numbering
				   colPins = [5, 6, 7, 8],
				   table   =[[ 7  , 8 ,  9 , '/'],	# Table for calculator keypad
					 		 [ 4  , 5 ,  6 , 'x'],
					 		 [ 1  , 2 ,  3 , '-'],
					 		 ['ON', 0 , '=', '+']])
```

**Scan keyboard in a new thread**

```
# Create new thread
keyThread = threading.Thread(target= keyboard_scan)
keyThread.start()
```

**Put your code to process keyboard event here...**

```
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
```