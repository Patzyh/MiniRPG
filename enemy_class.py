import random

class Gegner:
    def __init__(self, enemytype=0, window=None):
        self.__enemytype = enemytype
        if self.__enemytype == 0:
            self.__enemytype = random.randint(1, 3)
        else:
            self.__enemytype = enemytype
        self.__dead = False
        self.__ui = window

        self.__enemy = [ # haben wir selber gebalanced, sonst wärs legit unmöglich
            {"name": "Orc", "angriff": 14, "leben": 17},
            {"name": "Goblin", "angriff": 16, "leben": 15},
            {"name": "Geist", "angriff": 18, "leben": 13},
            {"name": "Malakar", "angriff": 20, "leben": 50}
        ]

        self.__enemy = self.__enemy[self.__enemytype - 1]
        self.__name = self.__enemy["name"]
        self.__leben = self.__enemy["leben"]
        self.__maxhealth = self.__enemy["leben"]

        self.__ui.create_enemybar(self)

    @property
    def dead(self):
        return self.__dead

    @dead.setter
    def dead(self, dead):
        self.__dead = dead
        self.__ui.remove_enemybar()

    @property
    def leben(self):
        return self.__leben

    @leben.setter
    def leben(self, hp):
        if hp > self.__maxhealth:
            hp = self.__maxhealth
        self.__leben = hp
        self.__ui.update_enemybar(hp / self.__maxhealth)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def atk(self):
        return self.__enemy["angriff"]

    @atk.setter
    def atk(self, atk):
        self.__enemy["angriff"] = atk
