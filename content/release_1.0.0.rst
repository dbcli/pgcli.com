Release v1.0.0
###############

:date: 2016/06/28
:tags: python, release, changelog, postgres
:category: Blog
:slug: v1.0.0

``Pgcli`` is a command line interface for Postgres database that does
auto-completion and syntax highlighting. You can install this version using:

.. code:: bash

   $ pip install -U pgcli

Check `detailed instructions`_ if you're having difficulty.

This is a major update with a ton of new features a lot of bug fixes. Some of
the highlights include support for Redshift and Postgres 8.x versions. Added
meta commands such as ``\copy``, ``\o``, ``\dx`` path completion for ``\i``.
The completions for JOIN and COLUMN were enhanced.

Please file any bug reports to github issues: https://github.com/dbcli/pgcli/issues


Features:
---------

* Upgrade to prompt-toolkit 1.0.0. (Thanks: `Jonathan Slenders`_).
* Add support for `\o` command to redirect query output to a file. (Thanks: `Tim Sanders`_).
* Add `\i` path completion. (Thanks: `Anthony Lai`_).
* Connect to a dsn saved in config file. (Thanks: `Rodrigo Ramírez Norambuena`_).
* Upgrade sqlparse requirement to version 0.1.19. (Thanks: `Fernando L. Canizo`_).
* Add timestamptz to DATE custom extension. (Thanks: `Fernando Mora`_).
* Ensure target dir exists when copying config. (Thanks: `David Szotten`_).
* Handle dates that fall in the B.C. range. (Thanks: `Stuart Quin`_).
* Pager is selected from config file or else from environment variable. (Thanks: `Fernando Mora`_).
* Add support for Amazon Redshift. (Thanks: `Timothy Cleaver`_).
* Add support for Postgres 8.x. (Thanks: `Timothy Cleaver`_ and `Darik Gamble`_)
* Don't error when completing parameter-less functions. (Thanks: `David Szotten`_).
* Concat and return all available notices. (Thanks: `Stuart Quin`_).
* Handle unicode in record type. (Thanks: `Amjith Ramanujam`_).
* Added humanized time display. Connect #396. (Thanks: `Irina Truong`_).
* Add EXPLAIN keyword to the completion list. (Thanks: `Amjith Ramanujam`_).
* Sort completions based on most recently used. (Thanks: `Darik Gamble`)
* Expand '*' into column list during completion. This can be triggered by hitting `<tab>` after the '*' character in the sql while typing. (Thanks: `Joakim Koljonen`_)
* Add a limit to the warning about too many rows. This is controlled by a new config value in ~/.config/pgcli/config. (Thanks: `Anže Pečar`_)
* Improved argument list in function parameter completions. (Thanks: `Joakim Koljonen`_)
* Column suggestions after the COLUMN keyword. (Thanks: `Darik Gamble`_)
* Filter out trigger implemented functions from the suggestion list. (Thanks: `Daniel Rocco`_)
* State of the art JOIN clause completions that suggest entire conditions. (Thanks: `Joakim Koljonen`_)
* Suggest fully formed JOIN clauses based on Foreign Key relations. (Thanks: `Joakim Koljonen`_)
* Add support for `\dx` meta command to list the installed extensions. (Thanks: `Darik Gamble`_)
* Add support for `\copy` command. (Thanks: `Catherine Devlin`_)

Bugs:
-----

* Fix bug where config writing would leave a '~' dir. (Thanks: `James Munson`_).
* Fix auto-completion breaking for table names with caps. (Thanks: `Anthony Lai`_).
* Fix lexical ordering bug. (Thanks: `Anthony Lai`_).
* Use lexical order to break ties when fuzzy matching. (Thanks: `Daniel Rocco`_).
* Fix the bug in auto-expand mode when there are no rows to display. (Thanks: `Amjith Ramanujam`_).
* Fix broken `\i` after #395. (Thanks: `David Szotten`_).
* Fix multi-way joins in auto-completion. (Thanks: `Darik Gamble`_)
* Display null values as <null> in expanded output. (Thanks: `Amjith Ramanujam`_).
* Robust support for Postgres version less than 9.x. (Thanks: `Darik Gamble`_)

Internal Changes:
-----------------

* Update config file location in README. (Thanks: `Ari Summer`_).
* Explicitly add wcwidth as a dependency. (Thanks: `Amjith Ramanujam`_).
* Add tests for the format_output. (Thanks: `Amjith Ramanujam`_).
* Lots of tests for pgcompleter. (Thanks: `Darik Gamble`_).
* Update pgspecial dependency to 1.4.0.
* Added sdist upload to release script. (Thanks: `Irina Truong`_).

.. _`detailed instructions`: {filename}/pages/1.install.rst
.. _`Amjith Ramanujam`: https://github.com/amjith
.. _`Darik Gamble`: https://github.com/darikg
.. _`Iryna Cherniavska`: https://github.com/j-bennet
.. _`Daniel Rocco`: https://github.com/drocco007 
.. _`Jay Zeng`:  https://github.com/jayzeng 
.. _`蔡佳男`: https://github.com/xalley
.. _dp: https://github.com/ceocoder
.. _`Jonathan Slenders`: https://github.com/jonathanslenders
.. _`Dimitar Roustchev`: https://github.com/droustchev
.. _`François Pietka`: https://github.com/fpietka
.. _`Ali Kargın`: https://github.com/sancopanco
.. _`Brett Atoms`: https://github.com/brettatoms 
.. _`Nathan Jhaveri`: https://github.com/nathanjhaveri
.. _`Çağatay Yüksel`: https://github.com/cagatay
.. _`Michael Kaminsky`: https://github.com/mikekaminsky
.. _`inkn`: inkn
.. _`Johannes Hoff`: Johannes Hoff
.. _`Matheus Rosa`: Matheus Rosa
.. _`Artur Dryomov`: https://github.com/ming13
.. _`Stuart Quin`: https://github.com/stuartquin
.. _`Tamas Boros`: https://github.com/TamasNo1
.. _`Jacek Wielemborek`: https://github.com/d33tah
.. _`Rodrigo Ramírez Norambuena`: https://github.com/roramirez
.. _`Anthony Lai`: https://github.com/ajlai
.. _`Ari Summer`: Ari Summer
.. _`David Szotten`: David Szotten
.. _`Fernando L. Canizo`: Fernando L. Canizo
.. _`Tim Sanders`: https://github.com/Gollum999
.. _`Irina Truong`: https://github.com/j-bennet
.. _`James Munson`: https://github.com/jmunson
.. _`Jonathan Slenders`: https://github.com/jonathanslenders
.. _`Fernando Mora`: https://github.com/fernandomora
.. _`Stuart Quin`: https://github.com/stuartquin
.. _`Timothy Cleaver`: Timothy Cleaver
.. _`gtxx`: gtxx
.. _`Joakim Koljonen`: https://github.com/koljonen
.. _`Anže Pečar`: https://github.com/Smotko
.. _`Catherine Devlin`: https://github.com/catherinedevlin
