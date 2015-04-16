import os
import sys
from shutil import copyfile
from rdio.player import version

# Downloads setuptools if not find it before try to import
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='rdio',
    version=version.__version__,
    description=version.__description__,
    url='https://www.rdio.com/',
    author=version.__author__,
    author_email=version.__author_email__,
    license=version.__license__,
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
    'Version='+version.__version__,
    'Name='+version.__appname__,
    'GenericName=Rdio Player',
    'Comment='+version.__description__,
    'Icon=/usr/share/rdio/icon.png',
    'Exec=rdio-player',
    'Type=Application',
    'Categories=AudioVideo;Player;GTK',
]

with open('/usr/share/applications/rdio.desktop', 'w+') as entry:
    for line in menu_entry:
        entry.write('%s\n' % line)