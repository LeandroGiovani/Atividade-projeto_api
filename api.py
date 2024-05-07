from flask import Blueprint, jsonify, request
import random
from funcoes import *
from random_data import *

bp = Blueprint("api", __name__)

@bp.route('/api/')
def index():
    return jsonify({"status": 200, "message": "API do Leandro Maciel Giovani"})

@bp.route('/api/aleatorio')
def aleatorio():
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@bp.route('/api/argumentos/<string:nome>')
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

@bp.route('/api/maiores_de_50')
def A():
    return jsonify(f'Quantidade: {maior_de_50(pessoas)}')

@bp.route('/api/ganham_mais_de_2000')
def B():
    return jsonify(f'Ganham mais de 2000R$: {mais_2000(pessoas)[0]} pessoas, representando {mais_2000(pessoas)[1]}% de {mais_2000(pessoas)[2]} pessoas no total')

@bp.route('/api/3_maiores_salarios')
def C():
    return jsonify(f'{maior2(pessoas)}')

@bp.route('/api/media_salarial_profissoes')
def D():
    return jsonify(media_profissoes(pessoas))

@bp.route('/api/intervalo_idades2000')
def E():
    return jsonify(maior_2000_sexo(pessoas, sexo='Masculino'), maior_2000_sexo(pessoas, sexo='Feminino'))