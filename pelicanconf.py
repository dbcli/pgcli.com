#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Amjith"
SITENAME = "pgcli"
SITEURL = 'https://www.pgcli.com'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TAG_FEED_ATOM = "feeds/tag.{slug}.atom.xml"
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"
TAG_FEED_RSS = "feeds/tag.{slug}.rss.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('mycli', 'http://mycli.net/'),
        )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/amjithr'),
          ('github', 'http://github.com/dbcli/pgcli'),
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

