Release v0.19.1
###############

:date: 2015-08-04
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.19.1

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version by:

.. code:: bash
   
   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

This is a minor bug fix release to fix a crashing bug during autocompletion.

Bug Fixes:
----------

* Fix an autocompletion bug that was crashing the completion engine when unknown keyword is entered. (Thanks: `Darik Gamble`_)


.. _`Darik Gamble`: https://github.com/darikg
.. _`detailed instructions`: {filename}/pages/1.install.rst 
