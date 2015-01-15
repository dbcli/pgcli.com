Release v0.13.0
###############

:date: 2015-1-14
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.13.0

A small release that gets ``pgcli`` closer to being a drop in replacement for
``psql``.

.. code:: bash
   
   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

Features:
---------

* Add -d/--dbname option to the commandline. 
  eg: pgcli -d database
* Add the username as an argument after the database.
  eg: pgcli dbname user

Bug Fixes:
----------
* Fix the crash when \c fails.
* Fix the error thrown by \d when triggers are present.
* Fix broken behavior on \?. (Thanks: darikg_)

.. _`darikg`: https://github.com/darikg
.. _`detailed instructions`: {filename}/pages/1.install.rst 
