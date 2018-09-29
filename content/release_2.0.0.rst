Release v2.0.0
##############

:date: 2018/09/28
:tags: python, release, changelog, postgres
:category: Blog
:slug: v2.0.0
:author: Irina Truong

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version using:

.. code:: bash

   $ pip install -U pgcli

This ``pgcli`` release has only one feature in it: migration to `Python Prompt Toolkit`_ 2.0. The
migration was non-trivial, because prompt-toolkit was reworked almost from the ground up, and 2.0
is not compatible with 1.x. But now, ``pgcli`` can finally use those `exciting new features`_ that
prompt-toolkit 2.0 has.

Many thanks to `Jonathan Slenders`_ and `Dick Marinus`_, who worked hard on the
migration!

Things to be aware of
=====================

* ``mycli`` did not yet migrate to prompt-toolkit 2.0. Until it does,
  ``pgcli`` and ``mycli`` can't be installed into the same venv.
* Same goes for ``ipython``. It already migrated, but is not yet released.
  To install ``ipython`` into the same venv as ``pgcli``, you'll have to
  do it from master:

.. code:: bash

    $ pip install pip install git+https://github.com/ipython/ipython.git

As always, we are here to help in case of any issues with the new release:

https://github.com/dbcli/pgcli/issues

.. _`Jonathan Slenders`: https://github.com/jonathanslenders
.. _`Dick Marinus`: https://github.com/meeuw
.. _`Python Prompt Toolkit`: https://github.com/jonathanslenders/python-prompt-toolkit
.. _`exciting new features`: https://python-prompt-toolkit.readthedocs.io/en/master/pages/upgrading.html#some-new-features
