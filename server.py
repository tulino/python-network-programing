import socket
def Main ():
        host = socket.gethostname()
        port = 2506
        buf = 1024
        run = ((host,port))
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind(run)
        server.listen(2)

        client,addr = server.accept()
        print "connection..:",addr[0]
        while True:
                data = client.recv(buf)
                if data == "q":
                        break
                elif len(data) == 0:
                        pass
                else:
                        print data
	
		answer = raw_input(">>")
		client.send(answer)
	client.close()
	server.close()
if __name__ == '__main__':
        Main()
