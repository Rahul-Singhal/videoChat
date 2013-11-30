#Programmer: Rahul Singhal
#Server

from socket import *
serverPort=8003

onlineUsers={}

def serviceUser():
	s = socket(AF_INET, SOCK_DGRAM)
	# myIp = gethostbyname("%s.local" % gethostname())
	# print myIp
	s.bind(("localhost",serverPort))
	while True:
		data, userAddress = s.recvfrom(1024) # buffer size is 1024 bytes                                                                                                      
		print "received message:", data
		clientInfo = data.split(',')
		onlineUsers[clientInfo[0]] = (userAddress[0],clientInfo[2])
		# print onlineUsers
		if(onlineUsers.has_key(clientInfo[1])):
			s.sendto("Connecting you to " + clientInfo[1] + "!!", userAddress)
		else:
			s.sendto(clientInfo[1] + " is not online right now!!", userAddress)



serviceUser()
# s = socket(AF_INET , SOCK_STREAM)
# #automatically choose a free port
# s.bind((serverIp, serverPort))
# s.listen(1)
# conn, addr = s.accept()
# print "connected by..", addr
# while True:
#     data = conn.recv(1024) #recives datae (1024 bytes) using conn and store into data
#     print "Received ", repr(data) # print data; Data is the message the users types
#     reply = raw_input("Reply: ")
#     conn.sendall(reply)

# conn.close()
