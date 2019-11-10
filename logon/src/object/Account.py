class Account():

    def __init__(self):
        pass

# ----------------------------------------

    def get_id(self):
        return self.UUid
    
    def set_id(self, i):
        self.UUid = i

# ----------------------------------------
    
    def get_name(self):
        return self.name
    
    def set_name(self, n):
        self.name = n
# ----------------------------------------

    def get_pass(self):
        return self.passs

    def set_pass(self, p):
        self.passs = p

# ----------------------------------------

    def get_nickname(self):
        return self.nickname

    def set_nickname(self, ni):
        self.nickname = ni

# ----------------------------------------

    def get_question(self):
        return self.question
    
    def set_question(self, q):
        self.question = q

# ----------------------------------------

    def get_state(self):
        return self.state

    def set_state(self, s): # "logged" byte
        self.state = s

# ----------------------------------------
 
    def is_staff(self):
        pass

# ----------------------------------------

    def get_client(self):
        pass

# ----------------------------------------

    def get_server(self):
        pass

    def set_server(self):
        pass

# ----------------------------------------

    def get_subscribe_remaining(self):
        pass

# ----------------------------------------

    def get_subscribe(self):
        return self.subscribe

    def set_subscribe(self, sup):
        self.subscribe = sup

    def is_subscribes(self):
        pass

# ----------------------------------------

    def set_banned(self, b):
        self.banned = b

    def is_banned(self):
        return self.banned

# ----------------------------------------

    def add_player(self):
        pass

    def del_player(self):
        pass

    def get_players(self):
        pass
