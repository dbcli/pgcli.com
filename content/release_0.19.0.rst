Release v0.19.0
###############

:date: 2015-08-03
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.19.0

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version by:

.. code:: bash
   
   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

This release comes with metadata information in the completion menus. Now you
can see whether a completion suggestion is a table or a schema or a view. 
New special command (``\i``), latest prompt_toolkit with wider completion menus.

Features:
---------

* Wider completion menus can be enabled via the config file. (Thanks: `Jonathan Slenders`_)

  Open the config file (~/.pgclirc) and check if you have
  ``wider_completion_menu`` option available. If not add it in and set it to
  ``True``.

* Completion menu now has metadata information such as schema, table, column, view, etc., next to the suggestions. (Thanks: `Darik Gamble`_)
* Customizable history file location via config file. (Thanks: `Çağatay Yüksel`_)

  Add this line to your config file (~/.pgclirc) to customize where to store the history file. 

::

  history_file = /path/to/history/file

* Add support for running queries from a file using ``\i`` special command. (Thanks: `Michael Kaminsky`_)

Bug Fixes:
----------

* Always use utf-8 for database encoding regardless of the default encoding used by the database.
* Fix for None dereference on ``\d schemaname.`` with sequence. (Thanks: `Nathan Jhaveri`_)
* Fix a crashing bug in the autocompletion engine for some ``JOIN`` queries.
* Handle KeyboardInterrupt in pager and not quit pgcli as a consequence.

Internal Changes:
-----------------

* Added more behavioral tests (Thanks: `Iryna Cherniavska`_)
* Added code coverage to the tests. (Thanks: `Iryna Cherniavska`_)
* Run behavioral tests as part of TravisCI (Thanks: `Iryna Cherniavska`_)
* Upgraded prompt_toolkit version to 0.45 (Thanks: `Jonathan Slenders`_)
* Update the minumum required version of click to 4.1.

.. _`Darik Gamble`: https://github.com/darikg
.. _`Jonathan Slenders`: https://github.com/jonathanslenders
.. _`Iryna Cherniavska`: https://github.com/j-bennet
.. _`detailed instructions`: {filename}/pages/1.install.rst 
.. _`Nathan Jhaveri`: https://github.com/nathanjhaveri
.. _`Çağatay Yüksel`: https://github.com/cagatay
.. _`Michael Kaminsky`: https://github.com/mikekaminsky
