Howdy there,
	In this project their is a possibility to optimize alot of things,
	I have done it by popular standared like using LCD 4-bit instade of I2C.
	Further more if you install the libraries using pip install, You wouldn't
	even have to look at the codes ;)
	
	Back to the project, you would have to install proteus 8.9 or above.
	The simulation uses:
		An LED that indicates it has started working.
		16×2 LCD Display Module --> Hitachi’s HD44780 LCD Controller.

For Upgrade (1)
	Remove Adafruit_CharLCD.py and its import header in main.py
	And instead Install the following via pip install preferably
		https://pypi.org/project/RPLCD/ --> pip install RPLCD
	You can remove the autoscroll when typing in main.py line 35
