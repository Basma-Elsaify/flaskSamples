# flaskSamples
Flask API samples
## Prerequisites
You need to install flask, request and jsonify
```bash
pip install flask
```
run the app.py file with the following command,
```bash
flask --app app run
```
Consume the API from the terminal using the following command,
```bash
curl -X POST http://127.0.0.1:5000/api/message -H "Content-Type: application/json" -d '{"message": "Hello, Flask!", "session_id": "12345", "auth": "your_secret_auth_token"}'
```
