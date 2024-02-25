#!/usr/bin/python3
from fabric.api import task, local, put, env, run
from os.path import isdir, islink
from os import unlink, symlink
from os.path import basename
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
    if not archive_path:
        return False

    extraction_path = "/data/web_static/releases/"
    destination = "/tmp/"
    env.hosts = ["ubuntu@18.210.14.47", "ubuntu@54.157.179.130"]
    env.key_filename = "~/.ssh/id_rsa"

    old_sym_link = "/data/web_static/current"
    new_sym_link = "/data/web_static/current"

    try:
        filename = basename(archive_path)
        filename = filename.replace(".tgz", "")
        print(f"Deploying {filename}")


        for server in env.hosts:
            put(archive_path, destination, host=server, mirror_local_mode=True)
            run(f"tar -xvzf /tmp/{filename} -C /data/web_static/releases/")
            run(f"rm {destination}/{filename}.tgz")

            if islink(old_sym_link):
                unlink(old_sym_link)

            symlink("/data/web_static/current", f"/data/web_static/releases/{filename}")
        return True

    except Exception as e:
        return False
