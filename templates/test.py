from flask import Flask, send_file, abort, request
import os

app = Flask(__name__)

@app.route('/')
def serve_index():
    try:
        # Return index.html if the root URL is accessed
        return send_file('index.html')
    except Exception as e:
        # If any other error occurs, return a 500 error
        abort(500)

@app.route('/submit', methods=['POST'])
def submit():
    data1 = request.form.get('data1')
    data2 = request.form.get('data2')
    return send_file('index.html')


@app.route('/<path:filename>')
def serve_file(filename):
    try:
        # Check if the file exists
        if os.path.exists(filename):
            return send_file(filename)
        else:
            # If the file doesn't exist, return a 404 error
            abort(404)
    except Exception as e:
        # If any other error occurs, return a 500 error
        abort(500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
