#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andy Goldschmidt'
SITENAME = u'Football, Is Sex Baby!'
SITESUBTITLE = u'Advanced Statistics... auf deutsch!'
SITEURL = ''

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/footballissex'),
          ('Facebook', 'https://www.facebook.com/FootballIsSexBaby'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# My custom settings
ARTICLE_URL = u'{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = u'{date:%Y}/{date:%m}/{slug}.html'

PLUGIN_PATH = 'plugins'

THEME = 'themes/tuxlite_tbs'
STATIC_PATHS = ["images", ]

TWITTER_USERNAME = 'footballissex'
