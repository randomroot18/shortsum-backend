from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def handle_share_target():
    """
    Endpoint to handle the share target. It processes the POST request data.
    """
    # Extract the shared data from the request
    title = request.form.get('title', 'No title provided')
    text = request.form.get('text', 'No text provided')
    url = request.form.get('url', 'No URL provided')

    # Log or print the data for debugging
    print(f"Received data: Title={title}, Text={text}, URL={url}")

    # Respond back with acknowledgment
    return jsonify({
        "message": "Data received successfully",
        "data": {
            "title": title,
            "text": text,
            "url": url
        }
    }), 200

@app.route('/')
def index():
    """
    A simple index endpoint for testing.
    """
    return jsonify({"message": "Server is running!"})

# Run the application locally (this part is ignored when using Gunicorn or other WSGI servers)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)