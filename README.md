rdio-linux
==========

Application RDIO for Linux


Install
=======

Install using 

```
python2 setup.py install
```

You will need to install the dependencies listed below first as well (you may
also do this via your distribution's package manager).

PyGTK
-----

```bash
$ wget http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.24/pygtk-2.24.0.tar.gz
$ tar -xvf pygtk-2.24.0.tar.gz
$ cd pygtk-2.24.0
$ ./configure
$ make
$ sudo make install
```


PyWebkitGTK
-----------

```bash
$ wget http://pywebkitgtk.googlecode.com/files/pywebkitgtk-1.1.8.tar.gz
$ tar -xvf pywebkitgtk-1.1.8.tar.gz
$ cd pywebkitgtk-1.1.8
$ ./configure
$ make
$ sudo make install
```
