Release v2.0.2
##############

:date: 2019/01/02
:tags: python, release, changelog, postgres
:category: Blog
:slug: v2.0.2
:author: Irina Truong

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version using:

.. code:: bash

   $ pip install -U pgcli

After the update of ``pgcli`` to use ``prompt-toolkit 2.0``, there were quite a few complaints
about performance, in particular, slow autocompletions. This release attempts to address
the problem. Additionally, thanks to our newest contributor `Ignacio Campabadal`_, it is
now possible to supply username with a ``-u`` flag, same as ``mycli``.

Features:
---------

* Allows passing the ``-u`` flag to specify a username. (Thanks: `Ignacio Campabadal`_)
* Fix for lag in v2 (#979). (Thanks: `Irina Truong`_)

.. _`Ignacio Campabadal`: https://github.com/igncampa
.. _`Irina Truong`: https://github.com/j-bennet
