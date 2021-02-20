from socket import *
from time import time, ctime
import sys

#there sohuld be 3 command line arguments
if (len(sys.argv) != 3):
    print("Usage: UDPPingClient.py <server_host> <server_portNum>")
    sys.exit()

ip_addr = sys.argv[1] 
portNum = sys.argv[2]

#create client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
#wait one second for reply
clientSocket.settimeout(1)

#send and receive 10 ping messages
for i in range(0, 10):
    t0 = time() #start time
    message = "Ping " + str(i+1) + " " + ctime(t0)[11:19]

    try:
        #sends and receives the message
        clientSocket.sendto(message.encode(),(ip_addr, int(portNum)))
        response, server_addr = clientSocket.recvfrom(1024)

        t1 = time() #end time

        #response message from server
        print("Response: " + response.decode())

        print("Round Trip Time: %.3fs \n" % (t1 - t0))
    except:
        print("Ping " + str(i+1) + " request timed out\n")

clientSocket.close()