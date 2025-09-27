from flask import Blueprint, request, jsonify
from functools import wraps
import os

basic_auth = Blueprint('basic_auth', __name__)

USERNAME = os.getenv('BASIC_AUTH_USER', 'admin')
PASSWORD = os.getenv('BASIC_AUTH_PASS', 'password')

def require_basic_auth(f):
    """
    Basic authentication decorator
    ---
    tags:
      - Auth
    responses:
      401:
        description: Authentication required
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.username != USERNAME or auth.password != PASSWORD:
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated
