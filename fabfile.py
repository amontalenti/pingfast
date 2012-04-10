import fabric
import fabric.colors
from fabric.api import *
from settings import DEPLOY_HOST

blue = lambda s: fabric.colors.blue(s, True)
green = lambda s: fabric.colors.green(s, True)
yellow = lambda s: fabric.colors.yellow(s, True)
red = lambda s: fabric.colors.red(s, True)

@hosts(DEPLOY_HOST)
def push():
    puts(blue("Deploying..."))
    # ...
    puts(green("Done!"))
