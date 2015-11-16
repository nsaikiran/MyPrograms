#! /usr/bin/env python
import socket,sys,os,platform,user
Logo="""  
    ______________
 ___ |Saikiran's| ___ 
|___|    _  _  _ |___|
|   ||_|| `|_|| `|   |
				     
"""
def Chatting(Ip,Port):
	Socket=socket.socket()
	Socket.bind((Ip,Port))
	Socket.listen(5)
	while True:
		print "\nWaiting for ur friend to connect ......"
		c,addr=Socket.accept()
		return c,addr

def Start(Ip,Port):
	print "\n\nRunning on ... "+Ip+" with port "+ str(Port)+".....\n\n\nEnter 'Exit' to disconnect and to inform ur friend .\n\tor\n  'e' to exit to disconnect ."
	Channel,Address=Chatting(Ip,Port)
	print "Ip ",Address[0]," wants to chat with you , press 'y' to accept or 'n' to reject ."
	if raw_input("Enter (y or n) ")=="y":
		Channel.send("Alert :: Accepted .")
		while True:
			print "\nReceived message <--: |",Channel.recv(1024)
			Message=raw_input("Enter a message :--> |")
			if Message=="Exit":
				Channel.send("Alert :: Ur channel disconnected !!! .press 'e' to disconnect .")
				break
			elif Message=="e":
				break
			Channel.send(Message)
	else:
		Channel.send("Rejected . Channel disconnected ! . press 'e' to exit .")
	Channel.close()

def End(Ip,Port):
	print "\n\nRunning on ... "+Ip+" with port "+ str(Port)+".....\n\n\nEnter 'Exit' to disconnect and to inform ur friend .\n\tor\n  'e' to disconnect & to exit ." 
	Socket=socket.socket()
	x=raw_input("\n\nEnter ur friend's Ip :: ")
	try:
		Socket.connect((x,Port))
		print "Received message <--: |",Socket.recv(1024)
		Message=raw_input("\nEnter a message :--> |")
		Socket.send(Message)
		while True:
			print "Received message <--: |",Socket.recv(1024)
			Message=raw_input("\nEnter a message :--> |")
			if Message=="Exit":
				Socket.send("Error :: Ur channel disconnected !!! .press 'e' to exit .")
				break
			elif Message=="e":
				break
			Socket.send(Message)
	except:
		print "Error::Ur friend is not ready "
	Socket.close()

#Program starts ...
if platform.system()=="Linux":
	name=sys.argv[0]
	File=user.home+"/aurora.txt"
	os.system("ifconfig > "+File)
	a=open(File,"r")
	Ip=a.read().split()[6][5:]
	a.close()
	os.remove(File)
	try:
		print Logo,'\n'
		try:Port=int(sys.argv[2])
		except:Port=8090
		if sys.argv[1]=="server":
			Start(Ip,Port)
		elif sys.argv[1]=="client":
			End(Ip,Port)
	except:
		print "ERROR :::\nRun as \n %s server \n or \n %s client .\n\n  U can change port ::\n %s server (or) client port "%(name,name,name)
