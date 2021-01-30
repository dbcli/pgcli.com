Title: Editor
Slug: editor
status: hidden

One of the most useful slash commands is `\e`. This will launch an editor to
edit the current query (or previous query, if the current query is blank).


Here are some examples:

```

# This will launch the default editor (read from $VISUAL or $EDITOR env variable, in that order).
# It will put the previous query in the editor's buffer.
> \e

# This will open the default editor with the current query in the buffer.
> SELECT * FROM \e

# This will open an existing file in the editor and the contents of the file
  will be populated into the prompt once the file is saved.
> \e <filename>

```
