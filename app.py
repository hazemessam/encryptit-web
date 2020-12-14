#!env/bin/python
from flask import Flask


app = Flask(
    __name__, 
    static_folder='public', 
    static_url_path='/public'
)

# Import all app routes
from routes import *

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)