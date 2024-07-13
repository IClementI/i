from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hello/<name>')
def hello_name(name):
    return f"Hello, {name}!"

@app.route('/sum/<int:a>/<int:b>')
def sum_two_numbers(a, b):
    return f"The sum of {a} and {b} is {a + b}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

