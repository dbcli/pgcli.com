Release v2.1.0
##############

:date: 2019/04/05
:tags: python, release, changelog, postgres
:category: Blog
:slug: v2.1.0
:author: Irina Truong

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version using:

.. code:: bash

   $ pip install -U pgcli

This version comes with quite a few fixes and a couple of nice usability improvements, including automatic reconnect.

Features:
---------

* Keybindings for closing the autocomplete list. (Thanks: `easteregg`_)
* Reconnect automatically when server closes connection. (Thanks: `Scott Brenstuhl`_)

Bug fixes:
----------
* Avoid error message on the server side if hstore extension is not installed in the current database (#991). (Thanks: `Marcin Cieślak`_)
* All pexpect submodules have been moved into the pexpect package as of version 3.0. Use pexpect.TIMEOUT (Thanks: `Marcin Cieślak`_)
* Resizing pgcli terminal kills the connection to postgres in python 2.7 (Thanks: `Amjith Ramanujam`_)
* Fix crash retrieving server version with ``--single-connection``. (Thanks: `Irina Truong`_)
* Cannot quit application without reconnecting to database (#1014). (Thanks: `Irina Truong`_)
* Password authentication failed for user "postgres" when using non-default password (#1020). (Thanks: `Irina Truong`_)

Internal:
---------

* (Fixup) Clean up and add behave logging. (Thanks: `Marcin Cieślak`_, `Dick Marinus`_)
* Override VISUAL environment variable for behave tests. (Thanks: `Marcin Cieślak`_)
* Remove build dir before running sdist, remove stray files from wheel distribution. (Thanks: `Dick Marinus`_)
* Fix unit tests, unhashable formatted text since new python prompttoolkit  version. (Thanks: `Dick Marinus`_)

.. _`Marcin Cieślak`: https://github.com/saper
.. _`Scott Brenstuhl`: https://github.com/808sAndBR
.. _`easteregg`: https://github.com/verfriemelt-dot-org
.. _`Amjith Ramanujam`: https://blog.amjith.com
.. _`Dick Marinus`: https://github.com/meeuw
.. _`Irina Truong`: https://github.com/j-bennet
