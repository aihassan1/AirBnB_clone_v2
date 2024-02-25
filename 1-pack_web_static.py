#!/usr/bin/python3
from fabric.api import task, local
from os.path import isdir
from datetime import datetime


@task
def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        filename = f"versions/web_static_{date}.tgz"
        local(f"tar -czvf {filename} web_static", capture=True)
        return filename
    except Exception as e:
        return None
