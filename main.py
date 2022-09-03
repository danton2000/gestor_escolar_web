import sqlite3

from flask import Flask, render_template, request, redirect, url_for

from aluno import Aluno

from professor import Professor

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")

# Rotas alunos
@app.route("/listar/alunos")
def listar_alunos():

    alunos = Aluno.listar()

    return render_template("listar_alunos.html", alunos=alunos)

@app.route("/cadastro/aluno", methods=('GET', 'POST'))
def cadastro_aluno():

    if request.method == 'POST':

        nome = request.form['nome_aluno']

        cpf = request.form['cpf_aluno']

        email = request.form['email_aluno']

        telefone = request.form['telefone_aluno']

        Aluno(nome = nome, cpf = cpf, telefone = telefone, email=email)

        # redirecionando o cliente para a rota do listar_alunos
        return redirect(url_for('listar_alunos'))

    return render_template("cadastro_aluno.html")

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

# Rotas Professores
@app.route("/listar/professores")
def listar_professores():

    professores = Professor.listar()

    return render_template("listar_professores.html", professores=professores)

@app.route("/cadastro/professor", methods=('GET', 'POST'))
def cadastro_professor():

    if request.method == 'POST':

        nome = request.form['nome_professor']

        cpf = request.form['cpf_professor']

        email = request.form['email_professor']

        telefone = request.form['telefone_professor']

        formacao = request.form['formacao_professor']

        especialidade = request.form['especialidade_professor']

        Professor(nome = nome, cpf = cpf, telefone = telefone, email = email, formacao = formacao, especialidade = especialidade)

        # redirecionando o cliente para a rota do listar_alunos
        return redirect(url_for('listar_professores'))

    return render_template("cadastro_professor.html")

@app.route("/editar/professor/<matricula>", methods=('GET', 'POST'))
def editar_professor(matricula):

    professor = Professor.listaProfessorMatricula(matricula = matricula)

    if request.method == 'POST':

        nome = request.form['nome_professor']

        cpf = request.form['cpf_professor']

        telefone = request.form['telefone_professor']

        email = request.form['email_professor']

        ativo = 0

        if 'ativo_professor' in request.form:
            ativo = 1
        
        formacao = request.form['formacao_professor']

        especialidade = request.form['especialidade_professor']

        Professor.atualizar(matricula = matricula, nome = nome, cpf = cpf, telefone = telefone, email=email, ativo = ativo, formacao = formacao, especialidade = especialidade)

        # redirecionando o cliente para a rota do listar_alunos
        return redirect(url_for('listar_professores'))

    return render_template("editar_professor.html", professor=professor)

# Rotas Turmas
@app.route("/cadastro/turma", methods=('GET', 'POST'))
def cadastro_turma():

    if request.method == 'POST':

        alunos = request.form.getlist['alunos']

        return alunos

    con = sqlite3.connect("gestao_escolar.db")

    cur = con.cursor()

    sql_professores = """
        SELECT matricula, nome FROM professores ORDER BY nome
    """
    cur.execute(sql_professores)

    professores = cur.fetchall()

    sql_alunos = """
        SELECT matricula, nome FROM alunos ORDER BY nome
    """

    cur.execute(sql_alunos)
    
    alunos = cur.fetchall()

    con.close()

    # A função render_template tem o propósito de ler os arquivos
    # Que estão disponíveis na pasta "templates" e apresentar no navegador do usuário
    # NOTE: o nome do arquivo é um texto
    return render_template("cadastro_turma.html", professores=professores, alunos=alunos)