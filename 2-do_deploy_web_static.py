#!/usr/bin/python3
"""
Deploy static
"""

from fabric.api import put, run, env

env.hosts = ['100.26.227.175', '54.166.43.77']


def do_deploy(archive_path):
    """Deploy the archive to the web servers"""
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

        run('rm -rf  /data/web_static/releases/{}/web_static/'
            .format(archive_path[9:-4]))

        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_path[9:-4]))

        return True
    except Exception as e:
        print("Error:", e)
        return False
