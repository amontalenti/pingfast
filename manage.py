from __future__ import absolute_import
from flask.ext.script import Manager

from health import create_app

app = create_app()
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
