#!/usr/bin/python3
# Fabric script that distributes an archive to your web servers

from fabric.api import *
from os.path import exists

env.hosts = ['107.23.90.193', '3.89.155.59']

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')
        # Uncompress the archive to the folder /data/web_static/releases/
        filename = archive_path.split('/')[-1]
        foldername = filename.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'.format(foldername))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(filename, foldername))
        # Delete the archive from the web server
        run('rm /tmp/{}'.format(filename))
        # Delete the symbolic link /data/web_static/current from the web server
        run('rm -rf /data/web_static/current')
        # Create a new the symbolic link /data/web_static/current on the web server
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(foldername))
        return True
    except:
        return False

