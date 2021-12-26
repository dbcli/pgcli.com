Title: SSH tunnel
Slug: ssh_tunnel
status: hidden

Sometimes a database you want to connect to is not directly accessible by your local machine.
For example only the SSH port might be open to external connections, or maybe the database is
in a private network and only a single machine can communicate with it.
For these cases you can ask Pgcli to create an SSH tunnel to that intermediate machine for you.

First scenario:
```
----------------------------------------------------------------------

                            |
-------------+              |     +----------+ my.server.com
    LOCAL    |              |     |  REMOTE  | :22 SSH
    CLIENT   | <== SSH Tunnel ==> |  SERVER  | :5432 Postgres instance
-------------+              |     +----------+
                            |
                         FIREWALL (only port 22 is open)

----------------------------------------------------------------------
```
In this scenario, to connect to the remote database you would do:
```bash
$ pgcli postgresql://user:password@localhost/mydatabase --ssh-tunnel myserver.com
```

Second scenario:
```
--------------------------------------------------------------------------------------------------


-------------+                    +----------+ my.server.com   +---------+ my.private.server.com
    LOCAL    |                    |  REMOTE  | :1022 SSH       | PRIVATE | :7777 Postgres instance
    CLIENT   | <== SSH Tunnel ==> |  SERVER  | <=============> | SERVER  |
-------------+                    +----------+                 +---------+
                                  my.server.com is the
                                  only server with access
                                  to my.private.server.com

--------------------------------------------------------------------------------------------------
```
In this scenario, to connect to the remote database you would do:
```bash
$ pgcli postgresql://user:password@my.private.server.com:7777/mydatabase \
    --ssh-tunnel john:mypass@myserver.com:1022
```

## Caveats
* [ProxyJump](https://man.openbsd.org/ssh_config#ProxyJump) directives are
[not supported yet](https://github.com/pahaz/sshtunnel/issues/244) by [sshtunnel](https://github.com/pahaz/sshtunnel)
which is the library we use to create SSH tunnels.
A workaround is to replace the `ProxyJump` directive by a `ProxyCommand` directive.
Example: `ProxyJump %r@bastion.server.com` becomes `ProxyCommand ssh %r@bastion.server.com -W %h:%p`.
* [Include](https://man.openbsd.org/ssh_config#Include) directives are
[not supported yet](https://github.com/paramiko/paramiko/pull/1892) by
[paramiko](https://github.com/paramiko/paramiko), the Python SSH implementation used by `sshtunnel`.
The workaround is to put everything in your main config file.
