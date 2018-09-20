#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from typing import Any, Dict, Union

import connexion
from connexion import NoContent


def signup_local(user: Dict[str, str]) -> Union[object, int]:
    return NoContent, 201


def signin_local(user: Dict[str, str]) -> Union[object, int]:
    return NoContent, 201


def authorize_signin_with_oauth2(user: Dict[str, str]) -> Union[object, int]:
    return NoContent, 201


def authorize_signup_with_oauth2(user: Dict[str, str]) -> Union[object, int]:
    return NoContent, 201


def allowed_via_oauth2(user: Dict[str, str]) -> Union[object, int]:
    return NoContent, 201


def put_experiment(organisation, workspace):
    journal = connexion.request.json
    print("Invoked put handler with Org:{org} and Workspace:{ws}".format(
        org=organisation, ws=workspace
    ))

    bearer_token = connexion.request.headers["Authorization"]
    print("Supplied user bearer token was {token}".format(
        token=bearer_token))

    journal = connexion.request.json
    print("Supplied journal was {journal}".format(journal=journal))

    return NoContent, 200


def get_account_profile():
    pass


def post_account_profile():
    pass


def get_account_tokens():
    pass


def post_account_token():
    pass

def delete_account_token():
    pass

def get_account_orgs():
    pass


def post_account_org():
    pass


def get_account_workspaces():
    pass


def post_account_workspace():
    pass


def create_organization(name: str, email: str = "", url: str = "",
                        avatar_url: str = "") -> Union[Dict[str, Any], int]:
    return {}, 200
    


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__, specification_dir='chaoshubtck/chaoshubserver/')
app.add_api('chaoshubserver.yaml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8081, server='gevent')
