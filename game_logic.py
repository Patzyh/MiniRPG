from game_class import Spiel
from player_class import Spieler
from enemy_class import Gegner
import random


class GameLogic:
    def __init__(self, window):
        self.__window = window

    def the_dark_forest(self):
        self.__window.print("Du hörst Geräusche um dich herum und bist auf der Hut.", 4000)
        Spiel.location.setter("Auf dem Weg zum Schloss")
        self.start_next_round()

    def hounted_castle(self):
        self.__window.print("Dir läuft ein kalter Schauer über den Rücken. ", 4000)
        Spiel.location.setter("Auf dem Weg zum Turm von Malakar")
        self.start_next_round()

    def malakars_tower(self):
        self.__window.print("Du spürst die dunkle Aura, die von dem Turm ausgeht.", 4000)
        self.start_next_round()

    def start_next_round(self):
        standard_gegner = random.randint(1, 10)
        stealth = random.randint(1, 20)
        if standard_gegner == 1:
            self.initate_fight()
            self.__window.print("Ein Gegner ist in der Nähe. Ich sollte mich auf einen Kampf vorbereiten.", 4000)
        else:
            self.__window.print("Es scheint kein Gegner in der Nähe zu sein. Ich kann wohl unbesorgt weitergehen.", 4000)
        if stealth == 1:
            self.__window.print("Ein Gegener greift aus dem Schatten an.", 4000)
            self.initate_fight()
            self.stealth_attack()

    def laufen(self):
        Spiel.round.setter(Spiel.round.getter() + 1)
        Spiel.update_location()
        if Spiel.location.getter() == "The Dark Forest":
            self.the_dark_forest()
        elif Spiel.location.getter() == "The Hounted Castle":
            self.hounted_castle()
        elif Spiel.location.getter() == "Malakars Tower":
            self.malakars_tower()
        self.start_next_round()

    def stealth_attack(self):
        Spieler.set_hp(Spieler.get_hp() - Gegner.atk.getter())
        if Spieler.get_hp() <= 0:
            self.__window.print("Spieler besiegt", 4000)
            self.stop()

    def spielablauf(self):
        while True:
           pass