BOARD = arduino:avr:nano
CPPFLAGS = 

all:
	arduino-cli compile -b $(BOARD) nim-psu.ino --build-property '$(CPPFLAGS)'


# this upload command is designed to work from the raspi
# after invoking the command, a manual press of the reset button
# on the arduino is needed.
upload: 
	arduino-cli compile nim-psu.ino -b arduino:avr:nano -u -p /dev/ttyS0