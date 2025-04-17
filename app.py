from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-quote')
def get_quote():
    try:
        with open('quotes.txt', 'r') as f:
            quotes = f.readlines()
        quote = random.choice(quotes).strip()
        return jsonify({'quote': quote})
    except FileNotFoundError:
        return jsonify({'quote': "No quotes found."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

