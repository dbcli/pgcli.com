#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Amjith'
SITENAME = u'pgcli'
SITEURL = 'http://pgcli.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag.%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
         #('Python.org', 'http://python.org/'),
         #('Jinja2', 'http://jinja.pocoo.org/'),
         #('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/amjithr'),
          ('github', 'http://github.com/amjith/pgcli'),
         )

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

DIRECT_TEMPLATES = {}

STATIC_PATHS = {'images', 'extra/CNAME'}
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

THEME = 'theme/notmyidea'

GOOGLE_ANALYTICS = 'UA-58061452-1'
