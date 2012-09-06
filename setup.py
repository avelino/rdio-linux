import os
import sys
import rdio.player

# Downloads setuptools if not find it before try to import
try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup

setup(
    name='rdio.player',
    version=rdio.player.__version__,
    url='http://rdio.com/',
    author=rdio.player.__author__,
    license=rdio.player.__license__,
    scripts=['rdio/player/rdio-player'],
    install_requires=['pygtk', 'pywebkitgtk'],)
