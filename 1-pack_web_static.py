#!/usr/bin/python3
from fabric.api import task, local
from os.path import isdir
from datetime import datetime


@task
def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    try:

        date = datetime.now().strftime("%Y%m%d%H%M%S")

        if isdir("versions") is False:
            local("mkdir versions")

        filename = "versions/web_static_{}.tgz".format(date)

        output = local("tar -czvf {} web_static".format(filename), capture=True)
        return filename

    except:
        return None
