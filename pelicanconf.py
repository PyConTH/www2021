#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tech WG'
AUTHORS = {"Tech WG": {
        "url": "https://th.pycon.org/",
        "blurb": "Website author.",
        "avatar": "",
    },}
SITENAME = 'PyCon APAC 2021'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Bangkok'

DEFAULT_LANG = 'en'

LANGUAGE_CODES = {
        'en': 'English',
        'th': 'ไทย',
        }

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),
        )

# Social widget
SOCIAL = (('email', 'contact@pyconthailand.org'),
          ('facebook', 'https://www.facebook.com/Pyconthailand'),
          ('twitter', 'https://twitter.com/pyconthailand'),
          ('instagram','https://www.instagram.com/pyconthailand/'),
          ('youtube','https://www.youtube.com/pyconthailand'),
         )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
