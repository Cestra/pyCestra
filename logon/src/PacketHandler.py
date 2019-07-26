import socket
import sys
import threading

from _thread import start_new_thread

class PacketHandler:

    def __init__(self):
    
        print("START PacketHandler")

    def threaded(self, c): 

        while True: 
    
            # data received from client 
            data = c.recv(1024) 
            if not data: 
                print('Bye! We lost :', self.addr[0], ':', self.addr[1])
                break
    
            msg = data
            print(self.addr[1], ': "', msg, '"')
            # reverse the given string from client 
            data = data[::-1]
    
            # send back reversed string to client 
            c.send(data) 
    
        # connection closed 
        c.close() 
    
    def test_socket(self): 

        host = "127.0.0.1"
        port = 478

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            s.bind((host, port))
            print("socket binded to post", port) 
        except socket.error:
            print("Binding faild")
            sys.exit

        s.listen(5) 
        print("socket is listening") 

        while True: 

            self.c, self.addr = s.accept() 

            print('Connected to :', self.addr[0], ':', self.addr[1]) 
    
            # Start a new thread and return its identifier 
            start_new_thread(self.threaded, (self.c,)) 
        s.close()
