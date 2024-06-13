class Archer:
    def __init__(self, name, lvl, hp, atk, df):
        self.name = name
        self.level = lvl
        self.health = hp
        self.attack = atk
        self.defence = df

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.health

    def get_atk(self):
        return self.attack

    def get_def(self):
        return self.defence

    def set_name(self, name):
        self.name = name

    def set_hp(self, hp):
        self.health = hp

    def set_atk(self, atk):
        self.attack = atk

    def set_def(self, df):
        self.defence = df