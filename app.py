from flask import Flask, send_file, abort
import os

app = Flask(__name__)

@app.route('/<path:filename>')
def serve_file(filename):
    file_path = os.path.join(app.root_path, filename)
    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

