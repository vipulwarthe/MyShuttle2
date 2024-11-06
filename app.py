from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Example endpoint that returns a JSON response
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message": "Hello, this is a JSON response from Flask!",
        "status": "success"
    }
    return jsonify(data)

# Endpoint to receive POST requests
@app.route('/api/post', methods=['POST'])
def post_data():
    received_data = request.get_json()
    if received_data:
        response = {
            "message": "Data received successfully!",
            "data": received_data
        }
        return jsonify(response), 201
    else:
        return jsonify({"message": "No data provided!"}), 400

if __name__ == '__main__':
    # Run the app on port 5000, accessible to any IP (0.0.0.0)
    app.run(host='0.0.0.0', port=5000)
