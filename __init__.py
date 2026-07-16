
from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
# Initialize Talisman for security headers
Talisman(app)

from service import routes
