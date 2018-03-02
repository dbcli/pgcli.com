Release v1.9.0, pgspecial 1.10.0
################################

:date: 2018/03/02
:tags: python, release, changelog, postgres
:category: Blog
:slug: v1.9.0
:author: Irina Truong

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version using:

.. code:: bash

   $ pip install -U pgcli

This release adds ``\pset pager`` and ``\T`` to control output, as well as ``--list-dsn``, and we
just welcomed a new contributor, `Frederic Aoustin`_. Updated ``pgspecial`` includes ``\dD``
command, and ``$1`` syntax for favorite query parameters.

Features:
---------

* Manage pager by ``\pset pager`` and add ``enable_pager`` to the config file (Thanks: `Frederic Aoustin`_).
* Add support for ``\T`` command to change format output. (Thanks: `Frederic Aoustin`_).
* Add option ``--list-dsn`` (Thanks: `Frederic Aoustin`_).

Internal changes:
-----------------

* Removed support for Python 3.3. (Thanks: `Irina Truong`_)

This release also bumps ``pgspecial`` requirement to 1.10.0. The new version of ``pgspecial``
adds:

Features:
---------

* Add support for ``\dD`` command. (Thanks: `Lele Gaifax`_).
* Add support for parameters ``$1...$n`` in query (Thanks: `Frederic Aoustin`_).

Bug fixes:
----------

* Fix listing of table inheritance in ``\d`` command. (Thanks: `Lele Gaifax`_).

.. _`Irina Truong`: https://github.com/j-bennet
.. _`Bojan Delić`: https://github.com/delicb
.. _`Frederic Aoustin`: https://github.com/fraoustin
.. _`Lele Gaifax`: https://github.com/lelit
