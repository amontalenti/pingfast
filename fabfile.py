import fabric
import fabric.colors
from fabric.api import *
from fabric.contrib.project import rsync_project
from settings import DEPLOY_SERVER, DEPLOY_USER, DEPLOY_DIR

blue = lambda s: fabric.colors.blue(s, True)
green = lambda s: fabric.colors.green(s, True)
yellow = lambda s: fabric.colors.yellow(s, True)
red = lambda s: fabric.colors.red(s, True)

configured_host = hosts("%s@%s" % (DEPLOY_USER, DEPLOY_SERVER))

@configured_host
@task
def push():
    puts(blue("Deploying..."))
    rsync_project(DEPLOY_DIR, exclude=[".git", "*.pyc"])
    puts(green("Done!"))

@configured_host
@task
def restart():
    sudo("supervisorctl restart pingfast")

