from flask import Flask, render_template, request, url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from app.model.tables import Abc2dv
from app import app, db
import requests
import json

def via_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    r = requests.get(url)
    dic = r.json()
    return dic['logradouro']

@app.route("/")
def index():
    #selecionar todos - select * from
    alunos = Abc2dv.query.all()
    return render_template("index.html", alunos=alunos)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # crio um objeto aluno com os dados do formulario
        alunos = Abc2dv(request.form['nome_aluno'], request.form['email_aluno'], via_cep(request.form['cep']), request.form['numero'], request.form['cep'], request.form['complemento'])
        # adiciono o aluno (insert into)
        db.session.add(alunos)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("add.html")
    
@app.route("/edit/<int:ra>", methods=['GET', 'POST'])
def edit(ra):
    # select from
    alunos = Abc2dv.query.get(ra) 
    if request.method == 'POST':
        alunos.nome_aluno = request.form['nome_aluno']
        alunos.email_aluno = request.form['email_aluno']
        alunos.logradouro = via_cep(request.form['cep'])
        alunos.numero = request.form['numero']
        alunos.cep = request.form['cep']
        alunos.complemento = request.form['complemento']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("edit.html", alunos = alunos)   
 
@app.route("/delete/<int:ra>")
def delete(ra):
    cliente = Abc2dv.query.get(ra)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('index'))
