Release v0.15.X
###############

:date: 2015-02-08
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.15.X

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version by:

.. code:: bash
   
   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

This version adds more color schemes to the syntax highlighting. An attempt to
add support for PyPy by using psycopg2cffi failed. Python 3 support for
psycopg2cffi was only added recently and there are still a few corner cases
where it fails.

Features:
---------
* Add syntax color styles to config. Try ``syntax_style=fruity``. Availble themes
  are `manni`, `igor`, `xcode`, `vim`, `autumn`, `vs`, `rrt`, `native`,
  `perldoc`, `borland`, `tango`, `emacs`, `friendly`, `monokai`,
  `paraiso-dark`, `colorful`, `murphy`, `bw`, `pastie`, `paraiso-light`,
  `trac`, `default`, `fruity`.

* Add auto-completion for COPY statements.

Bug Fixes:
----------
* Treat boolean values as strings instead of ints.
* Make \di, \dv and \dt to be schema aware. (Thanks: darikg_)
* Make column name display unicode compatible. 
* Override the LESS options completely instead of appending to it. 

.. _`darikg`: https://github.com/darikg
.. _`detailed instructions`: {filename}/pages/1.install.rst 
