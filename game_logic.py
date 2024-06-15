from game_class import Spiel
from player_class import Spieler
from enemy_class import Gegner
import random
class GameLogic:
    def __init__(self, window):
        self.window = window

    def the_dark_forest(self):
        self.window.print("Du hörst Geräusche um dich herum und bist auf der Hut.", 4000)
        Spiel.set_location("Auf dem Weg zum Schloss")
        self.start_next_round()

    def hounted_castle(self):
        self.window.print("Dir läuft ein kalter Schauer über den Rücken. ", 4000)
        Spiel.set_location("Auf dem Weg zum Turm von Malakar")
        self.start_next_round()

    def malakars_tower(self):
        self.window.print("Du spürst die dunkle Aura, die von dem Turm ausgeht.", 4000)
        self.start_next_round()

    def start_next_round(self):
        standard_gegner = random.randint(1, 10)
        stealth = random.randint(1, 20)
        if standard_gegner == 1:
            self.initate_fight()
            self.window.print("Ein Gegner ist in der Nähe. Ich sollte mich auf einen Kampf vorbereiten.", 4000)
        else:
            self.window.print("Es scheint kein Gegner in der Nähe zu sein. Ich kann wohl unbesorgt weitergehen.",4000)
        if stealth == 1:
            self.window.print("Ein Gegener greift aus dem Schatten an.", 4000)
            self.initate_fight()
            self.stealth_attack()

    def laufen(self):
        x = Spiel.get_round()
        x += 1
        Spiel.set_round(x)
        if round == 5:
            self.window.print("Du befindest dich im dunklen Wald. Es ist Nacht und du siehst kaum die Hand vor Augen.", 6000)
            Spiel.set_location("The Dark Forest")
        elif round == 12:
            self.window.print("Du befindest dich vor einem alten Schloss. Es ist verlassen und du siehst nur noch die Ruinen.", 6000)
            Spiel.set_location("The Hounted Castle")
        elif round == 20:
            self.window.print("Du befindest dich vor Malakars Turm. Ein finsterer Ort, an dem böse Mächte wirken.", 6000)
            Spiel.set_location("Malakars Tower")

        if Spiel.get_location() == "The Dark Forest":
            self.the_dark_forest()
        elif Spiel.get_location() == "The Hounted Castle":
            self.hounted_castle()
        elif Spiel.get_location() == "Malakars Tower":
            self.malakars_tower()
        self.start_next_round()

    def stealth_attack(self):
        Spieler.set_hp(Spieler.get_hp() - Gegner.get_atk())
        if Spieler.get_hp() <= 0:
            self.window.print("Spieler besiegt",4000)
            self.stop()

    def spielablauf(self):
        while True:
           pass