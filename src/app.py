from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

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
