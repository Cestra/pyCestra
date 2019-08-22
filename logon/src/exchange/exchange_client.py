class ExchangeClient:

    def __init__(self):
        pass
    
    def parse(self):
        try:
            def switch(self,i):
                method_name='number_'+str(i)
                method=getattr(self,method_name,lambda :'Invalid')
                return method()

            def number_0(self):
                return 'zero'

            def number_1(self):
                return 'one'

            def number_2(self):
                return 'two'
        except:
            # print("Packet undefined\"" + packet + "\"")
            # TODO Kick Player
            pass

'''
# TODO It would have to go but I do not get the switch running
 
s = ExchangeClient()
s.parse().switch(1)
print(s)
'''

'''
F           free Places ?
S
    SH      set Ip, set Port, set State ?   (send("SHK"))
    SK                                      (send("SKR")) and kick
    SS      get Server, set State ?
M
    MP      Map Magic
    MT                                      (server.send("MF" + account + "|" + getServer.getId + "|" + players))
    MD                                      (server.send("MD" + split))
    MO                                      (server.send("MO" + split + "|" + getServer().getId()))
'''
