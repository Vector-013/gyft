# app/routes/api.py
from flask import Blueprint, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/data', methods=['GET'])
def get_api_data():
    data = {'message': 'This is sample API data'}
    return jsonify(data), 200
