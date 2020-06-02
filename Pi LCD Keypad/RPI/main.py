# !/usr/bin/env python3

# IMPORTS
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep
import Adafruit_CharLCD
import Keypad

# INITALIZATIONS
ROWS = 4
COLS = 4
keys =  [   '7','8','9','C',
            '4','5','6','B',
            '1','2','3','A',
            '*','0','#','D'     ]
rowsPins = [6,12,13,16]
colsPins = [19,20,26,4]

def init():
 GPIO.setwarnings(False)    # Ignore warning for now
 GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
 GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)
 GPIO.output(5, GPIO.HIGH) # Turn on
 sleep(1)                  # Sleep for 1 second
 GPIO.output(5, GPIO.LOW)  # Turn off
 

# Main function
def main () :
# Setup
 peripheral_setup() # [For proteus only]
 init()
 lcd = Adafruit_CharLCD()
 lcd.message("  Waiting ...\nPress: ")
 lcd.autoscroll()
 keypad = Keypad(keys, rowsPins, colsPins, ROWS, COLS)
 keypad.setDebounceTime(50)
# Infinite loop
 while 1 :
  peripheral_loop() # [For proteus only]
  key = keypad.getKey()
  if(key != keypad.NULL):
   lcd.message("%c "%(key))
  pass

  
# Command line execution
if __name__ == '__main__' :
   main()
