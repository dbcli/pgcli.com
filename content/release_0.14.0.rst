Release v0.14.0
###############

:date: 2015-1-31
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.14.0

A huge release that adds completion support for schemas.

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can upgrade using:

.. code:: bash
   
   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

Features:
---------
* Add alias completion support to ON keyword. (Thanks: `Iryna Cherniavska`_)
* Add LIMIT keyword to completion. 
* Auto-completion for Postgres schemas. (Thanks: darikg_)
* Better unicode handling for datatypes, dbname and roles. 
* Add \timing command to time the sql commands. 
  This can be set via config file (~/.pgclirc) using ``timing = True``.
* Add different table styles for displaying output. 
  This can be changed via config file (~/.pgclirc) using ``table_format = fancy_grid``.
* Add confirmation before printing results that have more than 1000 rows. 

Bug Fixes:
----------

* Performance improvements to expanded view display (\x).
* Cast bytea files to text while displaying. (Thanks: `Daniel Rocco`_)
* Added a list of reserved words that should be auto-escaped.
* Auto-completion is now case-insensitive.
* Fix the broken completion for multiple sql statements. (Thanks: darikg_)

.. _`darikg`: https://github.com/darikg
.. _`Iryna Cherniavska`: https://github.com/j-bennet
.. _`Daniel Rocco`: https://github.com/drocco007 
.. _`detailed instructions`: {filename}/pages/1.install.rst 
