#!/usr/bin/python3
"""
Pack static content and deploy on servers
"""

import time
from fabric.api import local, run, put, env

env.hosts = ['100.26.227.175', '54.166.43.77']


def do_pack():
    """Pack the web_static content"""
    try:
        current_time = time.strftime("%Y%m%d%H%M%S", time.gmtime())
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """Deploy the archive to the web servers"""
    if not archive_path:
        return False

    try:
        put(archive_path, '/tmp/')

        run('mkdir -p /data/web_static/releases/{}/'
            .format(archive_path[9:-4]))

        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive_path[9:], archive_path[9:-4]))

        run('rm /tmp/{}'.format(archive_path[9:]))

        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'
            .format(archive_path[9:-4], archive_path[9:-4]))

        run('rm -rf /data/web_static/releases/{}/web_static/'
            .format(archive_path[9:-4]))

        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_path[9:-4]))

        return True
    except Exception as e:
        print("Error:", e)
        return False


path = do_pack()


def deploy():
    """Pack and deploy"""

    return do_deploy(path) if path else False


if __name__ == "__main__":
    deploy()
