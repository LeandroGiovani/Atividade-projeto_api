from flask import Flask, jsonify
from funcoes import *
from random_data import *
import random

# A - Pessoas maiores de 50 anos
# B - Pessoas que ganham mais de R$ 2000 e a porcentagem; que isso representa do todo;
# C - O nome, salário, idade e profissão das 3 pessoas com maiores salários
# D - A média salarial de cada profissão
# E - O  intervalo da maioria das idades e o sexo de quem ganha mais de R$ 2000. (M 39-50, F 29-30)
# --------------------------------------------------------
# Z - Sair

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": 200, "message": "API do Leandro Maciel Giovani"})

@app.route('/aleatorio')
def aleatorio():
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@app.route('/argumentos/<string:nome>')
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

@app.route('/maiores_de_50')
def A():
    return jsonify(f'Quantidade: {maior_de_50(pessoas)}')

@app.route('/ganham_mais_de_2000')
def B():
    return jsonify(f'Ganham mais de 2000R$: {mais_2000(pessoas)[0]} pessoas, representando {mais_2000(pessoas)[1]}% de {mais_2000(pessoas)[2]} pessoas no total')

@app.route('/3_maiores_salarios')
def C():
    return jsonify(f'{maior2(pessoas)}')

@app.route('/media_salarial_profissoes')
def D():
    return jsonify(media_profissoes(pessoas))

@app.route('/intervalo_idades2000')
def E():
    return jsonify(maior_2000_sexo(pessoas, sexo='Masculino'), maior_2000_sexo(pessoas, sexo='Feminino'))
if __name__ == '__main__':
    app.run(debug=True)