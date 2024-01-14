#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *

env.hosts = ['100.26.227.175', '54.166.43.77']
env.user = "ubuntu"


def do_clean(number=0):
    """ CLEANS """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    with lcd('versions'):
        local(f'ls -t | tail -n +{number} | xargs rm -rf')

    path = '/data/web_static/releases'
    with cd(path):
        run(f'ls -t | tail -n +{number} | xargs rm -rf')

if __name__ == "__main__":
    do_clean()
