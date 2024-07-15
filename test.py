from flask import Flask, send_file, abort
import os

app = Flask(__name__)

@app.route('/lol/')
def serve_file(filename):
    # Print the application's root path
    print("App root path: " + app.root_path)
    
    # Determine and print the requested file path
    file_path = os.path.join(app.root_path, filename)
    print("Requested file path: " + file_path)
    
    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        abort(404)

@app.route('/')
def serve_file2(filename):
	send_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)

