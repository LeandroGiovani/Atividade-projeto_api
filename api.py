from flask import Blueprint, jsonify, request
from funcoes import *
from random_data import *

bp = Blueprint("api", __name__)

@bp.route('/api/', methods=("GET"))
def index():
    return jsonify({"status": 200, "message": "API do Leandro Maciel Giovani"})

@bp.route('/api/aleatorio', methods=("GET"))
def aleatorio():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@bp.route('/api/argumentos/<string:nome>', methods=("GET"))
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

@bp.route('/api/maiores_de_50', methods=("GET"))
def A():
    return jsonify(f'Quantidade: {maior_de_50(pessoas)}')

@bp.route('/api/ganham_mais_de_2000', methods=("GET"))
def B():
    return jsonify(f'Ganham mais de 2000R$: {mais_2000(pessoas)[0]} pessoas, representando {mais_2000(pessoas)[1]}% de {mais_2000(pessoas)[2]} pessoas no total')

@bp.route('/api/3_maiores_salarios', methods=("GET"))
def C():
    return jsonify(f'{maior2(pessoas)}', methods=("GET"))

@bp.route('/api/media_salarial_profissoes', methods=("GET"))
def D():
    return jsonify(media_profissoes(pessoas))

@bp.route('/api/intervalo_idades2000', methods=("GET"))
def E():
    return jsonify(maior_2000_sexo(pessoas, sexo='Masculino'), maior_2000_sexo(pessoas, sexo='Feminino'))