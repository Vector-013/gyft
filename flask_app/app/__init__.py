from flask import Flask
from .extensions import sslify, jwt

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

# Import and initialize extensions
from .extensions import sslify, jwt
sslify.init_app(app)
jwt.init_app(app)

# Import and register routes
from .routes import authentication, api
app.register_blueprint(authentication.bp)
app.register_blueprint(api.bp)