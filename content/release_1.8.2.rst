Release v1.8.2
##############

:date: 2017/12/22
:tags: python, release, changelog, postgres
:category: Blog
:slug: v1.8.2
:author: Irina Truong

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version using:

.. code:: bash

   $ pip install -U pgcli

Features:
---------

* Use other prompt (prompt_dsn) when connecting using --dsn parameter. (Thanks: `Marcin Sztolcman`_)
* Include username into password prompt. (Thanks: `Bojan Delić`_)

Internal changes:
-----------------

* Use temporary dir as config location in tests. (Thanks: `Dmitry B`_)
* Fix errors in the ``tee`` test (#795 and #797). (Thanks: `Irina Truong`_)
* Increase timeout for quitting pgcli. (Thanks: `Dick Marinus`_)

Bug Fixes:
----------

* Do NOT quote the database names in the completion menu (Thanks: `Amjith Ramanujam`_)
* Fix error in ``unix_socket_directories`` (#805). (Thanks: `Irina Truong`_)
* Fix the --list command line option tries to connect to 'personal' DB (#816). (Thanks: `Isank`_)

.. _`Amjith Ramanujam`: https://github.com/amjith
.. _`Dick Marinus`: https://github.com/meeuw
.. _`Irina Truong`: https://github.com/j-bennet
.. _`Marcin Sztolcman`: https://github.com/msztolcman
.. _`Dmitry B`: https://github.com/oxitnik
.. _`Isank`: https://github.com/isank
.. _`Bojan Delić`: https://github.com/delicb