import random
import string

class LoginHandler:

    def exception_caught(self):
        pass

    def message_received(self):
        pass

    def message_sent(self):
        pass

    def session_closed(self):
        pass

    def session_created(self):
        pass

    def session_idle(self):
        pass

    def session_opened(self):
        pass

    def send_to_all(self):
        pass

    def generate_key(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))

    def input_closed(self):
        pass
