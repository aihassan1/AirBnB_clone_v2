#!/usr/bin/python3
from fabric.api import task, local
from os.path import isdir


@task
def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""

    result = local("date +%Y%m%d%H%M%S", capture=True)
    formatted_time = result.strip()

    if isdir("versions") is False:
        local("mkdir versions")

    filename = f"versions/web_static_{formatted_time}.tgz"

    output = local(f"tar -czvf {filename} web_static", capture=True)
    if output.succeeded:
        return filename
    else:
        return None
