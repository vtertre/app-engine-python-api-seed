# -*- coding: utf-8 -*-
__author__ = 'Vincent Tertre'

import os
import uuid

from flask import Flask, request, jsonify
from flask_restful import Api
from google.appengine.api import users


class Server(object):
    def __init__(self, application):
        flask = Flask(__name__)
        flask.config.from_object(ServerConfiguration)
        self._application = application
        self._web_server = Api(flask)
        self._admin_routes = []
        self.add_routes(self._application.routes())
        flask.before_request(check_privileges_for(self._admin_routes))

    def start(self, port):
        self.flask.run(port=port)

    def add_routes(self, routes):
        for route in routes:
            if route.requires_admin_privileges:
                self._admin_routes.append(route.resource.__name__.lower())
            self._web_server.add_resource(route.resource, route.uri)

    def __call__(self, environ, start_response):
        return self.flask.wsgi_app(environ, start_response)

    @property
    def flask(self):
        return self._web_server.app


class ServerConfiguration(object):
    DEBUG = os.environ.get(u'env', u'dev') == u'dev'
    SECRET_KEY = uuid.uuid4()


def check_privileges_for(admin_endpoints):
    def check_if_admin_role_is_required():
        if request.endpoint in admin_endpoints:
            if not users.is_current_user_admin():
                return jsonify({u'message': u'ACCESS_FORBIDDEN'}), 403
    return check_if_admin_role_is_required
