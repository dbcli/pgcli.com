Title: History and Search
Slug: history
status: hidden

Pgcli keeps track of the queries entered in the repl. You can navigate the history
using `Up/Down` arrow keys or `Ctrl-p/Ctrl-n` (useful when navigating a multiline command).

Pgcli will automatically suggest commands from the history that match the starting characters
of the command you've typed so far. In order to accept that suggestion, you can press the `Right Arrow` key. 

Pressing `Ctrl-r` will enable incremental history search. So press `Ctrl-r` and then
start typing your search term to see the queries narrowed down. You can cycle
through the matches by pressing `Ctrl-r` again.
