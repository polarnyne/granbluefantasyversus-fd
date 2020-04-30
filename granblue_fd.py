'''Granblue Fantasy Versus: Frame Data'''
import pandas as pd
import re

class Character(object):
    # This is the main class for all the characters

    def __init__(self, name):
        self.name = name
        self.movelist = {}

    # Using this function, you can insert the frame data manually
    def add_framedata(self, move, damage, guard, startup, active, recovery, on_block, on_hit, attribute, level, blockstun, hitstun, untech, hitstop, invul):
        self.move = move
        self.damage = damage
        self.guard = guard
        self.startup = startup
        self.active = active
        self.recovery = recovery
        self.on_block = on_block
        self.on_hit = on_hit
        self.attribute = attribute
        self.level = level
        self.blockstun = blockstun
        self.hitstun = hitstun
        self.untech = untech
        self.hitstop = hitstop
        self.invul = invul
        self.movelist[move] = {
            'damage': damage, 
            'guard': guard, 
            'startup': startup, 
            'active': active, 
            'recovery': recovery, 
            'on block': on_block, 
            'on hit': on_hit,
            'attribute': attribute,
            'level': level,
            'blockstun': blockstun,
            'hitstun': hitstun,
            'untech': untech,
            'hitstop': hitstop,
            'invul': invul
            }

    # using this function, you can insert the frame data automatically
    def add_sheet(self):
        moves = {}
        filename = str(self.name) + '_movelist.csv'
        df = pd.read_csv(filename)
        for index, row in df.iterrows():
            moves[row['Version']] = [               ##########################################################
            f"Damage: {row['Damage']}",             ##########################################################
            f"Guard: {row['Guard']}",               ##                                                      ##
            f"Startup: {row['Startup']}",           ##                                                      ##
            f"Active: {row['Active']}",             ##                                                      ##
            f"Recovery: {row['Recovery']}",         ##                                                      ##
            f"On Block: {row['On Block']}",         ##                                                      ##
            f"On Hit: {row['On Hit']}",             ##  This block can be merged in just one long command   ##
            f"Attribute: {row['Attribute']}",       ##  line, but I find this way to be easier to read      ##
            f"Level: {row['Level']}",               ##  and modify.                                         ##
            f"Blockstun: {row['Blockstun']}",       ##                                                      ## 
            f"Hitstun: {row['Hitstun']}",           ##                                                      ##
            f"Untech: {row['Untech']}",             ##                                                      ##
            f"Hitstop: {row['Hitstop']}",           ##########################################################
            f"Invul: {row['Invul']}"]               ##########################################################
        self.movelist = moves

    # Use this to print the entire movelist.
    def get_movelist(self):
        for key in self.movelist.keys():
            print(key, self.movelist[key])

    def get_table(self):
        filename = str(self.name) + '_movelist.csv'
        df = pd.read_csv(filename)
        print(df.iloc[0:])

names = {'Ferry', 'Lancelot', 'Metera', 'Zeta', 'Beelzebub', 'Djeeta', 'Gran', 'Percival', 'Ladiva', 'Vaseraga', 'Narmaya', 'Zooey', 'Katalina', 'Charlotta', 'Lowain', 'Soriz'}
fighters = { n.lower(): Character(n) for n in names }

#   Data stored!
for i in fighters:
    fighters[i].add_sheet()