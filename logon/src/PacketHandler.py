import socket 
from _thread import start_new_thread
import threading 

print_lock = threading.Lock() 

class PacketHandler:

    def __init__(self):
    
        print("START TestServer!")
        #PacketHandler().TestSocket()

    def threaded(self, c): 
        while True: 
    
            # data received from client 
            data = c.recv(1024) 
            if not data: 
                print('Bye') 
                
                # lock released on exit 
                print_lock.release() 
                break
    
            # reverse the given string from client 
            data = data[::-1] 
    
            # send back reversed string to client 
            c.send(data) 
    
        # connection closed 
        c.close() 
    
    
    def TestSocket(self): 
        host = "127.0.0.1" 
    
        # reverse a port on your computer 
        # in our case it is 12345 but it 
        # can be anything 
        port = 12345
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.bind((host, port)) 
        print("socket binded to post", port) 
    
        # put the socket into listening mode 
        s.listen(5) 
        print("socket is listening") 
    
        # a forever loop until client wants to exit 
        while True: 
    
            # establish connection with client 
            self.c, addr = s.accept() 
    
            # lock acquired by client 
            print_lock.acquire() 
            print('Connected to :', addr[0], ':', addr[1]) 
    
            # Start a new thread and return its identifier 
            start_new_thread(self.threaded, (self.c,)) 
        s.close()

PacketHandler().TestSocket()