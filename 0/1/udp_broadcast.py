ju.ci("import psutil","psutil")

from socket import *
import time
from datetime import datetime

s=socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
def Log(message):
    print("Broadcast: " + message)
    s.sendto(message.encode('utf-8'),('255.255.255.255',12345))
while True:
    msg = gethostname() + \
        ", Datetime " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + \
        ", CPU " + str(psutil.cpu_percent()) + "%" + \
        ", RAM " + str(psutil.virtual_memory().percent) + "%"
    Log(msg)
    time.sleep(5)
