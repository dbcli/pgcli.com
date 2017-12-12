Title: Introducing mssql-cli - A query tool for SQL Server
Date: 2017-12-12
Category: Blog
Tags: python 
Slug: mssql-cli

We are excited to welcome `mssql-cli` to the [dbcli](https://github.com/dbcli)
org. This new command line query tool for Microsoft's SQL
Server is developed by Microsoft.

<img src='/images/mssql-cli.gif' width=750px align=center alt='mssql-cli'/>

Microsoft's engineers reached out to the dbcli team and pitched the idea of
writing a tool for SQL Server based on `pgcli` and `mycli`. The new tool named
`mssql-cli` will live in the `dbcli` org in github.

`mssql-cli` will ship with context-aware auto-completion, syntax highlighting,
alias support, paged output and so on. Essentially all the niceties of `pgcli`
that works with SQL Server.

Here's the [official announcement](https://blogs.technet.microsoft.com/dataplatforminsider/2017/12/12/try-mssql-cli-a-new-interactive-command-line-tool-for-sql-server/) from Microsoft.

# Backstory:

A couple of months ago, I received an email from a Microsoft PM asking me about
pgcli and dbcli org in github. I hopped on a skype call with the PM and a few
of the MS engineers. They seemed genuinely impressed by the feature set of
`pgcli` and `mycli`. I got to see a little demo of the prototype in action. 

I was flattered when asked if the tool could be part of the dbcli suite.
Microsoft created the tool and offered to maintain it, but it will be under the
dbcli org in github. 

Now the tool and the code are available for [public preview](https://github.com/dbcli/mssql-cli).
