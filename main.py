import ui_class as ui
from game_logic import Spiel


def initiate_game(name, class_type, window):
    spiel = Spiel(name, class_type, window)
    # Musik wird gestartet
    window.stop_music()
    # Musik Piraterie
    window.play_game_music()
    window.get_gamelogic(spiel)
    window.get_player(spiel.spieler)


def main():
    window = ui.App("v1.9.4")
    window.mainloop()

if __name__ == "__main__": # glaub das behebt, das wenn ich das importier, das es nicht nochmal ausgeführt wird
    main()
