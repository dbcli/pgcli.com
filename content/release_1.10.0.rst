Release v1.10.0
###############

:date: 2018/07/14
:tags: python, release, changelog, postgres
:category: Blog
:slug: v1.10.0
:author: Irina Truong

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version using:

.. code:: bash

   $ pip install -U pgcli

This release adds new special commands ``\ev`` and ``\ef``, more table formats,
and a ``--user`` alias for ``--username`` option, to be compatible with psql. ``Pgcli``
also sets ``application_name`` to identify itself within postgres. Multiple bugs
were fixed.

This release was very special because we had a lot of first-time contributors, thanks
to `Amjith`_ leading a sprint on pgcli during PyCon 2018! It's wonderful to see that
spike of commits in mid-may:

.. image:: /images/pgcli-commits-2018.png

Our huge thanks to all the new contributors!

Features:
---------
* Add quit commands to the completion menu. (Thanks: `Jason Ribeiro`_)
* Add table formats to ``\T`` completion. (Thanks: `Jason Ribeiro`_)
* Support `\\ev``, ``\ef`` (#754). (Thanks: `Catherine Devlin`_)
* Add ``application_name`` to help identify pgcli connection to database (issue #868) (Thanks: `François Pietka`_)
* Add `--user` option, duplicate of `--username`, the same cli option like `psql` (Thanks: `Alexandr Korsak`_)

Internal changes:
-----------------

* Mark tests requiring a running database server as dbtest (Thanks: `Dick Marinus`_)
* Add an is_special command flag to MetaQuery (Thanks: `Rishi Ramraj`_)
* Ported Destructive Warning from mycli.
* Refactor Destructive Warning behave tests (Thanks: `Dick Marinus`_)

Bug Fixes:
----------
* Disable pager when using \watch (#837). (Thanks: `Jason Ribeiro`_)
* Don't offer to reconnect when we can't change a param in realtime (#807). (Thanks: `Amjith Ramanujam`_ and `Saif Hakim`_)
* Make keyring optional. (Thanks: `Dick Marinus`_)
* Fix ipython magic connection (#891). (Thanks: `Irina Truong`_)
* Fix not enough values to unpack. (Thanks: `Matthieu Guilbert`_)
* Fix unbound local error when destructive_warning is false. (Thanks: `Matthieu Guilbert`_)
* Render tab characters as 4 spaces instead of `^I`. (Thanks: `Artur Balabanov`_)

.. _`Jason Ribeiro`: https://github.com/jrib
.. _`Rishi Ramraj`: https://github.com/RishiRamraj
.. _`Matthieu Guilbert`: https://github.com/gma2th
.. _`Alexandr Korsak`: https://github.com/oivoodoo
.. _`Saif Hakim`: https://github.com/saifelse
.. _`Artur Balabanov`: https://github.com/arturbalabanov
.. _`Irina Truong`: https://github.com/j-bennet
.. _`Dick Marinus`: https://github.com/meeuw
.. _`Catherine Devlin`: https://github.com/catherinedevlin
.. _`Amjith Ramanujam`: https://github.com/amjith
.. _`Amjith`: https://github.com/amjith
.. _`François Pietka`: https://github.com/fpietka
