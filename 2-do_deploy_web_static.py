#!/usr/bin/python3
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ["18.210.14.47", "54.157.179.130"]


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False
    try:
        archived_file = archive_path.split("/")[-1]
        filename = archived_file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, filename))
        run("tar -xzf /tmp/{} -C {}{}/".format(archived_file, path, filename))
        run("rm /tmp/{}".format(archived_file))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, filename))
        run("rm -rf {}{}/web_static".format(path, filename))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, filename))
        return True
    except:
        return False
