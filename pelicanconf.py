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
LINKS = (('GFWTC', 'http://gfwtc.de'),
         ('Sideline Reporter', 'http://sidelinereporter.wordpress.com/'),
         ('Hard Count', 'http://hardcount.wordpress.com/'),
         ('Der andere Football Blog', 'http://deranderefootballblog.wordpress.com/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/footballissex'),
          ('Facebook', 'https://www.facebook.com/FootballIsSexBaby'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# My custom settings
ARTICLE_URL = u'{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = u'{date:%Y}/{date:%m}/{slug}.html'

PLUGIN_PATH = 'plugins'

THEME = 'themes/pelican-bootstrap3'
STATIC_PATHS = ["images", "themes/static"]
