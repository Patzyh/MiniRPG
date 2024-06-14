import random

class Gegner:
    def __init__(self, enemytype=0):
        self.__leben = 100
        self.__enemytype = enemytype
        if self.__enemytype == 0:
            self.__enemytype = random.randint(1,3)
        self.__dead = False

        self.__enemy = [
            {"name": "Orc", "angriff": 14, "leben": 17},
            {"name": "Goblin", "angriff": 16, "leben": 15},
            {"name": "Geist", "angriff": 18, "leben": 13}
        ]

        self.__enemy = self.__enemy[self.__enemytype - 1]
        self.__name = self.__enemy["name"]

    def get_dead(self):
        return self.__dead

    def get_leben(self):
        return self.__leben

    def get_name(self):
        return self.__name

    def set_dead(self):
        self.__dead = True

    def set_leben(self, leben):
        self.__leben = leben

    def set_name(self, name):
        self.__name = name
