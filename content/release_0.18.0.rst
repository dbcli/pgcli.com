Release v0.18.0
###############

:date: 2015-06-16
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.18.0

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version by:

.. code:: bash
   
   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

This release comes with the ability to save favorite queries, fuzzy matching in
auto-completion, new special commands (``\#``), fix unicode issues in Windows and 
lot more. Thanks to the many contributors.

Features:
---------

* Add fuzzy matching for the table names and column names. 

  Matching very long table/column names are now easier with fuzzy matching. The
  fuzzy match works like the fuzzy open in SublimeText or Vim's Ctrl-P plugin. 

  eg: Typing ``djmiviw`` will match **dj**\ ango\_\ **mi**\ gration\_\ **vi**\ ews since it is able to
  match parts of the input to the full table name.

* Timing information is now shown in seconds.
  
  The ``Command Time`` and ``Format Time`` are now displayed in seconds instead
  of a unitless number displayed in scientific notation.

* Support for named queries (favorite queries). (Thanks: `Brett Atoms`_)

  Frequently typed queries can now be saved and recalled using a name using
  newly added special commands (``\n[+]``, ``\ns``, ``\nd``).

  eg: 

::

    # Save a query
    pgcli> \ns simple select * from foo
    saved

    # List all saved queries
    pgcli> \n+

    # Execute a saved query
    pgcli> \n simple

    # Delete a saved query
    pgcli> \nd simple

* Pasting queries into the pgcli repl is orders of magnitude faster. (Thanks: `Jonathan Slenders`_)

* Add support for PGPASSWORD environment variable to pass the password for the
  postgres database. (Thanks: `Iryna Cherniavska`_)

* Add the ability to manually refresh autocompletions by typing ``\#`` or
  ``\refresh``. This is useful if the database was updated by an external means
  and you'd like to refresh the auto-completions to pick up the new change.


Bug Fixes:
----------

* Fix an error when running ``\d table_name`` when running on a table with rules. (Thanks: `Ali Kargın`_)
* Fix a pgcli crash when entering non-ascii characters in Windows. (Thanks: `Darik Gamble`_, `Jonathan Slenders`_)
* Faster rendering of expanded mode output by making the horizontal separator a fixed length string. 
* Completion suggestions for the ``\c`` command are not auto-escaped by default. 

Internal Changes:
-----------------

* Complete refactor of handling the back-slash commands. It is now easier to
  add new special back-slash commands using a decorator.
* Upgrade prompt_toolkit to 0.42. (Thanks: `Jonathan Slenders`_)
* Change the config file management to use ConfigObj.(Thanks: `Brett Atoms`_)
* Add integration tests using ``behave``. (Thanks: `Iryna Cherniavska`_)

.. _`Darik Gamble`: https://github.com/darikg
.. _`Jonathan Slenders`: https://github.com/jonathanslenders
.. _`Iryna Cherniavska`: https://github.com/j-bennet
.. _`detailed instructions`: {filename}/pages/1.install.rst 
.. _`Ali Kargın`: https://github.com/sancopanco
.. _`Brett Atoms`: https://github.com/brettatoms 
