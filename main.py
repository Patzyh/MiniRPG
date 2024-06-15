import ui_class as ui
from game_class import Spiel
from game_logic import GameLogic
import game_logic as logic
import time


def initiate_game(name, class_type, window):
    spiel = Spiel(name, class_type, window)
    class_stats = [spiel.get_player().get_hp()]


def main():
    window = ui.App("v0.0.13 INDEV")
    window.after(1000, window.play_title_music) # Play title music78765678
    game_logic = GameLogic(window)
    game_logic.spielablauf()
    window.mainloop()

print(__name__)

if __name__ == "__main__":
    main()