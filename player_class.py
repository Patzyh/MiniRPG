import random


class Spieler:
    def __init__(self, name, class_type):
        self.__name = name
        self.__level = 0
        if class_type == "Kämpfer":
            self.__health = 19
            self.__atk = 14
        elif class_type == "Bogenschütze":
            self.__health = 17
            self.__atk = 17
        elif class_type == "Magier":
            self.__health = 15
            self.__atk = 20

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__health

    def get_atk(self):
        return self.__atk

    def get_level(self):
        return self.__level

    def set_name(self, name):
        self.__name = name

    def set_hp(self, hp):
        self.__health = hp

    def set_atk(self, atk):
        self.__atk = atk

    def set_level(self, level):
        self.__level = level

    def get_damage(self):
        return self.__atk - random.randint(1,3)

