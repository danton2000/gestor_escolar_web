import sqlite3

class Professor:

    def __init__(self, nome, cpf, telefone=None, email=None,  formacao=None, especialidade=None):

        self.nome = nome

        self.cpf = cpf

        self.telefone = telefone

        self.verificaEmail(email)

        self.formacao = formacao

        self.especialidade = especialidade

        self.salvar()

    @property
    def matricula(self):

        return self.__matricula

    def verificaEmail(self, email):

        if email != "":
            if '@' in email:
                # true
                self.email = email
            else:
                # false
                raise ValueError('E-mail inválido.')
        else:
            self.email = email

    def salvar(self):

        conexao = sqlite3.connect('gestao_escolar.db')

        cursor = conexao.cursor()

        sql = f"""
            INSERT INTO Professores (
                nome,
                cpf,
                telefone,
                email,
                formacao,
                especialidade
            )
            VALUES (
                '{self.nome}',
                '{self.cpf}',
                '{self.telefone}',
                '{self.email}',
                '{self.formacao}',
                '{self.especialidade}'
            )
        """

        cursor.execute(sql)

        self.__matricula = cursor.lastrowid

        conexao.commit()

        conexao.close()

    @classmethod
    def listar(cls):

        conexao = sqlite3.connect("gestao_escolar.db")

        cursor = conexao.cursor()

        sql = """
            SELECT *
            FROM Professores
        """

        cursor.execute(sql)

        lista_professores = cursor.fetchall()

        conexao.close()

        return lista_professores

    @classmethod
    def listaProfessorMatricula(cls, matricula):

        # abrindo conexao
        conexao = sqlite3.connect("gestao_escolar.db")

        # utilizando o metodo cursor
        # para fazer alguma ação no bd
        cursor = conexao.cursor()

        sql = f"""
            SELECT * FROM Professores WHERE matricula = '{matricula}'
        """
        # executando a ação
        cursor.execute(sql)

        # lista de alunos recuperado do bd
        listaProfessor = cursor.fetchone()

        conexao.close()

        return listaProfessor

    # atualizar professor no bd
    @classmethod
    def atualizar(cls, matricula, nome, cpf, telefone, email, ativo, formacao, especialidade):
        # como conectar no meu banco
        # abrindo conexao
        conexao = sqlite3.connect("gestao_escolar.db")

        # utilizando o metodo cursor
        # para fazer alguma ação no bd
        cursor = conexao.cursor()

        sql = f"""
            UPDATE Professores SET
            nome = '{nome}',
            cpf = '{cpf}',
            telefone = '{telefone}',
            email = '{email}',
            ativo = '{ativo}',
            formacao = '{formacao}',
            especialidade = '{especialidade}'
            WHERE matricula = '{matricula}'
        """
        # executando a ação
        cursor.execute(sql)

        # salvando a alteração da tabela(confrima)
        conexao.commit()

        conexao.close()

    def __repr__(self):

        return f"Matricula: {self.__matricula}, Nome: {self.nome}, CPF: {self.cpf}, Telefone: {self.telefone}, E-mail: {self.email}, Formação: {self.formacao}, Especialidade: {self.especialidade}"


if __name__ == '__main__':

    # professor = Professor(nome='Felipe', cpf=12)

    print(Professor.listar())
