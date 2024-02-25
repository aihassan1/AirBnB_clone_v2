#!/usr/bin/python3
from fabric.api import task, local


@task
def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""

    result = local("date +%Y%m%d%H%M%S", capture=True)
    formatted_time = result.strip()

    local("mkdir versions")
    output = local(f"tar -czvf versions/web_static_{formatted_time}.tgz web_static")
    if output.succeeded:
        return f"versions/web_static_{formatted_time}.tgz"
    else:
        return None
