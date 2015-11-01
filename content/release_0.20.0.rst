Release v0.20.0
###############

:date: 2015-10-31
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.20.0

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version by:

.. code:: bash
   
   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

This version adds support for ``\\h``  command and ``\x auto`` command. Two
very important commands that bring us close to being a total replacement for
psql. This version can also handle really large databases without trouble
thanks to asynchronous completion refresh. Full details below:


Features:
---------
* Perform auto-completion refresh in background. (Thanks: Amjith, `Darik Gamble`_, `Iryna Cherniavska`_).

  When the auto-completion entries are refreshed, the update now happens in a
  background thread. This means large databases with thousands of tables are
  handled without blocking.
* Add support for ``\h`` command. (Thanks: `Stuart Quin`_).
 
  This is a huge deal. Users can now get help on an SQL command by typing:
  ``\h COMMAND_NAME`` in the pgcli prompt.
* Add support for ``\x auto``. (Thanks: `Stuart Quin`_).
 
  ``\\x auto`` will automatically switch to expanded mode if the output is wider
  than the display window.
* Don't hide functions from pg_catalog. (Thanks: `Darik Gamble`_).
* Suggest set-returning functions as tables. (Thanks: `Darik Gamble`_).
 
  Functions that return table like results will now be suggested in places of tables. 

* Suggest fields from functions used as tables. (Thanks: `Darik Gamble`_).
* Using ``pgspecial`` as a separate module. (Thanks: `Iryna Cherniavska`_).
* Make "enter" key behave as "tab" key when the completion menu is displayed. (Thanks: `Matheus Rosa`_).
* Support different error-handling options when running multiple queries. (Thanks: `Darik Gamble`_).
  
  When ``on_error = STOP`` in the config file, pgcli will abort execution if one of the queries results in an error. 
* Hide the password displayed in the process name in ``ps``. (Thanks: `Stuart Quin`_)
* Add ``CONCURRENTLY`` to keyword completion. (Thanks: `Johannes Hoff`_).

Bug Fixes:
----------
* Fix the ordering bug in `\\d+` display, this bug was displaying the wrong table name in the reference. (Thanks: `Tamas Boros`_).
* Only show expanded layout if valid list of headers provided. (Thanks: `Stuart Quin`_).
* Fix suggestions in compound join clauses. (Thanks: `Darik Gamble`_).
* Fix completion refresh in multiple query scenario. (Thanks: `Darik Gamble`_).
* Fix the broken timing information.
* Fix the removal of whitespaces in the output. (Thanks: `Jacek Wielemborek`_)
* Fix PyPI badge. (Thanks: `Artur Dryomov`_).

Improvements:
-------------
* Move config file to `~/.config/pgcli/config` instead of `~/.pgclirc` (Thanks: `inkn`_).
* Move literal definitions to standalone JSON files. (Thanks: `Darik Gamble`_).

Internal Changes:
-----------------
* Improvements to integration tests to make it more robust. (Thanks: `Iryna Cherniavska`_).

.. _`detailed instructions`: {filename}/pages/1.install.rst 
.. _`Darik Gamble`: https://github.com/darikg
.. _`Iryna Cherniavska`: https://github.com/j-bennet
.. _`Daniel Rocco`: https://github.com/drocco007 
.. _`Jay Zeng`:  https://github.com/jayzeng 
.. _`蔡佳男`: https://github.com/xalley
.. _dp: https://github.com/ceocoder
.. _`Jonathan Slenders`: https://github.com/jonathanslenders
.. _`Dimitar Roustchev`: https://github.com/droustchev
.. _`François Pietka`: https://github.com/fpietka
.. _`Ali Kargın`: https://github.com/sancopanco
.. _`Brett Atoms`: https://github.com/brettatoms 
.. _`Nathan Jhaveri`: https://github.com/nathanjhaveri
.. _`Çağatay Yüksel`: https://github.com/cagatay
.. _`Michael Kaminsky`: https://github.com/mikekaminsky
.. _`inkn`: inkn
.. _`Johannes Hoff`: Johannes Hoff
.. _`Matheus Rosa`: Matheus Rosa
.. _`Artur Dryomov`: https://github.com/ming13
.. _`Stuart Quin`: https://github.com/stuartquin
.. _`Tamas Boros`: https://github.com/TamasNo1
.. _`Jacek Wielemborek`: https://github.com/d33tah
