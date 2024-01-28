#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """Display a HTML page with filters"""
    return render_template('10-hbnb_filters.html',
                            states=storage.all(State),
                            amenities=storage.all(Amenity))


@app.teardown_appcontext
def close_storage(exception):
    """Close the storage session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
