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

    def __init__(self, id, name, account, groupe, sexe, pClass, color1,
                color2, color3, kamas, spellboost, capital, energy, level,
                xp, size, gfx, alignement, honor, deshonor, alvl, stats,
                seeFriend, seeAlign, seeSeller, channel, map, cell, pdvper,
                spells, objets, storeObjets, savepos, zaaps, jobs, mountxpgive,
                title, wife, morphMode, emotes, prison, server, logged,
                allTitle, parcho, timeDeblo, noall):
        self.id = id
        self.name = name
        self.account = account
        self.groupe = groupe
        self.sexe = sexe
        self.pclass = pClass
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

# ----------------------------------------

    def get_id(self):
        return self.id

# ----------------------------------------
    
    def get_name(self):
        return self.name

# ----------------------------------------

    def get_account_id(self):
        return self.account

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

