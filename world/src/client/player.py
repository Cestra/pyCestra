'''
pyCestra - Open Source MMO Framework
Copyright (C) 2020 pyCestra Team

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
        self.channel = channel
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
        self.socketManager.GAME_SEND_ASK(self.id,
                                        self.name,
                                        self.level,
                                        self.pClass,
                                        self.sex,
                                        self.gfx,
                                        self.color1,
                                        self.color2,
                                        self.color3,
                                        __ItemToASK)

        self.socketManager.send("ILS2000", "ILS2000 (DEMO)") # has something to do with the life points (regeneration time)
        self.socketManager.send("ZS0", "GAME_SEND_ALIGNEMENT (DEMO)")
        self.socketManager.send("cC+i", "GAME_SEND_ADD_CANAL (DEMO)")
        self.socketManager.send("eL", "GAME_SEND_EMOTE_LIST (DEMO)")
        self.socketManager.send("AR6bk", "GAME_SEND_RESTRICTIONS (DEMO)")
        self.socketManager.send("Ow0|1000", "GAME_SEND_Ow_PACKET (DEMO)")

        text1 = 'cs<font color=\'#B9121B\'>'
        test2 = '</font>'
        mess = 'Powered by <b>Cestra</b>'
        text1 += mess + test2
        self.socketManager.send(text1, 'GAME_SEND_MESSAGE (DEMO)')
