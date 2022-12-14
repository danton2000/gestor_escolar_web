from flask import Flask, render_template, request, redirect, url_for

from aluno import Aluno

from professor import Professor

from curso import Curso

from turma import Turma

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

        # redirecionando o cliente para a rota do listar_professores
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

        # redirecionando o cliente para a rota do listar_professores
        return redirect(url_for('listar_professores'))

    return render_template("editar_professor.html", professor=professor)

# Rotas Cursos
@app.route("/listar/cursos")
def listar_cursos():

    cursos = Curso.listar()

    return render_template("listar_cursos.html", cursos=cursos)

@app.route("/cadastro/curso", methods=('GET', 'POST'))
def cadastro_curso():

    if request.method == 'POST':
       
        nome = request.form['nome_curso']

        classificacao = request.form['classificacao_curso']

        descricao = request.form['descricao_curso']
    
        Curso(nome = nome, classificacao = classificacao, descricao = descricao)

        # redirecionando o cliente para a rota do listar_cursos
        return redirect(url_for('listar_cursos'))

    return render_template("cadastro_curso.html")

@app.route("/editar/curso/<codigo>", methods=('GET', 'POST'))
def editar_curso(codigo):

    curso = Curso.listaCursoCodigo(codigo = codigo)

    if request.method == 'POST':

        nome = request.form['nome_curso']

        classificacao = request.form['classificacao_curso']

        ativo = 0

        if 'ativo_curso' in request.form:
            ativo = 1

        descricao = request.form['descricao_curso']

        Curso.atualizar(codigo = codigo, nome = nome, classificacao = classificacao, ativo = ativo, descricao=descricao)

        # redirecionando o cliente para a rota do listar_cursos
        return redirect(url_for('listar_cursos'))

    return render_template("editar_curso.html", curso=curso)

# Rotas Turmas
@app.route("/listar/turmas")
def listar_turmas():

    turmas = Turma.listar()

    return render_template("listar_turmas.html", turmas=turmas)

@app.route("/listar/turmas_alunos/<codigo_turma>")
def listar_turmas_alunos(codigo_turma):

    alunos = Turma.listarAlunos(codigo_turma)

    return render_template("listar_turmas_alunos.html", alunos=alunos, codigo_turma=codigo_turma)

@app.route("/cadastro/turma", methods=('GET', 'POST'))
def cadastro_turma():

    professores = Professor.listar()

    cursos = Curso.listar()

    alunos = Aluno.listar()

    # CADASTRO TURMA
    if request.method == 'POST':

        # print(request.form)

        data_inicio = request.form['data_inicio']

        data_fim = request.form['data_fim']

        periodo = request.form['periodo']

        matricula_professor = request.form['professor']

        codigo_curso = request.form['curso']

        # Lista de matriculas dos alunos
        alunos_selecionados = request.form.getlist('alunos')

        if len(alunos_selecionados) >= 3:
            # print("Turma criada")
            #Enviando os dados para a classe Turma
            try:
                Turma(periodo=periodo, data_inicio=data_inicio, data_fim=data_fim, codigo_curso=codigo_curso, matricula_professor=matricula_professor, alunos=alunos_selecionados)

                return redirect(url_for("listar_turmas"))
            except ValueError as erro:
                mensagem = erro
                return render_template("cadastro_turma.html", professores=professores, cursos=cursos, alunos=alunos, mensagem=mensagem)
        else:
            mensagem = "Selecione pelo menos 3 alunos"
            return render_template("cadastro_turma.html", professores=professores, cursos=cursos, alunos=alunos, mensagem=mensagem)

    # A fun????o render_template tem o prop??sito de ler os arquivos
    # Que est??o dispon??veis na pasta "templates" e apresentar no navegador do usu??rio
    # NOTE: o nome do arquivo ?? um texto
    return render_template("cadastro_turma.html", professores=professores, cursos=cursos, alunos=alunos, mensagem=None)