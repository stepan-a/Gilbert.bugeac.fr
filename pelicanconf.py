#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Geneviève Loupias'
SITENAME = u'Gilbert Bugeac'
SITEURL = 'https://gilbert.bugeac.fr'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (('Hommage à Tulle, 18 avril 2015', 'hommage-tulle-le-18-avril-2015.html'),
             ('Contact', 'contact.html') )

THEME = "theme"

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images']

BANNER = 'images/bugeac.png'
BANNER_ALL_PAGES = True

HIDE_SIDEBAR = True

BOOTSTRAP_THEME = 'readable'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
