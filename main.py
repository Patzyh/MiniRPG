import ui_class as ui
from game_logic import Spiel
import time


def initiate_game(name, class_type, window):
    spiel = Spiel(name, class_type, window)
    window.stop_music()
    window.play_game_music()
    window.get_gamelogic(spiel)
    window.get_player(spiel.spieler)


def main():
    window = ui.App("v0.0.13 INDEV")
    window.after(1000, window.play_title_music) # Play title music78765678
    window.mainloop()

print(__name__)

if __name__ == "__main__":
    main()
