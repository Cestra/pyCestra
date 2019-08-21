import logging
from time import gmtime, strftime

class bcolors:
    red= '\033[31m'
    green= '\033[32m'
    orange= '\033[33m'
    cend = '\033[0m'

class log:
    
    def __init__(self, messageIn):
        self.message = messageIn
        logging.basicConfig(format="%(levelname)s %(message)s",filename="master.log",level=logging.DEBUG)

    def debug(self):
        
        print(bcolors.green + strftime("DEBUG (%H:%M:%S)") + self.message + bcolors.cend)
        logging.debug(strftime("(%H:%M:%S)") + " " + self.message)

    def info(self):

        print(bcolors.orange + strftime("INFO (%H:%M:%S)"), self.message + bcolors.cend)
        logging.info(strftime("(%H:%M:%S)") + " " + self.message)
    
    def warning(self):

        print(bcolors.red + strftime("WARNING (%H:%M:%S)"), self.message + bcolors.cend)
        logging.warning(strftime("(%H:%M:%S)") + " " + self.message)

'''
print("test")
log("debug test").debug()
log("info test").info()
log("warning test").warning()
print("test")
'''
