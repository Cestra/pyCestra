import logging
from time import strftime

class bcolors:
    red= '\033[31m'
    green= '\033[32m'
    orange= '\033[33m'
    cend = '\033[0m'

class Log():

    def __init__(self):
        logging.basicConfig(format="[%(levelname)s][%(name)s]%(message)s",filename="master.log",level=logging.DEBUG)

    def debug(self, message):
        print(strftime("[%H:%M:%S]")+bcolors.green+'[DEBUG]'+bcolors.cend,message)
        logging.debug(strftime("[%d.%m][%H:%M:%S]")+message)

    def info(self, message):
        print(strftime("[%H:%M:%S]")+bcolors.orange+'[INFO]'+bcolors.cend,message)
        logging.info(strftime("[%d.%m][%H:%M:%S]")+message)

    def warning(self, message):
        print(strftime("[%H:%M:%S]")+bcolors.red+'[WARNING]'+bcolors.cend,message)
        logging.warning(strftime("[%d.%m][%H:%M:%S]")+message)
'''
log = log()
print("test")
log.debug('kjshfkjwehjkewhwejkfhwekjh')
log.info('sdlkjdklfjdslkfjdslkfjdsklfjsd')
log.warning('ödkfjsdklfjdslkfjsdlkfjsdfljl')
print("test")
'''