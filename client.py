import socket
def Main():
	host = socket.gethostname()
	port =2506
	buf =1024
	run = ((host,port))

	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect(run)
	
	while True:
		message = raw_input(">>")
		client.send(message)
		answer = client.recv(buf)
		print str(answer)
		if message == "q":
			print "connection closed"
			break
		
	client.close()
if __name__ == '__main__':
	Main()
