# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sipfullproxy
import socketserver
import re
import string
import socket
# import threading
import sys
import logging
import time

# Press the green button in the gutter to run the script.
# Zdroj použitých funkcií https://github.com/tirfil/PySipFullProxy/blob/master/sipfullproxy.py
if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s:%(message)s', filename='dennik.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    hostname = socket.gethostname()


    sipfullproxy.ipaddress = "147.175.186.16"
    #sipfullproxy.ipaddress = "147.175.161.112"
    #sipfullproxy.ipaddress = "192.168.176.47"
    print(sipfullproxy.ipaddress)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (sipfullproxy.ipaddress, sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (sipfullproxy.ipaddress, sipfullproxy.PORT)
    server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
