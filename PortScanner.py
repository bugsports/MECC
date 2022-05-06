# Port Scanner
import socket
import sys
from datetime import datetime

ipv4 = input("Enter an IP address to scan: ")
print("Scanning ports on: " + str(ipv4))
print("-"*50)

try:
    for port in range(1,65535): #max port number
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        result = sock.connect_ex((ipv4,port))
        if result == 0:
            print("Port {}:  Open".format(port))
        sock.close()
except KeyboardInterrupt:
    print("\n Exiting scanner...")
    sys.exit()
except socket.gaierror:
    print("\n Hostname couldn't be resolved.")
    sys.exit()
except socket.error:
    print("\n Server not responding.")
    sys.exit()
