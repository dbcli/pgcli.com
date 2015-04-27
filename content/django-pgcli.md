Title: Django Integration of pgcli
Date: 2015-04-25
Category: Blog
Tags: python, django
Slug: django-pgcli

Django web framework has a rich set of management commands. One of them is `python manage.py dbshell`. This will launch the default database repl and connect to the appropriate database for the web application.

Now it is possible to launch `pgcli` instead of the default `psql` for Postgres by installing the [django-pgcli](https://github.com/ashchristopher/django-pgcli) python package.

### Installation

Install it using `pip`:

```
    $ pip install django-pgcli
```

Then add `django_pgcli` to the list of INSTALLED_APPS in your project's settings.py.

```
    INSTALLED_APPS = [
        ...,
        'django_pgcli',
    ]
```

### Usage

Launch the `dbshell` through the management command. 

```
    $ python manage.py dbshell
```

That will launch pgcli with the appropriate database credentials. 

That's it. 

### Credit

My personal thanks to [Ash Christopher](https://github.com/ashchristopher/) for taking the initiative to create this package. It was a well requested feature of pgcli, you just made a lot of people happy. 
