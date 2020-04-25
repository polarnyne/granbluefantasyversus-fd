'''Granblue Fantasy Versus: Frame Data'''

all_characters = [
    'Ferry',
    'Lancelot',
    'Metera',
    'Zeta',
    'Beelzebub',
    'Djeeta',
    'Gran',
    'Percival',
    'Ladiva',
    'Vaseraga',
    'Narmaya',
    'Zooey',
    'Katalina',
    'Charlotta',
    'Lowain',
    'Soriz',
    'Belial',]

class Character(object):
    '''This is the main class for all the characters'''

    def __init__(self, name):
        self.name = name
        self.movelist = {}

    ''' Using this function, you can insert the frame data manually'''
    def add_framedata(self, move, damage, guard, startup, active, recovery, on_block, on_hit):
        self.move = move
        self.damage = damage
        self.guard = guard
        self.startup = startup
        self.active = active
        self.recovery = recovery
        self.on_block = on_block
        self.on_hit = on_hit
        self.movelist[move] = {
            'damage': damage, 
            'guard': guard, 
            'startup': startup, 
            'active': active, 
            'recovery': recovery, 
            'on block': on_block, 
            'on hit': on_hit
            }

zeta = Character('Zeta')



# gran_movelist = {
#     'cl_L': {'damage': '400', 'guard': 'mid', 'startup': 5, 'active': 3, 'recovery': 5, 'on block': 3, 'on hit': 7}
# }