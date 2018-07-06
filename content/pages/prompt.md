Title: Prompt
Slug: prompt
status: hidden

Pgcli provides a configurable prompt. When pgcli starts up,
it will use the prompt configuration found in its
[config file]({filename}/pages/config.md). Once pgcli is running
up, you can change the prompt by using the
[`prompt` command]({filename}/pages/commands.md#prompt).

The default prompt looks something like this: `user@localhost:db_name> `.
It is formatted using the following character sequences.
The default format string is `\t \u@\h:\d> `.

* `\t` - Current date and time
* `\u` - Username
* `\h` - Hostname of the server
* `\d` - Database name
* `\p` - Database port
* `\i` - Postgres PID
* `\#` - "@" sign if logged in as superuser, '>' in other case
* `\n` - Newline
