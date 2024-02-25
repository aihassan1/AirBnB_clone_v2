#!/usr/bin/python3
from fabric.api import task, put, env, run
from os.path import isdir, islink
from os import unlink, symlink
from os.path import basename
from datetime import datetime

env.hosts = ["18.210.14.47", "54.157.179.130"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


@task
def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not archive_path:
        return False

    try:
        filename = basename(archive_path)
        filename = filename.replace(".tgz", "")
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run(f"mkdir -p {path}{filename}")
        run(f"tar -xvzf /tmp/{filename} -C {path}{filename}")
        run(f"mv /{path}{filename}/web_static/* {path}{filename}")
        run(f"rm /tmp/{filename}.tgz")

        run(f"rm -rf {path}{filename}/web_static")
        run(f"rm -rf /data/web_static/current")
        run("ln -s {path}{filename}/ /data/web_static/current ")

        return True

    except Exception as e:
        return False
