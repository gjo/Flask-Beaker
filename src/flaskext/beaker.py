# -*- coding: utf-8 -*-
"""
flaskext.beaker
~~~~~~~~~~~~~~~

Add Beaker support to Flask.

:copyright: (c) 2011 by OCHIAI, Gouji <gjo.ext@gmail.com>
:license: BSD
"""
from __future__ import absolute_import
from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
from beaker.middleware import SessionMiddleware
from flask import Flask
from types import MethodType

__all__ = ('Beaker',)


def _open_session(self, request):
    return request.environ['beaker.session']


def _save_session(self, session, response):
    pass


class Beaker(object):
    def __init__(self, app):
        self.app = app
        app.config.setdefault('BEAKER_CACHE_OPTIONS', {})
        app.config.setdefault('BEAKER_SESSION_OPTIONS', {})
        app.open_session = MethodType(_open_session, app, Flask)
        app.save_session = MethodType(_save_session, app, Flask)
        self.cache = CacheManager(
                **parse_cache_config_options(
                    self.app.config['BEAKER_CACHE_OPTIONS']))
        app.wsgi_app = SessionMiddleware(
            app.wsgi_app, app.config['BEAKER_SESSION_OPTIONS'])
        app.jinja_env.filters.update(
            cache=self.get_cache(),
            )

    def get_cache(self):
        return self.cache
