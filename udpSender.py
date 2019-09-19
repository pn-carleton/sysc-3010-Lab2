# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
numMessage = sys.argv[3]

if numMessage < 0:
    print("num of messages to be sent must be positive")
    sys.exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
my_address = (host, 1001)
s.bind(my_address)

while 1:
    print ("Enter data to transmit: ENTER to quit")
    data = sys.stdin.readline().strip()
    if not len(data):
        break
#    s.sendall(data.encode('utf-8'))
    for i in range(0, int(numMessage)):
        sendData = data + str(i)
        print("Sending data: " + sendData)
        s.sendto(sendData.encode('utf-8'), server_address)
        
        buf, address = s.recvfrom(port)
        print ("Received %s bytes from %s %s: " % (len(buf), address, buf ))

s.shutdown(1)

