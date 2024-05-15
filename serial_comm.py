#!/usr/bin/env python3

import serial
import threading
import time


channel_count = 16
enable_char = "e"
disble_char = "d"
hold_char = "h"
request_char = "q"
timeout_delay = 1.0


class thread_safe_serial:
    def __init__(self, device: str, baudrate: int, timeout: int = 0):
        self.lock = threading.Lock()
        self.serial_port = serial.Serial(device, baudrate, timeout=timeout)


    def readline(self):
        with self.lock:
            return self.serial_port.readline().decode('utf-8')


    def write(self, bytes: bytes):
        with self.lock:
            self.serial_port.write(bytes)


serial_con = thread_safe_serial('/dev/ttyS0', 9600, timeout=1)

def state_to_char(state: bool) -> str:
    if state:
        return enable_char
    return disble_char


def ping():
    while True:
        serial_con.write((hold_char + "\n").encode('utf-8'))
        time.sleep(0.75 * timeout_delay)


def send_deltas(changes: [(int, bool)]):
    # kick out changes relating to channels that don't exist
    changes = list(filter(lambda x: x[0] < channel_count, changes))

    command = ""

    for pin, state in changes:
        cmd_char = enable_char if state else disble_char
        command += cmd_char + " " + str(pin) + "\n"

    serial_con.write(command.encode('utf-8'))


def safe_int(s: str, default: int) -> int:
    try:
        return int(s)
    except ValueError:
        return default


def parse_input(line: str) -> [(int, bool)]:
    chunks = line.split()
    res = []
    if chunks[0] == "read":
        serial_con.write("q\n".encode('utf-8'))
        print(serial_con.readline())

    if chunks[0] == "enable" or chunks[0] == "e":
        return [(safe_int(pin, channel_count + 1), True) for pin in chunks[1:]]

    elif chunks[0] == "disable" or chunks[0] == "d":
        return [(safe_int(pin, channel_count + 1), False) for pin in chunks[1:]]

    return []
    # legacy input form:



def main():
    ping_thread = threading.Thread(target=ping)

    ping_thread.start()
    while True:
        command = input("<NIM-PSU> ")
        state_changes = parse_input(command)
        send_deltas(state_changes)


if __name__ == '__main__':
    main()