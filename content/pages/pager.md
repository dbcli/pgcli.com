Title: Pager
Slug: pager
status: hidden

Pgcli outputs query results in a pager (e.g. `less`, `more`). This
allows you to easily view large result sets one page at a time.

## Configuring the Pager

When starting up, pgcli checks the `pager` config option in the [config
file]({filename}/pages/config.md). If it's set, then pgcli uses its value as
the pager. If it is commented out, then pgcli will use the `PAGER` environment
variable's value.

Once pgcli is started, you can use the `\pager` command to change which pager
pgcli uses. 

```
> \pager less
PAGER set to less.
```

## Pager Behavior

On macOS and Linux, the pager will default to `less` for most users. `less`
sometimes has less-than-desirable behavior like clearing the screen, cutting
lines off, etc. You can configure `less` through environment variables in your
shell configuration files. Here are some common `less` options and
configuration examples:

- `-X` leaves file contents on the screen when less exits.
- `-F` makes `less` quit if the entire output can be displayed on one
  screen.
- `-R` displays ANSI color escape sequences in "raw" form.
- `-S` disables line wrapping. Side-scroll to see long lines.

```
# This is a popular option among pgcli users.
export LESS="-XFR"

# Some pgcli users like to disable line wrapping.
export LESS="-SRXF"
```

If the `LESS` environment variable is not set, and `less` is the pager, then
the `LESS` environment variable will automatically be set to `-SRXF`.
