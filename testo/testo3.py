import threading, time
 
class MyThread(threading.Thread):
    def run(self):
        while True:
            print('Ich Lebe')
            time.sleep(1)
             
th = MyThread()
print('-----')
th.start()
time.sleep(7)
th.daemon = True
print('-----')