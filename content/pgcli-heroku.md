Title: Integrating pgcli with heroku toolbelt
Date: 2015-05-06
Category: Blog
Tags: python, heroku
Slug: heroku-pgcli

Heroku is a popular PAAS provider that offers managed Postgres database. Heroku provides a convenience command to connect to the postgres database, which will launch `psql`. Now it is possible to launch `pgcli` instead of the default `psql` for heroku Postgres by installing the [heroku-pg-pgcli](https://github.com/chrisanderton/heroku-pg-pgcli) plugin for heroku tool belt.

### Installation

Make sure pgcli is installed. If it is not installed check the installation [instructions](http://pgcli.com/install). Typically it is:

Either:

```
    $ brew install pgcli    # Only on OS X
```

or 

```
    $ pip install pgcli   # Python package installation
```

Then install the heroku plugin

```
    $ heroku plugins:install git@github.com:chrisanderton/heroku-pg-pgcli.git
```

### Usage

Run this from within a Heroku app directory

```
    $ heroku pg:pgcli
```

That will launch pgcli with the appropriate database credentials, taken from heroku DATABASE_URL for that application.

That's it. 

### Credit

Thanks to [Chris Anderton](https://github.com/chrisanderton) for creating this heroku plugin. 
