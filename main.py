from flask import Flask, render_template, request, redirect, url_for

import aluno

import sqlite3

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/cadastro/alunos", methods=('GET', 'POST'))
def cadastro_alunos():

    if request.method == 'POST':

        nome = request.form['nome_aluno']

        cpf = request.form['cpf_aluno']

        email = request.form['email_aluno']

        telefone = request.form['telefone_aluno']



        #redirecionando o cliente para a rota de servicos
        # return redirect(url_for('servicos'))

    return render_template("cadastro_aluno.html")