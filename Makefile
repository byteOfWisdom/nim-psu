BOARD = arduino:avr:nano
CPPFLAGS = 

all:
	arduino-cli compile -b $(BOARD) NIM-PSU.ino --build-property '$(CPPFLAGS)'