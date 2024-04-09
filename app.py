from flask import Flask, jsonify
import random

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({"status": 200, "message": "API do Leandro Maciel Giovani"})

@app.route('/aleatorio')
def aleatorios():
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@app.route('/argumentos/<string:nome>')
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

if __name__ == '__main__':
    app.run(debug=True)