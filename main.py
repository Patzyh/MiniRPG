import ui_class as ui
from game_class import Spiel
import time


def initiate_game(name, class_type, window):
    spiel = Spiel(name, class_type, window)
    class_stats = [spiel.get_player().get_hp()]
    time.sleep(1)
    spiel.get_player().set_hp(17)



def main():
    window = ui.App("v0.0.13 INDEV")
    window.mainloop()


print(__name__)

if __name__ == "__main__":
    main()

