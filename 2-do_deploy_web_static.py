#!/usr/bin/python3
from fabric.api import task, local, put, env, run
from os.path import isdir, islink
from os import unlink, symlink
from os.path import basename
from datetime import datetime

env.hosts = ["ubuntu@18.210.14.47", "ubuntu@54.157.179.130"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


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
    if not archive_path:
        return False

    try:
        filename = basename(archive_path)
        filename = filename.replace(".tgz", "")
        print(f"Deploying {filename}")

        for server in env.hosts:
            put(archive_path, "/tmp/", host=server)
            run(
                f"tar -xvzf /tmp/{filename} -C /data/web_static/releases/",
                capture=False,
            )
            run(f"rm /tmp/{filename}.tgz")

            if islink("/data/web_static/current"):
                unlink("/data/web_static/current")

            symlink("/data/web_static/current", f"/data/web_static/releases/{filename}")
        return True

    except Exception as e:
        return False
