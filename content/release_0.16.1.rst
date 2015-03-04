Release v0.16.1
###############

:date: 2015-03-03
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.16.1

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version by:

.. code:: bash
   
   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

This is a minor bug-fix release that fixes unicode issues with hstore.

Bug Fixes:
----------
* Fix unicode issues with hstore. Previously the unicode type caster for hstore
  was done via a hardcoded oid. This is wrong since the oid for hstore will
  vary between different databases. Now the oid is determined at the time of
  connection and a type caster is registered accordingly.
* Fix an error when database is changed using \\c.

.. _`detailed instructions`: {filename}/pages/1.install.rst 
