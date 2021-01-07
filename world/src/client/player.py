'''
pyCestra - Open Source MMO Framework
Copyright (C) 2021 pyCestra Team

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from core.logging_handler import Logging

class Player:

    def __init__(self, id, name, account, groupe, sex, pClass, color1,
                color2, color3, kamas, spellboost, capital, energy, level,
                xp, size, gfx, alignement, honor, deshonor, alvl, stats,
                seeFriend, seeAlign, seeSeller, channel, map, cell, pdvper,
                spells, objets, storeObjets, savepos, zaaps, jobs, mountxpgive,
                title, wife, morphMode, emotes, prison, server, logged,
                allTitle, parcho, timeDeblo, noall):
        self.id = id
        self.name = name
        self.accountID = account
        self.account = None # this is where the account object is saved
        self.groupe = groupe
        self.sex = sex
        self.pClass = pClass
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.kamas = kamas
        self.spellboost = spellboost
        self.capital = capital
        self.energy = energy
        self.level = level
        self.xp = xp
        self.size = size
        self.gfx = gfx
        self.alignement = alignement
        self.honor = honor
        self.deshonor = deshonor
        self.alvl = alvl
        self.stats, = stats,
        self.seeFriend = seeFriend
        self.seeAlign = seeAlign
        self.seeSeller = seeSeller
        self.channel = channel # Infor[i] Public[*] priate,group,team[#$p] guild[%] alignment[!] recruitment[?] trading[:] newbies[^] admin[@]???
        self.map = map
        self.cell = cell
        self.pdvper = pdvper
        self.spells = spells
        self.objets = objets
        self.storeObjets = storeObjets
        self.savepos = savepos
        self.zaaps = zaaps
        self.jobs = jobs
        self.mountxpgive = mountxpgive
        self.title = title
        self.wife = wife
        self.morphMode = morphMode
        self.emotes = emotes
        self.prison = prison
        self.server = server
        self.logged = logged
        self.allTitle = allTitle
        self.parcho = parcho
        self.timeDeblo = timeDeblo
        self.noall = noall

        self.socketManager = None # is set at set_account

        self.mount = None
        self.fight = None

# ----------------------------------------

    def get_id(self):
        return self.id

# ----------------------------------------
    
    def get_name(self):
        return self.name

# ----------------------------------------

    def get_account_id(self):
        return self.accountID

# ----------------------------------------

    def get_account(self):
        return self.account
    
    def set_account(self, accobject, socketManager):
        self.account = accobject
        self.socketManager = socketManager

# ----------------------------------------

    def get_groupe(self):
        return self.groupe
    
    def set_groupe(self, g):
        self.groupe = g

# ----------------------------------------

    def get_sex(self):
        return self.sex

# ----------------------------------------

    def get_pClass(self):
        return self.pClass

# ----------------------------------------

    def get_level(self):
        return self.level

# ----------------------------------------

    def get_gfx(self):
        return self.gfx
        
# ----------------------------------------

    def get_color1(self):
        return self.color1

    def get_color2(self):
        return self.color2

    def get_color3(self):
        return self.color3

# ----------------------------------------

    def get_gfx(self):
        return self.gfx

    def set_gfx(self, gfx):
        self.gfx = gfx

# ----------------------------------------

    def get_channel(self):
        return self.channel

    def set_channel(self, cha):
        self.channel = cha

# ----------------------------------------

    def get_mountxpgive(self):
        return self.mountxpgive

# ----------------------------------------

    def get_online(self):
        return self.online

    def set_online(self, boolean):
        self.online = boolean

# ----------------------------------------

    def join_game(self):
        self.set_online(True)
        if self.mount != None:
            # SocketManager.GAME_SEND_Re_PACKET(this, "+", this._mount)
            pass
        self.socketManager.GAME_SEND_Rx_PACKET() # loads correctly
        __ItemToASK = '' # TODO
        self.socketManager.GAME_SEND_ASK(self.get_id(),
                                        self.get_name(),
                                        self.get_level(),
                                        self.get_pClass(),
                                        self.get_sex(),
                                        self.get_gfx(),
                                        self.get_color1(),
                                        self.get_color2(),
                                        self.get_color3(),
                                        __ItemToASK)
                                        
        # TODO GAME_SEND_OS_PACKET - something with World.getItemSetNumber()
        if self.fight is not None:
            self.socketManager.send('ILS0', 'ILS0') # heart display in the middle of the screen
        else:
            self.socketManager.send('ILS2000', 'ILS2000')
        if len(self.jobs) > 0:
            # TODO JOBS here
            pass
        self.socketManager.GAME_SEND_ALIGNEMENT(self.alignement) # TODO i don't think it works
        # the info channel is always activated when entering
        __chn = 'i'
        # it is checked whether the player has the authorization to join the @ channel
        if self.get_groupe() > 0:
            __chn += '@'
        self.socketManager.GAME_SEND_ADD_CANAL(str(self.get_channel()) + __chn)
        del __chn
        # TODO GAME_SEND_ZONE_ALLIGN_STATUT - al| + World.getSousZoneStateString()
        self.socketManager.send("eL1", "GAME_SEND_EMOTE_LIST (DEMO)") # no plan how it works yet (look at Player.java 370-376)
        self.socketManager.GAME_SEND_RESTRICTIONS()

        mess = 'cs<font color=\'#B9121B\'>Powered by <b>Cestra</b></font>'
        self.socketManager.send(mess, 'GAME_SEND_MESSAGE (DEMO)')

    def send_game_create(self):
        self.socketManager.GAME_SEND_GAME_CREATE(str(self.get_name()))

        # GAME_SEND_STATS_PACKET -> GAME_SEND_Ow_PACKET
        self.socketManager.GAME_SEND_STATS_PACKET(self.get_As_packet())

        # As	xp | _kamas | _capital | _spellPts | _align ~ _align , _aLvl , getGrade , _honor , _deshonor , 0 | curPdv , pdvMax | getEnergy , 10000 | getInitiative | 0 | 0,0,0,0,0 | 0,0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0| 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 |
        #packet_As = 'As1,1,1|10000|5|6|0~3,0,0,0,0,0|10,100|10000,10000|100|0|0,0,0,0,0|0,0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|'
        #self.socketManager.send(packet_As, 'GAME_SEND_GAME_CREATE (DEMO)')

        mapID = '10294'
        data = '0802221747'
        key = '6a292e2c446752644236725b68355d733e3a446060303e7d476e7c63354e5e42505052657756526b32585753473b64782f6f2261545d47732a5e63253242772532427e4b636c663a6e33395031705c4461386348652d527f6059365d5154703a4c39416d342962707e653b214c2e7657573c4f5542223f5d285b66423a446c5d723c2f594a6d7820787826505b253242663d463150253235304b4e41312d7f784e7d23712c655a5230335f55382046202869795f6e71415463753c4f3840492c4e'

        packet_GDM = 'GDM|' + mapID + '|'  + data + '|'  + key
        self.socketManager.send(packet_GDM, 'packet_GDM (DEMO)')

        self.socketManager.send('fC0', 'packet_GDM (DEMO)')

    def get_As_packet(self):
        # refreshStats
        # refreshLife
        # As	xp | _kamas | _capital | _spellPts | _align ~ _align , _aLvl , getGrade , _honor , _deshonor , 0 | curPdv , pdvMax | getEnergy , 10000 | getInitiative | 0 | 0,0,0,0,0 | 0,0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0| 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 | 0,0,0,0 |
        packet_As = 'As1,1,1|10000|5|6|0~3,0,0,0,0,0|10,100|10000,10000|100|0|0,0,0,0,0|0,0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|0,0,0,0|'
        packet = 'As' # As
        packet += 'XP' + '|' # xp |
        # kamas |
        # capital |
        # spellPts |
        # align ~ align , aLvl , getGrade , _honor , _deshonor , 0 |
        # curPdv , pdvMax |
        # getEnergy , 10000 |
        # getInitiative |
        # 0 |
        # 0,0,0,0,0 |
        # 0,0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0|
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        # 0,0,0,0 |
        return packet_As