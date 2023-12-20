# app/routes/authentication.py
from flask import Blueprint, request, jsonify

auth_bp = Blueprint('authentication', __name__)

# Mock user data for demonstration purposes
user_data = {
    '123': {'security_question': 'What is your favorite color?', 'answer': 'blue', 'password': ''}
    # Add more user data as needed
}

@auth_bp.route('/enter_roll_number', methods=['POST'])
def enter_roll_number():
    data = request.get_json()
    roll_number = data.get('roll_number')

    if roll_number in user_data:
        # Return the security question associated with the roll number
        security_question = user_data[roll_number]['security_question']
        print("jbhvbhuvhjbhjbjh")
        return jsonify(security_question=security_question), 200
    else:
        return jsonify(message='Invalid roll number'), 401


@auth_bp.route('/answer_security_question_and_set_password', methods=['POST'])
def answer_security_question_and_set_password():
    data = request.get_json()
    roll_number = data.get('roll_number')
    answer = data.get('answer')
    password = data.get('password')

    if roll_number in user_data and user_data[roll_number]['answer'].lower() == answer.lower():
        # Answer is correct, set the user's password
        user_data[roll_number]['password'] = password
        return jsonify(message='Authentication successful. Password set.'), 200
    else:
        return jsonify(message='Authentication failed. Invalid answer or roll number.'), 401
