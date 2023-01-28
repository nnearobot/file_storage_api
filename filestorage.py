from flask import Flask
import os

app = Flask(__name__)

# Limit uploaded file size, M
max_file_size = 50

# List of the allowe file extensions, i.g. {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
allowed_extensions = {}


app.config['MAX_CONTENT_LENGTH'] = max_file_size * 1024 * 1024
app.config['ALLOWED_EXTENSIONS'] = allowed_extensions

with app.app_context():
    from api.v1.routes import api as v1

app.register_blueprint(v1, url_prefix='/v1')
app.register_blueprint(v1, name="root", url_prefix='/') # the last stable version may be here


"""
When we will need some new features, which break v1 functionality, we can create
a new module, e.g. v2, and register its blueprint:

from api.v2 import api as api_v2
app.register_blueprint(api_v2, url_prefix='/v2')
"""

