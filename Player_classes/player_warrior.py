class Warrior:
    def __init__(self, name, lvl, hp, atk, df):
        self.__name = name
        self.__level = lvl
        self.__health = hp
        self.__atk = atk
        self.__defence = df

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__health

    def get_atk(self):
        return self.__atk

    def get_def(self):
        return self.__defence

    def set_name(self, name):
        self.__name = name

    def set_hp(self, hp):
        self.__health = hp

    def set_atk(self, atk):
        self.__atk = atk

    def set_def(self, df):
        self.__defence = df
