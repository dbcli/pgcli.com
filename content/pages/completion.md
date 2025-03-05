Title: Auto-Completion
Slug: completion
status: hidden

# AutoCompletion

Auto-completion is on by default. The REPL will pop up a suggestion menu as soon as you start typing. The suggestions are context sensitive based on the position of the cursor. eg: Only tables are suggested after the FROM keyword, only column names are suggested after the WHERE clause.

## Smart Completion

Here are a few examples of smart completion.

### Table

Only table names from the current database are suggested after the FROM keyword.

<img src="images/docs/table.png" width=750 align="center"
     alt="Screenshot of pgcli auto-completion on table names in 'select * from ‸'">

### Column

Column names from the current table are suggested after the WHERE clause.

<img src="images/docs/column.png" width=750 align="center"
     alt="Screenshot of pgcli auto-completion on column names in 'select * from django_site where ‸'">

### Insert

Insert statement will suggest the column names.

<img src="images/docs/insert.png" width=750 align="center"
     alt="Screenshot of pgcli auto-completion in 'insert into django_site values (‸'">

### Alias

Aliases in the query are resolved and the columns from the table aliases are suggested.

<img src="images/docs/alias.png" width=750 align="center"
     alt="Screenshot of pgcli auto-completion on aliases tables in 'select * from django_site d join auth_group a on d.‸'">

## Fuzzy Match

The completions are matched using a [fuzzy algorithm](http://blog.amjith.com/fuzzyfinder-in-10-lines-of-python). For example typing 'djmi' will match the table 'django_migrations' because 'djmi' has parts of matching substrings. Here's an example:

<img src="images/docs/fuzzy.png" width=750 align="center"
     alt="Screenshot of pgcli auto-completion with fuzzy matching in 'select * from aup‸' that proposes 'auth_permission', 'auth_group', etc.">