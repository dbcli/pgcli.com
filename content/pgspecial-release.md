Title: Pgspecial is now an independent module
Date: 2015-09-22
Category: Blog
Tags: python, pgspecial
Slug: pgspecial-release
Author: Iryna Cherniavska

The pgspecial package is now independent and has its own place on PyPI:
 
# [pgspecial](https://pypi.python.org/pypi/pgspecial)

The package provides an API for developers who wish to run meta-commands on
PostgreSQL database without invoking the command line or rolling out their own
custom solution. It is easily extendable.

Here is an example of installing it and using it in in python REPL:

```
$ pip install pgspecial
$ python
Python 2.7.3 (default, Jun 22 2015, 19:33:41) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
```

After you see the prompt:

```
>>> import psycopg2
>>> from pgspecial.main import PGSpecial
>>> p = PGSpecial()
>>> conn = psycopg2.connect(user='postgres', host='localhost', database='geo')
>>> cur = conn.cursor()
>>> for title, rows, headers, status in p.execute(cur, '\\d city'):
...     print title
...     print headers
...     for row in rows:
...         print row
...     print status
...     
... 

['Column', 'Type', 'Modifiers']
['zip_code', 'character varying(5)', ' not null']
['name', 'character varying(28)', ' not null']
['abbreviation', 'character varying(13)', '']
Indexes:
    "city_pkey" PRIMARY KEY, btree (zip_code, name)
```

To learn more about the package or to contribute, follow the
[github](https://github.com/dbcli/pgspecial) link.
