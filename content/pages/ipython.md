Title: IPython integration
Slug: ipython
status: hidden

Pgcli can be run from within `IPython <https://ipython.org>`_ console. When working on a query,
it may be useful to drop into a pgcli session without leaving the IPython console, iterate on a
query, then quit pgcli to find the query results in your IPython workspace.

Assuming you have IPython installed:

::

    $ pip install ipython-sql

After that, run ipython and load the ``pgcli.magic`` extension:

::

    $ ipython

    In [1]: %load_ext pgcli.magic


Connect to a database and construct a query:

::

    In [2]: %pgcli postgres://someone@localhost:5432/world
    Connected: someone@world
    someone@localhost:world> select * from city c where countrycode = 'USA' and population > 1000000;
    +------+--------------+---------------+--------------+--------------+
    | id   | name         | countrycode   | district     | population   |
    |------+--------------+---------------+--------------+--------------|
    | 3793 | New York     | USA           | New York     | 8008278      |
    | 3794 | Los Angeles  | USA           | California   | 3694820      |
    | 3795 | Chicago      | USA           | Illinois     | 2896016      |
    | 3796 | Houston      | USA           | Texas        | 1953631      |
    | 3797 | Philadelphia | USA           | Pennsylvania | 1517550      |
    | 3798 | Phoenix      | USA           | Arizona      | 1321045      |
    | 3799 | San Diego    | USA           | California   | 1223400      |
    | 3800 | Dallas       | USA           | Texas        | 1188580      |
    | 3801 | San Antonio  | USA           | Texas        | 1144646      |
    +------+--------------+---------------+--------------+--------------+
    SELECT 9
    Time: 0.003s


Exit out of pgcli session with ``Ctrl + D`` and find the query results:

::

    someone@localhost:world>
    Goodbye!
    9 rows affected.
    Out[2]:
    [(3793, u'New York', u'USA', u'New York', 8008278),
     (3794, u'Los Angeles', u'USA', u'California', 3694820),
     (3795, u'Chicago', u'USA', u'Illinois', 2896016),
     (3796, u'Houston', u'USA', u'Texas', 1953631),
     (3797, u'Philadelphia', u'USA', u'Pennsylvania', 1517550),
     (3798, u'Phoenix', u'USA', u'Arizona', 1321045),
     (3799, u'San Diego', u'USA', u'California', 1223400),
     (3800, u'Dallas', u'USA', u'Texas', 1188580),
     (3801, u'San Antonio', u'USA', u'Texas', 1144646)]

The results are available in special local variable ``_``, and can be assigned to a variable of your
choice:

::

    In [3]: my_result = _
