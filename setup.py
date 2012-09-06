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
    description=rdio.player.__description__,
    url='http://rdio.com/',
    author=rdio.player.__author__,
    author_email=rdio.player.__author_email__,
    license=rdio.player.__license__,
    classifiers=['Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Widget Sets',
        'Topic :: Utilities'],
    scripts=['rdio/player/rdio-player'],)
#    install_requires=['pygtk', 'pywebkitgtk'],)
