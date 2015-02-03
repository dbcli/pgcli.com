Title: Embedding pgcli in IPython
Date: 2015-2-3
Category: Blog
Tags: ipython, python, postgres
Status: draft


[IPython](http://ipython.org/) is an interactive shell for Python that is
well-suited to do data-analysis. It has integration for plotting, data-analysis
libraries, parallel computing etc. 

[IPython-sql](https://github.com/catherinedevlin/ipython-sql) is a python
package that provides an easy way to load data from a database into the ipython
environment to do the data-analysis. Here's an example. 

```
In [1]: %load_ext sql

In [2]: %sql postgres://localhost:5432/misago_testforum
Out[2]: u'Connected: None@misago_testforum'

In [3]: %sql select * FROM django_migrations where id = 5
1 rows affected.
Out[3]: [(5, u'admin', u'0001_initial', datetime.datetime(2014, 11, 24, 14, 26, 43, 625938, 
          tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=-480, name=None)))]
```

We can now manipulate the data that was imported from the database. 

The trouble is ipython doesn't have the ability to do auto-completion for the
sql statements. So it's a bit hard to iterate on the sql statement to get the
right data.

Thanks to [Darik Gamble](https://github.com/darikg) we can now embed pgcli
directly inside the ipython console. We can iterate over the sql statements in
pgcli with the comfort of auto-completion and preview the results before
loading it into IPython. When we're satisfied with the results all we do is
quit pgcli, and we'll drop back to IPython loaded with the results from the
last query.

Let's see how that works. 

```
# IPython Console

In [1]: %load_ext pgcli.main
The pgcli.main module is not an IPython extension.

In [2]: %load_ext pgcli.magic

In [3]: %pgcli postgres://localhost:5432/misago_testforum
Connected: None@misago_testforum

# pgcli repl

misago_testforum> SELECT * FROM django_migrations WHERE id = 5
+------+-------+--------------+----------------------------------+
|   id | app   | name         | applied                          |
|------+-------+--------------+----------------------------------|
|    5 | admin | 0001_initial | 2014-11-24 14:26:43.625938-08:00 |
+------+-------+--------------+----------------------------------+
SELECT 1
misago_testforum>
GoodBye!
1 rows affected.

# Back on IPython Console. 

Out[3]: [(5, u'admin', u'0001_initial', datetime.datetime(2014, 11, 24, 14, 26, 43, 625938, 
          tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=-480, name=None)))]

In [4]: _
Out[4]: [(5, u'admin', u'0001_initial', datetime.datetime(2014, 11, 24, 14, 26, 43, 625938, 
          tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=-480, name=None)))]
```

That's it. So if you're using IPython for data-analysis and have your data
residing in a Database, you can easily import it in using ipython-sql and
pgcli.

### Installation 

Install pgcli and ipython-sql and you're all set to go. 

```
$ pip install pgcli ipython ipython-sql

```

If you have feedback, please reach out via
[twitter](https://twitter.com/amjithr) or
[github](https://github.com/amjith/pgcli/issues). Thank you!
