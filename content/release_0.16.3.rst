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

This is a bug-fix release that improves auto-completion and formatting of large
numbers in the output.

Bug Fixes:
----------

* Add more SQL keywords for auto-complete suggestion.
* Messages raised as part of stored procedures are no longer ignored.
* Use postgres flavored syntax highlighting instead of generic ANSI SQL.

.. _`detailed instructions`: {filename}/pages/1.install.rst 
