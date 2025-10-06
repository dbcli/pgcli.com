Title: Keybindings
Slug: keybindings
status: hidden

pgcli is built on top of [python-prompt-toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit), which provides default keybindings for both Emacs and Vi modes. These include standard text editing operations, cursor movement, and history navigation that are not enumerated here but follow the conventions of their respective editing modes.

Toggling between Emacs and Vi keybindings can be done via the config file (~/.config/pgcli/config) or toggled via the `F4` key.

Emacs mode is the default. In emacs mode you can press `Ctrl-a` to go to the beginning of a line and `Ctrl-e` to go to the end of a line and many more. 

When Vi mode is enabled you can use modal editing features offered by Vi in the REPL command line. For instance, press `Esc` key to go to normal mode and you can use `^` to go to the beginning and `$` to go to the end of a line. Pressing `i` will drop you into the insert mode.

## pgcli-specific Keybindings

The following keybindings are specific to pgcli:

| Key | Function |
|-----|----------|
| `F2` | Toggle Smart Completion Mode on/off |
| `F3` | Toggle Multi-line Mode on/off |
| `F4` | Toggle between Vi and Emacs editing modes |
| `F5` | Toggle Explain Mode on/off |
| `Tab` | Force autocompletion at cursor on non-empty lines |
| `Ctrl+space` | Initialize autocompletion at cursor, select the completion if menu is shown |
| `Alt+Enter` | Insert line break (Emacs mode only, when not in safe multi-line mode) |
| `Ctrl+p` | Move up in command history (when no text is selected) |
| `Ctrl+n` | Move down in command history (when no text is selected) |
