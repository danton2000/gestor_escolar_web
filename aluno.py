import sqlite3
# teste


class Aluno:
    def __init__(self, nome, cpf, email, telefone=None):

        self.nome = nome

        self.cpf = cpf

        # self.__matricula = 0
        # só a classe podem 'alterar' esse metodo
        # self.incrementar_matricula()

        # propriedade, parece um atributo, setter
        self.email = email

        self.telefone = telefone

        self.salvar()

    # bloqueando o atributo, podem só visualizar
    # metodo que virou um 'atributo'
    @property
    def matricula(self):

        return self.__matricula

    @property
    def email(self):

        return self.__email

    # habilitando a alteração do email
    @email.setter
    def email(self, email):

        if '@' in email:
            # true
            self.__email = email
        else:
            # false
            raise ValueError('E-mail inválido.')

    # adicionar aluno no bd
    def salvar(self):
        # como conectar no meu banco
        # abrindo conexao
        conexao = sqlite3.connect("gestao_escolar.db")

        # utilizando o metodo cursor
        # para fazer alguma ação no bd
        cursor = conexao.cursor()

        sql = f"""
            INSERT INTO Alunos (
                nome,
                cpf,
                telefone,
                email
            )
            VALUES (
                '{self.nome}',
                '{self.cpf}',
                '{self.telefone}',
                '{self.email}'
            )
        """
        # executando a ação
        cursor.execute(sql)

        # retornando a ultima id (key primary)
        self.__matricula = cursor.lastrowid

        # salvando a alteração da tabela(confrima)
        conexao.commit()

        conexao.close()

    @classmethod
    def listar(cls):

        # abrindo conexao
        conexao = sqlite3.connect("gestao_escolar.db")

        # utilizando o metodo cursor
        # para fazer alguma ação no bd
        cursor = conexao.cursor()

        sql = f"""
            SELECT * FROM Alunos
        """
        # executando a ação
        cursor.execute(sql)

        # lista de alunos recuperados do bd
        listaAlunos = cursor.fetchall()

        conexao.close()

        return listaAlunos

    @classmethod
    def listaAlunoMatricula(cls, matricula):

        # abrindo conexao
        conexao = sqlite3.connect("gestao_escolar.db")

        # utilizando o metodo cursor
        # para fazer alguma ação no bd
        cursor = conexao.cursor()

        sql = f"""
            SELECT * FROM Alunos WHERE matricula = '{matricula}'
        """
        # executando a ação
        cursor.execute(sql)

        # lista de alunos recuperado do bd
        listaAluno = cursor.fetchone()

        conexao.close()

        return listaAluno

    # atualizar aluno no bd
    @classmethod
    def atualizar(cls, matricula, nome, cpf, telefone, email):
        # como conectar no meu banco
        # abrindo conexao
        conexao = sqlite3.connect("gestao_escolar.db")

        # utilizando o metodo cursor
        # para fazer alguma ação no bd
        cursor = conexao.cursor()

        sql = f"""
            UPDATE Alunos SET
            nome = '{nome}',
            cpf = '{cpf}',
            telefone = '{telefone}',
            email = '{email}'
            WHERE matricula = '{matricula}'
        """
        # executando a ação
        cursor.execute(sql)

        # salvando a alteração da tabela(confrima)
        conexao.commit()

        conexao.close()

    def __repr__(self):

        return f"Matricula: {self.matricula} Nome: {self.nome}, CPF: {self.cpf}, Email: {self.email}, Telefone: {self.telefone}"


if __name__ == '__main__':

    joao = Aluno(nome='João', cpf=1, email='joao')

    # print(Aluno.listar())
