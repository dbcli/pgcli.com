Release v0.17.0
###############

:date: 2015-05-26
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.17.0

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version by:

.. code:: bash
   
   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

This release comes with the latest version of prompt_tookit, better matching
algorithm in auto-completion, new special commands (``\\e``, ``\\dT``), fix CJK
dispaly and a lot more. Thanks to the many contributors.

Features:
---------

* Add support for auto-completing view names. (Thanks: `Darik Gamble`_)
* Add subsequence matching for completion. (Thanks: `Daniel Rocco`_)
  Previously completions only matched a table name if it started with the
  partially typed word. Now completions will match even if the partially typed
  word is in the middle of a suggestion.
  eg: When you type 'mig', 'django_migrations' will be suggested. 
* Completion for built-in tables and temporary tables are suggested after entering a prefix of ``pg_``. (Thanks: `Darik Gamble`_)
* Add place holder doc strings for special commands that are planned for implementation. (Thanks: `Iryna Cherniavska`_)
* Updated version of prompt_toolkit, now matching braces are highlighted. (Thanks: `Jonathan Slenders`)
* Added support of ``\\e`` command. Queries can be edited in an external editor. (Thanks: `Iryna Cherniavska`_)
  eg: When you type ``SELECT * FROM \e`` it will be opened in an external editor.
* Add special command ``\dT`` to show datatypes. (Thanks: `Darik Gamble`_)
* Add auto-completion support for datatypes in CREATE, SELECT etc. (Thanks: `Darik Gamble`_) 
* Improve the auto-completion in WHERE clause with logical operators. (Thanks: `Darik Gamble`_)
* 

Bug Fixes:
----------

* Fix the table formatting while printing multi-byte characters (Chinese, Japanese etc). (Thanks: `蔡佳男`_)
* Fix a crash when pg_catalog was present in search path. (Thanks: `Darik Gamble`_)
* Fixed a bug that broke `\\e` when prompt_tookit was updated. (Thanks: `François Pietka`_)
* Fix the display of triggers as shown in the ``\d`` output. (Thanks: `Dimitar Roustchev`_)
* Fix broken auto-completion for INNER JOIN, LEFT JOIN etc. (Thanks: `Darik Gamble`_)
* Fix incorrect super() calls in pgbuffer, pgtoolbar and pgcompleter. No change in functionality but protects against future problems. (Thanks: `Daniel Rocco`_)
* Add missing schema completion for CREATE and DROP statements. (Thanks: `Darik Gamble`_)
* Minor fixes around cursor cleanup.

.. _`Darik Gamble`: https://github.com/darikg
.. _`Iryna Cherniavska`: https://github.com/j-bennet
.. _`Daniel Rocco`: https://github.com/drocco007 
.. _`Jay Zeng`:  https://github.com/jayzeng 
.. _`蔡佳男`: https://github.com/xalley
.. _dp: https://github.com/ceocoder
.. _`Jonathan Slenders`: https://github.com/jonathanslenders
.. _`Dimitar Roustchev`: https://github.com/droustchev
.. _`François Pietka`: https://github.com/fpietka
.. _`detailed instructions`: {filename}/pages/1.install.rst 
