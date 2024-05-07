from flask import Blueprint, jsonify, request
from funcoes import *
from random_data import *

bp = Blueprint("api", __name__)

@bp.route('/api', methods=("GET",))
def index():
    return jsonify({"status": 200, "message": "API do Leandro Maciel Giovani"})

@bp.route('/api/aleatorios', methods=("GET",))
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@bp.route('/api/argumentos/<string:nome>', methods=("GET",))
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

@bp.route('/api/idades', methods=("GET",))
def idades():
    return jsonify(f'Quantidade: {maior_de_50(pessoas)}')

@bp.route('/api/salarios', methods=("GET",))
def salarios():
    return jsonify(f'Ganham mais de 2000R$: {mais_2000(pessoas)[0]} pessoas, representando {mais_2000(pessoas)[1]}% de {mais_2000(pessoas)[2]} pessoas no total')

@bp.route('/api/maioressalarios', methods=("GET",))
def maioressalarios():
    return jsonify(f'{maior2(pessoas)}')

@bp.route('/api/profissoes', methods=("GET",))
def profissoes():
    return jsonify(media_profissoes(pessoas))

@bp.route('/api/intervalo', methods=("GET",))
def intervalo():
    return jsonify(maior_2000_sexo(pessoas, sexo='Masculino'), maior_2000_sexo(pessoas, sexo='Feminino'))