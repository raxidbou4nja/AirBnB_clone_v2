#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    compresses the contents of the web_static folder into a .tgz archive.
    returns the archive path if successful, otherwise, returns None.
    """
    try:
        # Create the 'versions' directory if it doesn't exist
        local("mkdir -p versions")

        # Generate the archive path
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)

        # Compress the web_static folder
        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path
    except Exception as e:
        return None


if __name__ == "__main__":
    do_pack()
