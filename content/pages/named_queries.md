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
