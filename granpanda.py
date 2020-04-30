class Character(object):
    # This is the main class for all characters

    def __init__(self, name):
        self.name = name
        self.movelist = {}

names = {'Ferry', 'Lancelot', 'Metera', 'Zeta', 'Beelzebub', 'Djeeta', 'Gran', 'Percival', 'Ladiva', 'Vaseraga', 'Narmaya', 'Zooey', 'Katalina', 'Charlotta', 'Lowain', 'Soriz'}
characters = { n.lower(): Character(n) for n in names }

