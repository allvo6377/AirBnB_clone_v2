#!/usr/bin/python3
'''Fabric script to generate .tgz archive'''
from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns the archive path if successful, otherwise returns None.
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate the archive path
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)
        archive_path = "versions/{}".format(archive_name)

        # Compress the web_static folder into the archive
        local("tar -czvf {} web_static".format(archive_path))

        # Return the archive path if successful
        return archive_path
    except Exception as e:
        print("An error occurred during archive generation: {}".format(e))
        return None

# Calling the do_pack function to generate the archive
archive_path = do_pack()
if archive_path:
    print("Archive generated: {}".format(archive_path))
else:
    print("Archive generation failed.")
