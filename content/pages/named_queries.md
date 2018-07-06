Title: Favorite Queries
Slug: favorites
status: hidden

Favorite Queries are a way to save frequently used queries
with a short name.

`\n` - list all favorite queries.

`\n <name>` - Invoke a favorite query by its name.

`\ns <name> <query>` - Save a new favorite query called 'name'.

`\nd <name>` - Delete an existing favorite query by its name.

Examples:

```
    # Save a new favorite query.
    > \ns simple select * from abc where a is not Null;

    # List all favorite queries.
    > \n
    +--------+---------------------------------------+
    | Name   | Query                                 |
    |--------+---------------------------------------|
    | simple | SELECT * FROM abc where a is not NULL |
    +--------+---------------------------------------+

    # Run a favorite query.
    > \n simple
    +--------+--------+
    | a      | b      |
    |--------+--------|
    | 日本語 | 日本語   |
    +--------+--------+

    # Delete a favorite query.
    > \nd simple
    simple: Deleted
```

## Positional Parameters

Favorite queries support shell-style parameter substitution. Save your favorite
query with parameters as placeholders (e.g. `$1`, `$2`,
`$3`, etc.):

```
\ns user_by_name select * from users where name = '$1'
```

When you call a favorite query with parameters, just add the parameters after
the query's name. You can put quotes around arguments that include spaces.

```
\n user_by_name "Skelly McDermott"
```
