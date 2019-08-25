import re

class ChooseNickName:
    '''
    https://www.dofus.com/en/mmorpg/community/nicknames#\n
    https://www.python-kurs.eu/re.php
    '''

    def verify(self, client, nickname):
        #                  Admin                    Modo                 GM           Game Master
        forbidden_words = [r'[Aa][Dd][Mm][Ii][Nn]', r'[Mm][Oo][Dd][Oo]', r'[Gg][Mm]', r'[Gg][Aa][Mm][Ee]-?[Mm][Aa][Ss][Tt][Ee][Rr]',]

        def forbidden_check(val):
            for x in forbidden_words:
                if re.search(x, nickname):
                    return False
            return True

        def forbidden_symbol(val):
            for i in nickname:
                nick = re.match(r'[a-z]?[A-Z]?[0-9]?\x2D?', i)
                if nick.group(0) == '':
                    return False
            return True

        flag = 0
        while True:
            # the nickname must be at least 3 symbol long
            if (len(nickname) < 3):
                flag = -1
                break
            # the nickname may only consist of a-z, A-Z, 0-1 and -
            elif not forbidden_symbol(nickname):
                flag = -1
                break
            # the nickname can not contain more than 4 "-"
            elif len(re.findall(r'\x2D', nickname)) >= 5:
                flag = -1
                break
            # the nickname can not contain more than 2 numbers
            elif len(re.findall(r'[0-9]', nickname)) >= 3:
                flag = -1
                break
            # The nickname can not be a forbidden word
            elif not forbidden_check(nickname):
                flag = -1
                break
            else: 
                flag = 0
                return True
        if flag ==-1: 
            return False

print(ChooseNickName().verify(0, '--8XxNicknamexX8--'))
