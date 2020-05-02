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
            moves[row['Version']] = [               
            f"Damage: {row['Damage']}",            
            f"Guard: {row['Guard']}",               
            f"Startup: {row['Startup']}",           
            f"Active: {row['Active']}",             
            f"Recovery: {row['Recovery']}",         
            f"On Block: {row['On Block']}",         
            f"On Hit: {row['On Hit']}",             
            f"Attribute: {row['Attribute']}",       
            f"Level: {row['Level']}",               
            f"Blockstun: {row['Blockstun']}",        
            f"Hitstun: {row['Hitstun']}",           
            f"Untech: {row['Untech']}",             
            f"Hitstop: {row['Hitstop']}",           
            f"Invul: {row['Invul']}"]               
        self.movelist = moves

    # Prints only information regarding to frame data.
    def get_framedata(self):
        filename = str(self.name) + '_movelist.csv'
        df = pd.read_csv(filename)
        df_animation = df[['Version','Startup','On Block','On Hit']]
        print(df_animation.to_string(index=False))

    # Use this to print the entire movelist. 
    def get_fulltable(self):
        filename = str(self.name) + '_movelist.csv'
        df = pd.read_csv(filename)
        print(df.iloc[0:])

    # We can obtain specific information for a certain movement. 
    def get_moveinfo(self):
        filename = str(self.name) + '_movelist.csv'
        df = pd.read_csv(filename)
        print('Which move do you need?')
        for index, row in df.iterrows():
            print(index, row['Version'])
        attack = int(input(''))
        print(df.iloc[attack])

names = {'Ferry', 'Lancelot', 'Metera', 'Zeta', 'Beelzebub', 'Djeeta', 'Gran', 'Percival', 'Ladiva', 'Vaseraga', 'Narmaya', 'Zooey', 'Katalina', 'Charlotta', 'Lowain', 'Soriz'}
fighters = { n.lower(): Character(n) for n in names }

#   Data stored!
for warrior in fighters:
    fighters[warrior].add_sheet()

#   Frame data calculator
def frame_advantage():
    fighter_1 = input('Enter the character that you want to punish: ').lower()     ### 
    filename = str(fighter_1) + '_movelist.csv'                                      #   Read fighter_1 character's .csv   
    df = pd.read_csv(filename)                                                     ###

    print('Which move do you need?')

    for index, row in df.iterrows():
        print(index, row['Version'])

    attack_1 = int(input(''))
    atk_1 = df.iloc[attack_1][0]
    attack_1 = df.iloc[attack_1][6]
    attack_1 = int(attack_1)

    #   
    if attack_1 >= 1:
        print(f'This move is {attack_1} on block, therefore you will not be able to punish {fighter_1}')
    elif attack_1 == 0:
        print(f'This move is 0 on block, therefore it will not give any advantage neither to you nor your opponent')
    else:

        fighter_2 = input('Enter the character that will punish: ').lower()     ###
        filename = str(fighter_2) + '_movelist.csv'                               # Read fighter_2 character's .csv
        df = pd.read_csv(filename)                                              ###

        punish_dictionary = {}
        
        for index, row in df.iterrows():
            attack_move = row['Version']
            attack_startup = row['Startup']
            
            # Searching for possible moves that can punish fighter_1's move
            if attack_startup == '-' or attack_startup == 'HKD':                
                pass
            elif len(attack_startup) >= 3:
                pass
            else:
                if attack_1 < 0:
                    attack_1 = attack_1 * -1
                
                attack_startup = int(attack_startup)

                if attack_startup < attack_1:           # If there are moves that can punish, they will be stored in this dictionary
                    punish_dictionary.update({attack_move: attack_startup})
        
        if len(punish_dictionary) >= 1:                 # If this dictionary is empty, it means fighter_2 does not have move that can punish fighter_1
            print(f'This move is -{attack_1} on block, therefore {fighter_2.capitalize()} can use the following moves to punish {fighter_1.capitalize()}\'s {atk_1}: \n')
            for key in sorted(punish_dictionary.keys()):
                print(f'{key}: {punish_dictionary[key]}')
            
        else:
            print(f'{fighter_2.capitalize()} do not have a movement that can punish {fighter_1.capitalize()}\'s [{atk_1}].')