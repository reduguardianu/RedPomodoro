import gtk

from gui.TrayIcon import TrayIcon
from PomodoroLogic import PomodoroLogic

import gobject

gobject.threads_init()

class Pomodoro(gtk.Window):
    def __init__(self):
        super(Pomodoro, self).__init__()

        self.set_size_request(600, 600)
        self.set_position(gtk.WIN_POS_MOUSE)

        self.connect("delete-event", self.close_handler)

        self.trayIcon = TrayIcon(self.show)
        self.trayIcon.start_item.connect("activate", self.start)
        self.trayIcon.stop_item.connect("activate", self.stop)
        self.add(gtk.Label("AAAA"))
        self.show_all()

    def start(self, w):
        self.trayIcon.start_item.set_sensitive(False)
        self.trayIcon.stop_item.set_sensitive(True)
        self.logic = PomodoroLogic(55, 5, self.trayIcon.update_text)
        self.logic.start()

    def stop(self, w):
        self.trayIcon.start_item.set_sensitive(True)
        self.trayIcon.stop_item.set_sensitive(False)
        self.logic.cancel()
        self.logic = None
        self.trayIcon.update_text("")

    def close_handler(self, widget, data):
        pomodoro.hide()
        return True


if __name__ == "__main__":
    pomodoro = Pomodoro()
    gtk.main()
