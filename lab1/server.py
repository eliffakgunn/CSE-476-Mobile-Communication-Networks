# Import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM) #TCP server socket

# Prepare a server socket
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1) #listen 1 connction

while True:
	#Establish the connection
	print ("Ready to serve...")

	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()

	try:
		# Receives the request message from the client
		message =  connectionSocket.recv(1500)
		filename = message.split()[1] #path of request
		f = open(filename[1:], 'rb')
		outputdata = f.read()
		#print(outputdata)

		#Send one HTTP header line into socket
		connectionSocket.send(str("HTTP/1.1 200 OK\r\n\r\n").encode())

		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
		    connectionSocket.send(chr(outputdata[i]).encode())

		connectionSocket.close()

	except IOError:
		#Send response message for file not found
		connectionSocket.send(str("HTTP/1.1 404 Not Found\r\n\r\n").encode())
		connectionSocket.send(str("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n").encode())

		#Close client socket
		connectionSocket.close()

serverSocket.close()