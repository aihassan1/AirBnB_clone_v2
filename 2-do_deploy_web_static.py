#!/usr/bin/python3
from fabric.api import put, env, run, local
from os.path import isdir, islink, isfile
from os import unlink, symlink
from os.path import basename
from datetime import datetime
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['142.44.167.228', '144.217.246.195']

def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if isfile(archive_path) is False:
        print("Archive file does not exist.")
        return False

    filename = basename(archive_path)
    filename = filename.replace(".tgz", "")
    print(f"Deploying {filename}")

    try:
        path = "/data/web_static/releases/"
        print(f"Creating directory {path}{filename}")
        put(archive_path, "/tmp/")
        print(f"Uploaded {archive_path} to /tmp/")

        run(f"mkdir -p {path}{filename}")
        print(f"Extracting archive to {path}{filename}")
        run(f"tar -xvzf /tmp/{filename} -C {path}{filename}")

        print(f"Moving files to {path}{filename}")
        run(f"mv /{path}{filename}/web_static/* {path}{filename}")

        print(f"Removing archive file /tmp/{filename}.tgz")
        run(f"rm /tmp/{filename}.tgz")

        print(f"Removing old web_static directory")
        run(f"rm -rf {path}{filename}/web_static")

        print("Removing old symbolic link")
        run("rm -rf /data/web_static/current")

        print("Creating new symbolic link")
        run(f"ln -s {path}{filename}/ /data/web_static/current ")

        print("Deployment completed successfully.")
        return True

    except Exception as e:
        print(f"Error during deployment: {e}")
        return False
