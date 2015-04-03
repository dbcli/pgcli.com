Release v0.16.3
###############

:date: 2015-04-02
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.16.3

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version by:

.. code:: bash
   
   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

This is a minor bug-fix release that fixes the syntax-highlighting of various
Postgres specific keywords and adds the ability to surface messages thrown by
sql exceptions.

Bug Fixes:
----------

* Add more SQL keywords for auto-complete suggestion.
* Messages raised as part of stored procedures are no longer ignored.
* Use postgres flavored syntax highlighting instead of generic ANSI SQL.

.. _`detailed instructions`: {filename}/pages/1.install.rst 
