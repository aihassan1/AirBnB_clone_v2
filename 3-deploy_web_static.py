#!/usr/bin/python3
"""Fabric script that creates and
distributes an archive to your web servers, using the function deploy:"""

from fabric.api import task, local, put, run, env
from os.path import isdir, isfile, basename
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


def deploy():
    """deploy to server"""
    tgz_file_path = do_pack()
    if tgz_file_path is False:
        return False
    else:
        return do_deploy(tgz_file_path)
