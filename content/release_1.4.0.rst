Release v1.4.0
##############

:date: 2017/01/11
:tags: python, release, changelog, postgres
:category: Blog
:slug: v1.4.0
:author: Irina Truong

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version using:

.. code:: bash

   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

Features:
---------

* Search table suggestions using initialisms. (Thanks: `Joakim Koljonen`_).
* Support for table-qualifying column suggestions. (Thanks: `Joakim Koljonen`_).
* Display transaction status in the toolbar. (Thanks: `Joakim Koljonen`_).
* Display vi mode in the toolbar. (Thanks: `Joakim Koljonen`_).
* Added --prompt option. (Thanks: `Irina Truong`_).

Bug Fixes:
----------

* Fix scoping for columns from CTEs. (Thanks: `Joakim Koljonen`_)
* Fix crash after `with`. (Thanks: `Joakim Koljonen`_).
* Fix issue #603 (`\i` raises a TypeError). (Thanks: `Emanuele Gaifas`_).


Internal Changes:
-----------------

* Set default data_formatting to nothing. (Thanks: `Amjith Ramanujam`_).
* Increased minimum prompt_toolkit requirement to 1.0.9. (Thanks: `Irina Truong`_).

.. _`detailed instructions`: {filename}/pages/1.install.rst
.. _`Joakim Koljonen`: https://github.com/koljonen
.. _`Amjith Ramanujam`: https://github.com/amjith
.. _`Irina Truong`: https://github.com/j-bennet
.. _`Emanuele Gaifas`: https://github.com/lelit
