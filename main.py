#!/usr/bin/env python

import gtk
import webkit
import gobject
import os


# init thread
gobject.threads_init()

window = gtk.Window()
window.set_title('Rdio for Linux')

# set size and position
window.resize(gtk.gdk.screen_width()-100,800)
window.move(0,0)

# set icon
def get_resource_path(rel_path):
    dir_of_py_file = os.path.dirname(__file__)
    rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
    abs_path_to_resource = os.path.abspath(rel_path_to_resource)
    return abs_path_to_resource

window.set_icon_from_file(get_resource_path("icon.png"))


view = webkit.WebView()
browser = view.get_settings()
browser.set_property("enable-plugins", True)
browser.set_property("enable-private-browsing", True)
browser.set_property("enable-page-cache", True)
view.set_settings(browser)

view.open('https://www.rdio.com/signin/')

window.add(view)
window.show_all()


window.connect('delete-event', lambda window, event: gtk.main_quit())

gtk.main()
