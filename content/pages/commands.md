Title: Commands
Slug: commands
status: hidden

## Meta-commands (backslash commands)

Pgcli has implemented most of the meta-commands that are supported by `psql`. These meta-commands start with the backslash character. To see these, type `\?` at the prompt:

```
+--------------------------------------+------------------------------------------------+      
| Command                              | Description                                    |      
|--------------------------------------+------------------------------------------------|      
| \!                                   | Pass commands to shell.                        |
| \#                                   | Refresh auto-completions.                      |      
| \?                                   | Show Commands.                                 |      
| \T [format]                          | Change the table format used to output results |      
| \c[onnect] database_name             | Change to a new database.                      |      
| \conninfo                            | Get connection details                         |      
| \copy [tablename] to/from [filename] | Copy data between a file and a table.          |      
| \d[+] [pattern]                      | List or describe tables, views and sequences.  |      
| \dD[+] [pattern]                     | List or describe domains.                      |      
| \dE[+] [pattern]                     | List foreign tables.                           |
| \dF[+] [pattern]                     | List text search configurations.               |
| \dT[S+] [pattern]                    | List data types                                |      
| \db[+] [pattern]                     | List tablespaces.                              |      
| \ddp [pattern]                       | Lists default access privilege settings.       |
| \df[+] [pattern]                     | List functions.                                |      
| \di[+] [pattern]                     | List indexes.                                  |      
| \dm[+] [pattern]                     | List materialized views.                       |      
| \dn[+] [pattern]                     | List schemas.                                  |      
| \dp [pattern]                        | List privileges.                               |
| \ds[+] [pattern]                     | List sequences.                                |      
| \dt[+] [pattern]                     | List tables.                                   |      
| \du[+] [pattern]                     | List roles.                                    |      
| \dv[+] [pattern]                     | List views.                                    |      
| \dx[+] [pattern]                     | List extensions.                               |      
| \e [file]                            | Edit the query with external editor.           |      
| \echo [string]                       | Echo a string to stdout                        |
| \h                                   | Show SQL syntax and help.                      |      
| \i filename                          | Execute commands from file.                    |      
| \l[+] [pattern]                      | List databases.                                |      
| \n[+] [name] [param1 param2 ...]     | List or execute named queries.                 |      
| \log-file [filename]                 | Log all query results to a logfile, in         |
|                                      |   addition to the normal output destination.   |
| \nd [name]                           | Delete a named query.                          |      
| \np name_pattern                     | Print a named query.                           |
| \ns name query                       | Save a named query.                            |      
| \o [filename]                        | Send all query results to file.                |      
| \pager [command]                     | Set PAGER. Print the query results via PAGER.  |      
| \pset [key] [value]                  | A limited version of traditional \pset         |      
| \q                                   | Quit pgcli.                                    |      
| \qecho [string]                      | Echo a string to the query output channel.     |
| \refresh                             | Refresh auto-completions.                      |      
| \sf[+] FUNCNAME                      | Show a function's definition.                  |      
| \timing                              | Toggle timing of commands.                     |      
| \v [on|off]                          | Toggle verbose errors.                         |
| \watch [sec=2]                       | Execute query every `sec` seconds.             |
| \x                                   | Toggle expanded output.                        |      
| quit                                 | Quit pgcli.                                    |      
+--------------------------------------+------------------------------------------------+    
```

