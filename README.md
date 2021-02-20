# CSE-476-Mobile-Communication-Networks

Includes Socket Programming Assignments using Phyton.  

## Lab1 - Web Server

Developed a simple Web server in Python that is capable of processing only one request. 
If a browser requests a file that is not present in server, server returns a “404 Not Found” error message.

## Lab2 - UDP Pinger

Written a client ping program in Python. 
Client sends a simple ping message to a server, receives a corresponding pong message back from the server, 
and determines the delay between when the client sent the ping message and received the pong message.
This delay is called the Round Trip Time (RTT). Client waits up to one second for a reply from the server; 
if no reply is received, the client assumes that the packet was lost and prints a message accordingly.

## Lab3 - Mail Client

Created a simple mail client that sends email to any recipient. 
The client needs to establish a TCP connection with a mail server (e.g., a Google mail server), 
dialogue with the mail server using the SMTP protocol, send an email message to a recipient (e.g., your friend) 
via the mail server, and finally close the TCP connection with the mail server.

You can check report for more details and sample input/output.
