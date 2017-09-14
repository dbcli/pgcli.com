Release v1.8.0
##############

:date: 2017/09/14
:tags: python, release, changelog, postgres
:category: Blog
:slug: v1.8.0
:author: Irina Truong

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version using:

.. code:: bash

   $ pip install -U pgcli

Features:
---------

* Add fish-style auto-suggestion from history. (Thanks: `Amjith Ramanujam`_)
* Improved formatting of arrays in output (Thanks: `Joakim Koljonen`_)
* Don't quote identifiers that are non-reserved keywords. (Thanks: `Joakim Koljonen`_)
* Remove the ``...`` in the continuation prompt and use empty space instead. (Thanks: `Amjith Ramanujam`_)
* Add \conninfo and handle more parameters with \c (issue #716) (Thanks: `François Pietka`_)

Internal changes:
-----------------
* Preliminary work for a future change in outputting results that uses less memory. (Thanks: `Dick Marinus`_)
* Remove import workaround for OrderedDict, required for python < 2.7. (Thanks: `Andrew Speed`_)
* Use less memory when formatting results for display (Thanks: `Dick Marinus`_).
* Port auto_vertical feature test from mycli to pgcli. (Thanks: `Dick Marinus`_)
* Drop wcwidth dependency (Thanks: `Dick Marinus`_)

Bug Fixes:
----------

* Fix the way we get host when using DSN (issue #765) (Thanks: `François Pietka`_)
* Add missing keyword COLUMN after DROP (issue #769) (Thanks: `François Pietka`_)
* Don't include arguments in function suggestions for backslash commands (Thanks: `Joakim Koljonen`_)
* Optionally use POSTGRES_USER, POSTGRES_HOST POSTGRES_PASSWORD from environment (Thanks: `Dick Marinus`_)

.. _`Joakim Koljonen`: https://github.com/koljonen
.. _`Amjith Ramanujam`: https://github.com/amjith
.. _`François Pietka`: https://github.com/fpietka
.. _`Dick Marinus`: https://github.com/meeuw
.. _`Andrew Speed`: https://github.com/AndrewSpeed
