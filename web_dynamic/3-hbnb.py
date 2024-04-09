#!/usr/bin/python3
"""
A Flask application that integrates with an AirBnB static HTML template.
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid

# Setting up Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

# Starting Flask page rendering
@app.teardown_appcontext
def close_storage(exception):
    """
    After each request, this function calls the .close() method (equivalent to .remove()) 
    on the current SQLAlchemy Session.
    """
    storage.close()

@app.route('/3-hbnb')
def render_hbnb_filters(the_id=None):
    """
    Handles requests to a custom template with states, cities, and amenities.
    """
    state_objects = storage.all('State').values()
    states = {state.name: state for state in state_objects}
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = {user.id: f"{user.first_name} {user.last_name}" for user in storage.all('User').values()}
    return render_template('3-hbnb.html',
                           cache_id=uuid.uuid4(),
                           states=states,
                           amenities=amenities,
                           places=places,
                           users=users)

if __name__ == "__main__":
    """
    Main Flask application.
    """
    app.run(host=host, port=port)