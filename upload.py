#!/usr/bin/env python3

import serial
import subprocess

serial_con = serial.Serial('/dev/ttyS0', 9600, timeout=1)

# first compile the arduino sketch, so that upload has a more predictable
# runtime
subprocess.run(['mkdir', '-p', 'build'])
subprocess.run(['arduino-cli', 'compile', 'nim-psu.ino', '-b', 'arduino:avr:nano', '--output-dir', './build'])

# send the reset command to the arduino, so it resets
# after 500ms,
serial_con.write('R 500\n'.encode('utf-8'))

subprocess.run(['arduino-cli', 'upload', './build/', '-b', 'arduino:avr:nano', '-p', '/dev/ttyS0'])