
from flask import Blueprint, render_template

# Declare the Blueprint
homepage = Blueprint('homepage', __name__, template_folder='templates')

# Default route
@homepage.route('/')
def index():
    return render_template('homepage.html')

# About route
@homepage.route('/about')
def about():
    return render_template('about.html')

