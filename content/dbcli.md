Title: dbcli - a new github org 
Date: 2015-04-18
Category: Blog
Tags: python 
Slug: dbcli

I'm officially moving the [pgcli](https://github.com/dbcli/pgcli) project into
the [dbcli](https://github.com/dbcli) org in github.

## Why?

* pgcli is a community project now and having an organization helps solidify that.
* More peope will now have write access to the repo. Watch for the announcement of the core-devs of pgcli.
* It's a better home for similar projects in the future, such as mysql-cli, sqlite-cli etc.
* pgcli has a few subpackages that should be individual projects (sqlcompelter.py, pgspecial.py etc) so it can be repurposed in other projects. They will be broken out into separate repos and pulled into pgcli as dependencies in the future.

## How does it affect users?

* The changes to the code base will be peer reviewed by more than one person. Result: Improved stability, Less bugs.
* Quicker turn around on bug reports and feature requests, since more people will feel the ownership towards the project instead of that one guy.
