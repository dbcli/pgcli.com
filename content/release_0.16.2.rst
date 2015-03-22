Release v0.16.2
###############

:date: 2015-03-22
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.16.2

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version by:

.. code:: bash
   
   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

This is a bug-fix release that improves auto-completion and formatting of large
numbers in the output.

Bug Fixes:
----------

* Fix a bug where the schema qualifier was ignored by the auto-completion.
  As a result the suggestions for tables vs functions are cleaner. (Thanks: darikg_)
* Remove scientific notation when formatting large numbers. (Thanks: `Daniel Rocco`_)
* Add the FUNCTION keyword to auto-completion.
* Display NULL values as <null> instead of empty strings. 
* Fix the completion refresh when ``\connect`` is executed.

.. _`detailed instructions`: {filename}/pages/1.install.rst 
.. _`Daniel Rocco`: https://github.com/drocco007 
.. _darikg: https://github.com/darikg
