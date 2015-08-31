Release v0.19.2
###############

:date: 2015-08-30
:tags: python, release, changelog, postgres
:category: Blog
:slug: v0.19.2

Features:
---------

* Autocompletion for database name in \c and \connect. (Thanks: `Darik Gamble`_).
* Improved multiline query support by correctly handling open quotes. (Thanks: `Darik Gamble`_).
* Added \pager command.
* Enhanced \i to run multiple queries and display the results for each of them
* Added keywords to suggestions after WHERE clause.
* Enabled autocompletion in named queries. (Thanks: `Iryna Cherniavska`_).
* Path to .pgclirc can be specified in command line. (Thanks: `Iryna Cherniavska`_).
* Added support for pg_service_conf file. (Thanks: `Iryna Cherniavska`_).
* Added custom styles. (Contributor: `Darik Gamble`_).

Internal Changes:
-----------------

* More completer test cases. (Thanks: `Darik Gamble`_).
* Updated sqlparse version from 0.1.14 to 0.1.16. (Thanks: `Darik Gamble`_).
* Upgraded to prompt_toolkit 0.46. (Thanks: `Jonathan Slenders`_).

BugFixes:
---------
* Fixed the completer crashing on invalid SQL. (Thanks: `Darik Gamble`_).
* Fixed unicode issues, updated tests and fixed broken tests.

.. _`Darik Gamble`: https://github.com/darikg
.. _`Jonathan Slenders`: https://github.com/jonathanslenders
.. _`Iryna Cherniavska`: https://github.com/j-bennet
