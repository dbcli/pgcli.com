Release v1.11.0
###############

:date: 2018/09/24
:tags: python, release, changelog, postgres
:category: Blog
:slug: v1.11.0
:author: Irina Truong

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version using:

.. code:: bash

   $ pip install -U pgcli

A very small release this time, but coming next is ``pgcli`` migration to `Python Prompt Toolkit`_ 2.0.

Features:
---------

* Respect ``\pset pager on`` and use pager when output is longer than terminal height (Thanks: `Max Rothman`_)

.. _`Max Rothman`: https://github.com/maxrothman
.. _`Python Prompt Toolkit`: https://github.com/jonathanslenders/python-prompt-toolkit
