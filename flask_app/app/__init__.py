# app/__init__.py
from flask import Flask
from .routes import init_app
from flask_cors import CORS  # Import CORS

# Create a function to create the Flask app
def create_app():
    app = Flask(__name__)
    
    app.config['JWT_SECRET_KEY'] = 'oioi iuio yupp yuph'

    # Import and initialize extensions within the context of the app
    
    # Initialize CORS
    CORS(app)
    
    with app.app_context():
        from flask_sslify import SSLify
        from flask_jwt_extended import JWTManager

        sslify = SSLify()
        jwt = JWTManager()
        sslify.init_app(app)
        # init_sslify(app)
        jwt.init_app(app)
    
    app.app_context().push()
    # Call the init_app function to register route blueprints
    init_app(app)

    return app
