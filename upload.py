#!/usr/bin/env python3

import serial
import subprocess
import threading
import time

serial_con = serial.Serial('/dev/ttyS0', 9600, timeout=1)

running = True

def reset_arduino():
    while running:
        # send the reset command to the arduino, so it resets
        serial_con.write('R 10\n'.encode('utf-8'))
        time.sleep(0.5)


reset_thread = threading.Thread(target=reset_arduino)
reset_thread.start()
# first compile the arduino sketch, so that upload has a more predictable
# runtime
subprocess.run(['arduino-cli', 'compile', 'nim-psu.ino', '-b', 'arduino:avr:nano', '-u', '-p', '/dev/ttyS0'])

running = False