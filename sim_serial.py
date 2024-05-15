# a placeholder serial module for developing on
# systems that don't support serial communication


class Serial:
    def __init__(self, dev, baud, timeout=0):
        self.dev = dev
        self.baud = baud
        self.timeout = 1

    def write(self, message):
        print("serial writing: ")
        print(message.decode('utf-8'))