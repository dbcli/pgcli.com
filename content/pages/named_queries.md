Title: Named Queries
Slug: named_queries.md
status: hidden

Named Queries are a way to save frequently used queries
with a short name.

`\n` - list all named queries.

`\n <name>` - Invoke a named query by its name.

`\ns <name> <query>` - Save a new named query called 'name'.

`\nd <name>` - Delete an existing named query by its name.

Examples:

```
    # Save a new named query.
    > \ns simple select * from abc where a is not Null;

    # List all named queries.
    > \n
    +--------+---------------------------------------+
    | Name   | Query                                 |
    |--------+---------------------------------------|
    | simple | SELECT * FROM abc where a is not NULL |
    +--------+---------------------------------------+

    # Run a named query.
    > \n simple
    +--------+--------+
    | a      | b      |
    |--------+--------|
    | 日本語 | 日本語   |
    +--------+--------+

    # Delete a named query.
    > \nd simple
    simple: Deleted
```

## Save location

Queries are saved in the `[named queries]` section of the 
[Config]({filename}/pages/config.md) file. You can also edit the config
file to manage the named queries.

An example of a query on a single line of the config file:

```yaml
[named queries]
simple = select * from abc where a is not Null
```

To create a named query that spans multiple lines do this:

```yaml
[named queries]
complex = """
    select
        *
    from
        abc
    where
        a is not Null
"""
```


## Positional Parameters

Named queries support shell-style parameter substitution. Save your named
query with parameters as placeholders (e.g. `$1`, `$2`,
`$3`, etc.):

```
\ns user_by_name select * from users where name = '$1'
```

When you call a named query with parameters, just add the parameters after
the query's name. You can put quotes around arguments that include spaces.

```
\n user_by_name "Skelly McDermott"
```

## Parameters Aggregation

Named queries also support parameters aggregation via two placeholders.
`$*` for raw aggregation and `$@` for string aggregation.
The former will use raw values of aggregated parameters, the later will quote
each aggregated value.

### Raw Aggregation
```
\ns users_by_age select * from users where id in ($*)
```

When you call a named query with parameters, just add any (at least one)
parameters after the query's name.

```
\n users_by_age 42 1337
```

### String Aggregation
```
\ns users_by_categories select * from users where category in ($@)
```

When you call a named query with parameters, just add any (at least one)
parameters after the query's name.
You can put quotes around arguments that include spaces.

```
\n users_by_categories "home user" "mobile user" superuser
```

## Combining Positional Parameters and Parameters Aggregation
It is possible to combine both positional parameters and parameters aggregation.
The positional parameters substitution takes place before the aggregation.
Which means positional parameters can be placed after parameters aggregation
in the query ; see example bellow.
Please note that the positional parameters will not be part of the aggregation taking place afterwards!

```
\ns users_by_categories_and_age select * from users where name in ($@) and age = $1
```

```
\n users_by_categories_and_age 42 "Skelly McDermott" "François Pignon"
```

The query after substitution would be:
```
select * from users where name in ('Skelly McDermott', 'François Pignon') and age = 42
```
