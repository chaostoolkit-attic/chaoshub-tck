#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import connexion
import logging

from connexion import NoContent


def put_experiment(organisation, workspace):
    journal = connexion.request.json
    print("Invoked put handler with Org:{org} and Workspace:{ws}".format(
        org=organisation, ws=workspace
    ))

    token = connexion.request.headers["CHAOSHUB-TOKEN"]
    print("Supplied user token was {token}".format(token=token))

    journal = connexion.request.json
    print("Supplied journal was {journal}".format(journal=journal))

    return NoContent, 200


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__, specification_dir='chaoshubtck/chaoshubserver/')
app.add_api('chaoshubserver.yaml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8080, server='gevent')
