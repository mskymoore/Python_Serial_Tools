
# Title:	binary_blaster.py
# Author:       Sky Moore (mskymoore@gmail.com)
# Summary:      Console script that opens a serial port and writes the characters supplied.
#
# usage: binary_blaster.py [-h] [-b BAUDRATE] [-t TIMEOUT] p c
#
# positional arguments:
#   p                     Serial_Port, ex: /dev/ttyUSB0, COM24, /dev/ttyS0
#   c                     Characters to send, must be hexadecimal digits, 0 -
#                         f/F
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -b BAUDRATE, --baudrate BAUDRATE
#                         baud rate to send bytes at, default = 9600 baud
#   -t TIMEOUT, --timeout TIMEOUT
#                         timeout for sending and recieving bytes, default = 1
#                         second
#
#
#
#
import argparse, sys, serial, time

def Main():

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('p', type=str, help='Serial_Port, ex: /dev/ttyUSB0, COM24, /dev/ttyS0')
    parser.add_argument('c', type=str, help='Characters to send, must be hexadecimal digits, 0 - f/F')
    parser.add_argument('-b', '--baudrate', type=int, help='baud rate to send bytes at, default = 9600 baud')
    parser.add_argument('-t', '--timeout', type=int, help='timeout for sending and recieving bytes, default = 1 second')
    args = parser.parse_args(sys.argv[1:])

    #If -t flag was not sent
    if(args.timeout is None):
        #set default timout
        TimeOut = 1
    else:
        #set timout to -t arg
        TimeOut = args.timeout

    # If -b flag was not sent
    if(args.baudrate is None):
	# set default baudrate
	BaudRt = 9600
    else:
	# set baudrate to -b arg
	BaudRt = args.baudrate

    # If there was a com port sent
    if(args.p is not None):
        # Create and configure serialInterface
        serialInterface = serial.Serial(baudrate=BaudRt,timeout=TimeOut)
        serialInterface.port = args.p
    # Else we must exit
    else:
        print("Must supply a serial port... Exiting.")
        sys.exit(1)
    
    # If there was a string of characters sent
    if(args.c is not None):
        try:
            # Open the serial port
            serialInterface.open()
            time.sleep(3)
        except Exception:
            print("Unable to open serial port " + args.p)
            sys.exit(3)
        # For each character sent in the string of characters
        for c in args.c:
            # Write it to the serial interface
            serialInterface.write(c)
            time.sleep(0.5)
            # Retrieve and display the output
            print(serialInterface.read_all())
        try:
            # Close the serial port
            serialInterface.close()
        except Exception:
            print("Error closing serial port " + args.p)
    # Else no reason to continue
    else:
        print("No characters supplied to write to device... Exiting.")
        sys.exit(2)

if __name__ == '__main__':
    Main()
