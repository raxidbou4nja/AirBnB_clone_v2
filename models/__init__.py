#!/usr/bin/python3
"""This module instantiates an object of the appropriate storage class"""

import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Determine the storage type based on the environment variable
storage_type = os.getenv('HBNB_TYPE_STORAGE')

# Create an instance of the appropriate storage class
if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

# Reload the storage instance
storage.reload()
