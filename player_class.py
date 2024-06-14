import random


class Spieler:
    def __init__(self, name, class_type):
        self.__name = name
        self.__level = 0
        class_types = {
            "Kämpfer": {"health": 19, "atk": 14},
            "Bogenschütze": {"health": 17, "atk": 17},
            "Magier": {"health": 15, "atk": 20}
        }

        if class_type in class_types:
            self.__health = class_types[class_type]["health"]
            self.__atk = class_types[class_type]["atk"]

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

