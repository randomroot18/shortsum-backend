from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/submit", methods=["POST"])
def submit():
    # Retrieve shared data
    title = request.form.get("title", "No title")
    text = request.form.get("text", "No text")
    url = request.form.get("url", "No URL")

    # Log the received data for testing
    print(f"Received submission - Title: {title}, Text: {text}, URL: {url}")

    # Respond to the client
    return jsonify({
        "status": "success",
        "message": "Data received successfully",
        "data": {
            "title": title,
            "text": text,
            "url": url
        }
    })# test

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)