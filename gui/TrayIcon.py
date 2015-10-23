import gtk
import cairo
from gtk import gdk
import appindicator
import os

class TrayIcon(appindicator.Indicator):
    def __init__(self, showHandler):
        super(TrayIcon, self).__init__("pomodoro", os.path.join(os.path.dirname(os.path.realpath(__file__)),"..", "gfx", "pomodoro.png"), appindicator.CATEGORY_APPLICATION_STATUS)
        self.set_status( appindicator.STATUS_ACTIVE )


        self.start_item = gtk.MenuItem("Start")
        self.stop_item = gtk.MenuItem("Stop")
        quit_item = gtk.MenuItem("Quit")
        self.stop_item.set_sensitive(False)
        quit_item.connect("activate", gtk.main_quit)
        show_item = gtk.MenuItem("Show")
        show_item.connect("activate", lambda w : showHandler())
        self.menu = gtk.Menu()
        self.menu.append(self.start_item)
        self.menu.append(self.stop_item)
        self.menu.append(show_item)
        self.menu.append(quit_item)
        self.set_menu(self.menu)
        self.menu.show_all()

    def update_text(self, text):
        self.set_label(text)
