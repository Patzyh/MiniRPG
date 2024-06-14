from time import time as Zeit
from player_class import Spieler
from enemy_class import Gegner

class Spiel:
    def __init__(self):
        self.spieler = Spieler()
        self.gegner = Gegner()
        self.zeit = Zeit()
        self.zeit.start()
        self.punkte = 0

    def spielstand(self):
        print("Punkte: ", self.punkte)
        print("Zeit: ", self.zeit.get_time())

    def spielzug(self):
        self.spieler.ziehe()
        self.gegner.ziehe()
        self.zeit.tick()

    def spielende(self):
        self.zeit.stop()
        self.spielstand()
        print("Spielende")

    def start(self):
        while self.zeit.get_time() > 0:
            self.spielzug()
        self.spielende()