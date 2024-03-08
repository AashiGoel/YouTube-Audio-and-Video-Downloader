# app.py
from flask import Flask, render_template, request, jsonify
from process_data import process_input

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        user_input = request.form['user_input']
        processed_output = process_input(user_input)
        return jsonify(processed_output)

if __name__ == '__main__':
    app.run(debug=True)
