from flask import Flask, render_template, request, redirect, url_for

from aluno import Aluno

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

        Aluno(nome = nome, cpf = cpf, telefone = telefone, email=email)

        # redirecionando o cliente para a rota do listar_alunos
        return redirect(url_for('listar_alunos'))

    return render_template("cadastro_aluno.html")


@app.route("/listar/alunos")
def listar_alunos():

    alunos = Aluno.listar()

    return render_template("listar_alunos.html", alunos=alunos)


@app.route("/editar/aluno/<matricula>", methods=('GET', 'POST'))
def editar_aluno(matricula):

    aluno = Aluno.listaAlunoMatricula(matricula = matricula)

    if request.method == 'POST':

        nome = request.form['nome_aluno']

        cpf = request.form['cpf_aluno']

        telefone = request.form['telefone_aluno']

        email = request.form['email_aluno']

        Aluno.atualizar(matricula = matricula, nome = nome, cpf = cpf, telefone = telefone, email=email)

        # redirecionando o cliente para a rota do listar_alunos
        return redirect(url_for('listar_alunos'))

    return render_template("editar_aluno.html", aluno=aluno)
