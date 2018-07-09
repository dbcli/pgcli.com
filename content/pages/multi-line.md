Title: Multi-line Mode
Slug: multi-line
status: hidden

The default behavior of `pgcli` is to execute a query as soon as the enter key
is pressed. This might come as a surprise to seasoned `psql` users who always
enter a semi-colon to denote the end of the query. 

To emulate the original `psql` behavior you can enable the multi-line mode which
will require a semi-colon to be present at the end of the line. This enables
writing multi-line queries if they are really long. You can enable multi-line
mode by pressing `<F3>` key or set it permanently via the
[config]({filename}/pages/config.md) file. 
