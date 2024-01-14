#!/usr/bin/env python3
"""
Fabric deployment script
"""

import os
import time
from fabric.api import env, local, run, put, cd

# Define the remote hosts
env.hosts = ['100.26.227.175', '54.166.43.77']


def do_pack():
    """Create a compressed archive of the web_static folder"""
    timestr = time.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestr)
    local("mkdir -p versions")
    local("tar -cvzf {} web_static/".format(archive_path))
    return archive_path

def do_deploy(archive_path):
    """Deploy the compressed archive to the server"""
    if not os.path.isfile(archive_path):
        return False

    try:
        # Extract information from the archive path
        archive_filename = os.path.basename(archive_path)
        archive_no_extension = os.path.splitext(archive_filename)[0]

        # Upload the compressed archive to the server
        put(archive_path, "/tmp/")

        # Create the necessary directories
        run("sudo mkdir -p /data/web_static/releases/{}".format(archive_no_extension))

        # Extract the contents of the archive
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_filename, archive_no_extension))

        # Remove the temporary archive
        run("sudo rm /tmp/{}".format(archive_filename))

        # Move the contents to the final location
        run("sudo mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(
            archive_no_extension, archive_no_extension))

        # Remove the now-empty web_static directory
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(archive_no_extension))

        # Update the symbolic link
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
            archive_no_extension))

        return True
    except Exception as e:
        print(e)
        return False

def deploy():
    """Pack and deploy the web application"""
    try:
        archive_path = do_pack()
        result = do_deploy(archive_path)
        return result
    except Exception as e:
        print(e)
        return False

def do_clean(number=0):
    """Clean up old releases"""
    try:
        with cd('./versions/'):
            local("ls -lv | rev | cut -f 1 | rev | head -n +{} | xargs -d '\n' rm -rf".format(number))

        with cd('/data/web_static/releases/'):
            run("sudo ls -lv | rev | cut -f 1 | rev | head -n +{} | xargs -d '\n' rm -rf".format(number))

        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    deploy()
