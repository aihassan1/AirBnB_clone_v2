#!/usr/bin/python3
from fabric.api import task, local, put, env
from os.path import isdir, basename

from datetime import datetime

env


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


@task
def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    extraction_path = "/data/web_static/releases/"
    destination = "/tmp/"
    env.hosts = ["ubuntu@18.210.14.47", "ubuntu@54.157.179.130"]
    env.key_filename = "~/.ssh/id_rsa"
    filename = basename(archive_path)
    print(filename)

    if not archive_path:
        return False
