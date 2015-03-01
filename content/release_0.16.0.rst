Release v0.16.0
###############

:date: 2015-03-01
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.16.0

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version by:

.. code:: bash
   
   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

This release adds Vi-keybindings, improvements to special commands (new
additions \ds and \df) and a lot of annoyances. Many thanks to the
contributors.

Features:
---------
* Add \ds special command to show sequences. 
* Add Vi mode for keybindings. (Thanks: `Jay Zeng`_)
* Add a -v/--version flag to pgcli.
* Add completion for TEMPLATE keyword and smart-completion for 
  'CREATE DATABASE blah WITH TEMPLATE <tab>'. (Thanks: `Daniel Rocco`_)
* Add custom decoders to json/jsonb to emulate the behavior of psql. This
  removes the unicode prefix (eg: u'Éowyn') in the output. (Thanks: `Daniel Rocco`_)
* Add \df special command to show functions. (Thanks: darikg_)
* Make suggestions for special commands smarter. eg: \dn - only suggests schemas. (Thanks: darikg_)
* Print out the version and other meta info about pgcli at startup.

Bug Fixes:
----------
* Fix a rare crash caused by adding new schemas to a database. (Thanks: darikg_)
* Make \dt command honor the explicit schema specified in the arg. (Thanks: darikg_)
* Print BIGSERIAL type as Integer instead of Float.
* Show completions for special commands at the beginning of a statement. (Thanks: `Daniel Rocco`_)
* Allow special commands to work in a multi-statement case where multiple sql
  statements are separated by semi-colon in the same line. 

.. _darikg: https://github.com/darikg
.. _`Daniel Rocco`: https://github.com/drocco007 
.. _`Jay Zeng`:  https://github.com/jayzeng 
.. _`detailed instructions`: {filename}/pages/1.install.rst 
