#!/usr/bin/python3
from fabric.api import put, run, env
from os.path import isfile, basename

"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ["18.210.14.47", "54.157.179.130"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if isfile(archive_path) is False:
        return False

    filename = basename(archive_path)
    filename = filename.replace(".tgz", "")

    try:
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")

        run(f"mkdir -p {path}{filename}")
        run(f"tar -xvzf /tmp/{filename}.tgz -C {path}{filename}")

        run(f"mv {path}{filename}/web_static/* {path}{filename}")

        run(f"rm /tmp/{filename}.tgz")

        run(f"rm -rf {path}{filename}/web_static")

        run("rm -rf /data/web_static/current")

        run(f"ln -s {path}{filename}/ /data/web_static/current ")

        return True

    except Exception as e:
        return False
