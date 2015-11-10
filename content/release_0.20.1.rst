Release v0.20.1
###############

:date: 2015-11-08
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.20.1
:author: Iryna Cherniavska

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version by:

.. code:: bash

   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

This is a bug fix release to fix ``pgcli`` crashing on startup in Windows.

Bug Fixes:
----------

* Fixed logging in Windows by switching the location of log and history file based on OS. (Thanks: Amjith, `Darik Gamble`_, `Iryna Cherniavska`_).

.. _`Darik Gamble`: https://github.com/darikg
.. _`Iryna Cherniavska`: https://github.com/j-bennet
.. _`detailed instructions`: {filename}/pages/1.install.rst
