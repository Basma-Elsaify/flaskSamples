from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def landing_page():
    return "<p>Landing Page!</p>"

# Endpoint to receive a message
@app.route('/api/message', methods=['POST'])
def receive_message():
    # Get the JSON data from the request
    data = request.json

    # Extract message, session_id, and auth from the JSON data
    message = data.get('message')
    session_id = data.get('session_id')
    auth = data.get('auth')

    # Check if all required data is provided
    if not message or not session_id or not auth:
        return jsonify({'error': 'Missing required parameters'}), 400

    # You can add your authentication logic here
    # For now, we will just check if the auth token is correct
    if auth != 'your_secret_auth_token':  # Replace with your actual authentication logic
        return jsonify({'error': 'Invalid authentication token'}), 403

    # Return the received message
    return jsonify({'session_id': session_id, 'message': message}), 200

if __name__ == '__main__':
    app.run(debug=True)


# use the following command to consume the application.
# curl -X POST http://127.0.0.1:5000/api/message -H "Content-Type: application/json" -d '{"message": "Hello, Flask!", "session_id": "12345", "auth": "your_secret_auth_token"}'

