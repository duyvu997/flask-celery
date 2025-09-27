from flask import Flask
from flasgger import Swagger
from src.models import db
import os
from src.api.crawl_api import crawl_api
from src.api.auth import basic_auth

app = Flask(__name__)

# Example DB config from .env (adjust as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://{user}:{pw}@{host}:{port}/{db}'
    .format(
        user=os.getenv('DB_USER'),
        pw=os.getenv('DB_PASS'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        db=os.getenv('DB_NAME')
    )
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
swagger = Swagger(app)

# Register blueprints
app.register_blueprint(crawl_api)
app.register_blueprint(basic_auth)

@app.route('/')
def index():
    """Root endpoint
    ---
    responses:
      200:
        description: Welcome message
    """
    return {'message': 'Welcome to the Flask Celery Crawler API'}

if __name__ == '__main__':
    app.run(debug=True)
