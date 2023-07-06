#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Create a .tgz archive from the contents of the web_static folder."""
    # Create the versions folder if it doesn't exist
    if not os.path.exists('versions'):
        os.makedirs('versions')

    # Generate the archive path
    now = datetime.now()
    archive_name = 'web_static_{}{}{}{}{}{}.tgz'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    archive_path = os.path.join('versions', archive_name)

    # Create the archive using tar and gzip
    try:
        local('tar -czvf {} web_static'.format(archive_path))
        return archive_path
    except Exception as e:
        print('An error occurred during archive creation:', e)
        return None
archive_path = do_pack()
if archive_path is not None:
    print('Archive created:', archive_path)
else:
    print('Failed to create archive.')

