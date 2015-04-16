import os
import sys
from shutil import copyfile
import rdio.player.version as rpv

# Downloads setuptools if not find it before try to import
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='rdio.player',
    version=rpv.__version__,
    description=rpv.__description__,
    url='https://www.rdio.com/',
    author=rpv.__author__,
    author_email=rpv.__author_email__,
    license=rpv.__license__,
    data_files=[('', ['rdio/player/icon.png'])],
    classifiers=['Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Widget Sets',
        'Topic :: Utilities'],
    scripts=['rdio/player/rdio-player', 'rdio/player/version.py'],)
#    install_requires=['pygtk', 'pywebkitgtk'],)

dest = '/usr/share/rdio'
if not os.path.exists(dest):
    os.makedirs(dest)

copyfile('rdio/player/icon.png', '%s/icon.png' % dest)

# Add menu entry!
menu_entry = [
    '[Desktop Entry]',
    'Version='+rpv.__version__,
    'Name='+rpv.__appname__,
    'GenericName=Rdio Player',
    'Comment='+rpv.__description__,
    'Icon=/usr/share/rdio/icon.png',
    'Exec=rdio-player',
    'Type=Application',
    'Categories=AudioVideo;Player;GTK',
]

with open('/usr/share/applications/rdio.desktop', 'w+') as entry:
    for line in menu_entry:
        entry.write('%s\n' % line)
