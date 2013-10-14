UCD Name database
=================

This repository offers the mapping between Unicode code points and
their standard name in various formats:

- ``ucd.json``: JSON (RFC 4627, ECMA-404)
- ``ucd.html``: HTML
- ``ucd.h``: C/C++ header file, with preprocessor macro definitions
- ``ucd.py``: Python module

See the ``tables`` subdirectory for the generated files.

You can use the Python module as follows:

- you know a character's name, you want to know its code.

  For example, you want to know which code corresponds to "COMET":

  .. code:: python

     import ucd
     print (hex(ucd.COMET))  # should print 2604

     # alternatively:
     name = "COMET"
     print (hex(getattr(ucd, name)))

- you know the character's code, you want to know its name.

  For example, you want to know what is the standard name of character
  0x262f:

  .. code:: python

     import ucd
     print (ucd.names[0x262f])  # should print YIN YANG
