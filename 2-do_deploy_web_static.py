#!/usr/bin/python3
"""
fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists, join

env.hosts = ['100.26.227.175', '54.166.43.77']

def do_deploy(archive_path):
    """Distributes an archive to the web servers."""
    if not exists(archive_path):
        return False

    try:
        archive_filename = archive_path.split("/")[-1]
        no_ext = archive_filename.split(".")[0]
        path = "/data/web_static/releases/"
        
        put(archive_path, '/tmp/')
        run('mkdir -p {}/{}'.format(join(path, no_ext), no_ext))
        run('tar -xzf /tmp/{} -C {}/{}'.format(archive_filename, join(path, no_ext), no_ext))
        run('rm /tmp/{}'.format(archive_filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {0}{1}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
