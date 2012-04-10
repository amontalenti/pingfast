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

if __name__ == "__main__":
    manager.run()
