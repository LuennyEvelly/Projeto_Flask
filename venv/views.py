from flask import render_template, request, redirect, session, flash, url_for
from models import Carro
from venv.carro import app, db
from dao import CarroDao, UsuarioDao

carro_dao = CarroDao(db)
usuario_dao = UsuarioDao(db)

@app.route('/')
def index():
    return render_template('lista.html',titulo='carro', carros=carro_dao.listar())

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Carro')

@app.route('/criar', methods=['POST',])
def criar():
    id = request.form['id']
    marca = request.form['marca']
    modelo = request.form['modelo']
    cor = request.form['cor']
    combustivel = request.form['combustivel']
    ano = request.form['ano']
    carro = Carro(marca, modelo, cor, combustivel, ano)
    carro = carro_dao.salvar(carro)
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))
    carro = carro_dao.busca_por_id(id)
    return render_template('editar.html', titulo='Editando Carro', carro=carro)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    id = request.form['id']
    marca = request.form['marca']
    modelo = request.form['modelo']
    cor = request.form['cor']
    combustivel = request.form['combustivel']
    ano = request.form['ano']
    carro = Carro(marca, modelo, cor, combustivel, ano, id)
    carro_dao.salvar(carro)
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('deletar', id=id)))
    carro_dao.deletar(id)
    flash("O carro foi removido com sucesso!")
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo='login', proxima=proxima)


@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = usuario_dao.autenticar(request.form['usuario'], request.form['senha'])
    if usuario:
        session['usuario_logado'] = usuario.id
        flash(usuario.nome + 'Logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect((proxima_pagina))
    else:
        flash('Usuário ou senha inválida, tente novamente!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))

@app.route('/carro/<int:id>')
def carro(id):
    carro = carro_dao.busca_por_id(id)
    return render_template('carros.html', titulo='Carro', carro=carro)