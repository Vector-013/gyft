# run.py
from app import create_app

# Create the Flask app
app = create_app()

app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True)
