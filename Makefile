BOARD = arduino:avr:nano
CPPFLAGS = 

all:
	arduino-cli compile -b $(BOARD) nim-psu.ino --build-property '$(CPPFLAGS)'