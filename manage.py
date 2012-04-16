from __future__ import absolute_import
from flask.ext.script import Manager

from health import create_app

app = create_app()
manager = Manager(app)

@manager.command
def sync():
    """sync Pingdom accounts from primary -> secondary"""
    from pingdom_sync import sync_pingdom_accounts
    sync_pingdom_accounts()

@manager.command
def pause_secondary():
    """pause all checks on secondary account"""
    from pingdom_sync import pause_all, secondary_account_login
    pause_all(secondary_account_login())

@manager.command
def unpause_secondary():
    """unpause all checks on secondary account"""
    from pingdom_sync import unpause_all, secondary_account_login
    unpause_all(secondary_account_login())

if __name__ == "__main__":
    manager.run()
