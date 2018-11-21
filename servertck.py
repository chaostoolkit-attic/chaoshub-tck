# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import logging
from typing import Any, Dict, List, Union
import uuid

import connexion
from connexion import NoContent
from flask import redirect
from swagger_ui_bundle import swagger_ui_3_path


###############################################################################
# Access Tokens
###############################################################################
def create_token():
    pass


def get_token():
    pass


def get_tokens():
    pass


def list_tokens():
    pass


def delete_token():
    pass

###############################################################################
# Organizations
###############################################################################
def create_org():
    pass


def get_org():
    pass


def get_orgs():
    pass


def list_orgs():
    pass


def delete_org():
    pass


def get_org_workspaces():
    pass


def link_workspace_to_org():
    pass


def unlink_workspace_from_org():
    pass


###############################################################################
# Workspaces
###############################################################################
def create_workspace():
    pass


def get_workspace():
    pass


def get_workspace_experiments():
    pass


def get_workspaces():
    pass


def list_workspaces():
    pass


def delete_workspace():
    pass


###############################################################################
# Experiments
###############################################################################
def upload_experiment():
    pass


def get_experiment():
    pass


def delete_experiment():
    pass


def get_experiment_executions():
    pass


def get_experiment_policy():
    pass


def set_experiment_policy():
    pass


def get_experiment_schedulings():
    pass


###############################################################################
# Executions
###############################################################################
def upload_execution():
    pass


def get_execution():
    pass


def get_execution_journal():
    pass


def get_execution_report():
    pass


def delete_execution():
    pass


###############################################################################
# Scheduling
###############################################################################
def create_scheduling():
    pass


def get_scheduling():
    pass


def get_schedulings():
    pass


def delete_scheduling():
    pass


def get_scheduling_status():
    pass


def set_scheduling_status():
    pass


def get_scheduling_executions():
    pass


def get_scheduling_status_history():
    pass



###############################################################################
# Policy
###############################################################################
def create_policy():
    pass


def get_policy():
    pass


def get_policies():
    pass


def delete_policy():
    pass


def run():
    options = {'swagger_path': swagger_ui_3_path}

    logging.basicConfig(level=logging.DEBUG)
    app = connexion.App(
        __name__, specification_dir='chaoshubtck/chaoshubserver/',
        options=options)
    app.add_api('chaoshubserver.yaml')
    app.run(port=8081, server='tornado')


if __name__ == '__main__':
    run()
