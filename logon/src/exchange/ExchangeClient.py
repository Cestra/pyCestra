class ExchangeClient:

    def __init__(self):
        pass
    
    def parse(self):

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

'''
# TODO Es müsste gehen aber ich bekomme denn switch nicht ausgeführt
 
s = ExchangeClient()
s.parse().switch(1)
print(s)
'''

