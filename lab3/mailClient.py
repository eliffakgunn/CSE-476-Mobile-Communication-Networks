from socket import *
import ssl
import base64

mailAddress = "mail@gmail.com"
password = "password"
targetMail = "targetmail@mail.com"
subject = "Enter mail's subject"
message = "Enter message"

#set mail server
mailServer = ("smtp.gmail.com", 587)
#create socket for TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailServer)
#get response and print
response = clientSocket.recv(1024).decode()
print("response: ", response)
if(response[:3] != "220"):
    print("220 reply not received from server.")

#send HELO command
command = "HELO Alice\r\n"
clientSocket.send(command.encode())
#get response and print
response1 = clientSocket.recv(1024).decode()
print("response1: ", response1)
if(response1[:3] != "250"):
    print("250 reply not received from server.")

#send STARTTLS command
command = "STARTTLS\r\n"
clientSocket.send(command.encode())
#get response and print
response2 = clientSocket.recv(1024).decode()
print("response2: ", response2)
if(response2[:3] != "220"):
    print("220 reply not received from server.")

#wrap socket for security
tlsSocket = ssl.wrap_socket(clientSocket)

#send AUTH LOGIN command
command = "AUTH LOGIN\r\n"
tlsSocket.send(command.encode())
#get response and print
response3 = tlsSocket.recv(1024).decode()
print("response3: ", response3)
if(response3[:3] != "334"):
    print("334 reply not received from server.")

#send mail address 
tlsSocket.send(base64.b64encode(mailAddress.encode()))
tlsSocket.send(("\r\n").encode())
#get response and print
response4 = tlsSocket.recv(1024).decode()
print("response4: ", response4)
if(response4[:3] != "334"):
    print("334 reply not received from server.")

#send password 
tlsSocket.send(base64.b64encode(password.encode()))
tlsSocket.send(("\r\n").encode())
#get response and print
response5 = tlsSocket.recv(1024).decode()
print("response5: ", response5)
if(response5[:3] != "235"):
    print("235 reply not received from server.")

#send MAIL FROM command
command = "MAIL FROM:<" + mailAddress + ">\r\n"
tlsSocket.send(command.encode())
#get response and print
response6 = tlsSocket.recv(1024).decode()
print("response6: ", response6)
if(response6[:3] != "250"):
    print("250 reply not received from server.")

#send RCPT TO command 
command = "RCPT TO:<" + targetMail + ">\r\n"
tlsSocket.send(command.encode())
#get response and print
response7 = tlsSocket.recv(1024).decode()
print("response7: ", response7)
if(response7[:3] != "250"):
    print("250 reply not received from server.")

#send DATA command
command = "DATA\r\n"
tlsSocket.send(command.encode())
#get response and print
response8 = tlsSocket.recv(1024).decode()
print("response8: ", response8)
if(response8[:3] != "354"):
    print("354 reply not received from server.")

#send subject and message
subject = "Subject: "+ subject + "\r\n\r\n"
message = "\r\n" + message + "\r\n.\r\n"
tlsSocket.send(subject.encode())
tlsSocket.send(message.encode())
#get response and print
response9 = tlsSocket.recv(1024).decode()
print("response9: ", response9)
if(response9[:3] != "250"):
    print("250 reply not received from server.")

#send QUIT command
command = "QUIT\r\n"
tlsSocket.send(command.encode())
#get response and print
response10 = tlsSocket.recv(1024).decode()
print("response10: ", response10)
if(response10[:3] != "221"):
    print("221 reply not received from server.")