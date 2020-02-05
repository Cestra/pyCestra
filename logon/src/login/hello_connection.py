import sys

from core.logging_handler import Logging


class HelloConnection():

    def __init__(self, c):
        self.log = Logging()
        client = c
        # We send the first package (HC + KEY + empty byte)
        client.write('HC'+client.get_key())

        # We are waiting for the client version
        data = client.get_io_session().recv(2048)
        msg = data.decode()
        if not (msg == '1.30.9\n\x00' or msg == '1.29.1\n\x00' or msg == '1.30.0\n\x00'):
            self.log.debug('[' + str(client.get_address()[0]) +
                            ':' + str(client.get_address()[1]) +
                            '][' + str(client.get_status().name) +
                            '] The client has the wrong version - ' +
                            '(' + str(msg.split('\n')[0]) + ')')
            # TODO wrong text window is displayed "Invalid login or password."
            client.write('AlEf')
            sys.exit(0)
        self.log.debug('[' + str(client.get_address()[0]) + ':' +
                        str(client.get_address()[1]) +'][' +
                        str(client.get_status().name) + '] Version accepted ' +
                        '(' + str(msg.split('\n')[0]) + ')')
        return
