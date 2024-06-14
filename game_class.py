from player_class import Spieler
from enemy_class import Gegner


class Spiel:
    def __init__(self, name, class_type, window):
        self.__punkte = 0
        self.__ui = window
        print(type(self.__ui))
        self.__spieler = Spieler(name, class_type, self.__ui)

    def spielstand(self):
        print("Punkte: ", self.__punkte)

    def initate_fight(self):
        self.__gegner = Gegner()

    def attack(self):
        self.__gegner.set_leben(self.__gegner.get_leben() - self.__spieler.get_atk())
        if self.__gegner.get_leben() <= 0:
            self.__gegner.set_dead()
            self.__punkte += 1
            self.__gegner = Gegner()
            print("Gegner besiegt")
        else:
            self.__spieler.set_hp(self.__spieler.get_hp() - self.__gegner.get_atk())
            if self.__spieler.get_hp() <= 0:
                print("Spieler besiegt")
                self.stop()

    def get_player(self):
        return self.__spieler


    def spielende(self):
        self.spielstand()
        print("Spielende")

    def stop(self):
        self.spielende()

    def get_class_type(self):
        return self.__spieler.get_class_type()