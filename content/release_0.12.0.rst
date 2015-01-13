Release v0.12.0
###############

:date: 2015-1-13
:tags: python, release, changelog
:category: Blog
:slug: v0.12.0

A feature packed release.

0.12.0
======

Features:
---------

* Upgrade to prompt_toolkit version 0.26 (Thanks:`Karl-Aksel Puulmann`_) 

  - Adds Ctrl-left/right to move the cursor one word left/right respectively.
  - Internal API changes.

* IPython integration through `ipython-sql`_ (Thanks:`darikg`_)

  - Add an ipython magic extension to embed pgcli inside ipython. (more details to follow)
  - Results from a pgcli query are sent back to ipython. 

* Multiple sql statments in the same line separated by semi-colon. (Thanks:`Karl-Aksel Puulmann`_)

.. _`ipython-sql`: https://github.com/catherinedevlin/ipython-sql

Bug Fixes:
----------

* Fix 'message' attribute not found exception in Python 3. (Thanks:`Ludovic Gasc`_ )
* Use the database username as the database name instead of defaulting to OS username. (Thanks:`François Pietka`_)
* Auto-completion for auto-escaped column/table names.
* Fix i-reverse-search to work in prompt_toolkit version 0.26.

.. _`Karl-Aksel Puulmann`: https://github.com/macobo
.. _`darikg`: https://github.com/darikg
.. _`Ludovic Gasc`: https://github.com/GMLudo
.. _`François Pietka`: https://github.com/fpietka
