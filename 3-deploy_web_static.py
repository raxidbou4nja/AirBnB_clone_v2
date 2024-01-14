#!/usr/bin/python3
"""
    pack static content and deploy on server
"""
import time
from fabric.context_managers import cd
from fabric.api import local, get, put, reboot, run, sudo, env
import os.path

env.hosts = ['100.26.227.175', '54.166.43.77']


def do_pack():
    """ pack my static"""
    try:
        if not os.path.exists('versions'):
            l = local("mkdir -p versions")
        n = "versions/web_static_{}.tgz".\
            format(time.strftime("%Y%m%d%H%M%S", time.gmtime()))
        o = local("tar -cvzf {} web_static".format(n))
        # x = local("mv {} versions".format(n))
        # p = local("pwd {}".format(n))
        # return 'versions/{}'.format(n)
        return n
    except:
        return None


def do_deploy(archive_path):
    """ deploy my archive tgz into my servers """
    try:
        put(archive_path, '/tmp/')
        c1 = 'mkdir -p /data/web_static/releases/{}/'
        run(c1.format(archive_path[9:-4]))
        c2 = 'tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
        run(c2.format(archive_path[9:], archive_path[9:-4]))
        run('rm /tmp/{}'.format(archive_path[9:]))
        c3 = 'mv /data/web_static/releases/{}/web_static/* \
              /data/web_static/releases/{}/'
        run(c3.format(archive_path[9:-4], archive_path[9:-4]))
        c4 = 'rm -rf  /data/web_static/releases/{}/web_static/'
        run(c4.format(archive_path[9:-4]))
        run('rm -rf /data/web_static/current')
        c5 = 'ln -s /data/web_static/releases/{}/ {}'
        run(c5.format(archive_path[9:-4], '/data/web_static/current'))
        return True
    except:
        return False


path = do_pack()


def deploy():
    """ pack and deploy """
    if path:
        return do_deploy(path)
    else:
        return False
