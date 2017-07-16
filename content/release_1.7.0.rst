Release v1.7.0
##############

:date: 2017/07/15
:tags: python, release, changelog, postgres
:category: Blog
:slug: v1.7.0
:author: Irina Truong

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version using:

.. code:: bash

   $ pip install -U pgcli

Features:
---------

* Refresh completions after `COMMIT` or `ROLLBACK`. (Thanks: `Irina Truong`_)
* Use dbcli's Homebrew tap for installing pgcli on macOS (issue #718) (Thanks: `Thomas Roten`_).
* Only set `LESS` environment variable if it's unset. (Thanks: `Irina Truong`_)
* Quote schema in `SET SCHEMA` statement (issue #469) (Thanks: `Irina Truong`_)
* Use CLI Helpers for pretty printing query results (Thanks: `Thomas Roten`_).
* Skip serial columns when expanding * for `INSERT INTO foo(*` (Thanks: `Joakim Koljonen`_).
* Command line option to list databases (issue #206) (Thanks: `François Pietka`_)

Bug Fixes:
----------

* Fixed DSN aliases not being read from custom pgclirc (issue #717). (Thanks: `Irina Truong`_).

.. _`Joakim Koljonen`: https://github.com/koljonen
.. _`Amjith Ramanujam`: https://github.com/amjith
.. _`Thomas Roten`: https://github.com/tsroten
.. _`François Pietka`: https://github.com/fpietka
.. _`Irina Truong`: https://github.com/j-bennet
