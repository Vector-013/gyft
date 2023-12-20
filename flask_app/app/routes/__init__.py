# app/routes/__init__.py
from flask import Blueprint

# Import your route modules
from .authentication import auth_bp
from .api import api_bp

# Create a function to initialize all route blueprints
def init_app(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(api_bp, url_prefix='/api')

# Make sure to call the init_app function when the Flask app is created
