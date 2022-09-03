import sqlite3

class Curso:

    def __init__(self, nome, classificacao, descricao):

        self.nome = nome

        self.classificacao = classificacao

        self.descricao = descricao

        self.salvar()

    @property
    def codigo(self):

        return self.__codigo

    def salvar(self):

        conexao = sqlite3.connect("gestao_escolar.db")

        cursor = conexao.cursor()

        sql = f"""
            INSERT INTO Cursos (
                nome,
                classificacao,
                descricao  
            )
            VALUES
            (
                '{self.nome}',
                '{self.classificacao}',
                '{self.descricao}'   
            )
        """

        cursor.execute(sql)

        self.__codigo = cursor.lastrowid

        conexao.commit()

        conexao.close()

    @classmethod
    def listar(cls):

        conexao = sqlite3.connect("gestao_escolar.db")

        cursor = conexao.cursor()

        sql = """
            SELECT * FROM Cursos
        """

        cursor.execute(sql)

        lista_cursos = cursor.fetchall()

        conexao.close()

        return lista_cursos

    @classmethod
    def listaCursoCodigo(cls, codigo):

        # abrindo conexao
        conexao = sqlite3.connect("gestao_escolar.db")

        # utilizando o metodo cursor
        # para fazer alguma ação no bd
        cursor = conexao.cursor()

        sql = f"""
            SELECT * FROM Cursos WHERE codigo = '{codigo}'
        """
        # executando a ação
        cursor.execute(sql)

        # lista de curso recuperado do bd
        listaCurso = cursor.fetchone()

        conexao.close()

        return listaCurso

    # atualizar curso no bd
    @classmethod
    def atualizar(cls, codigo, nome, classificacao, ativo, descricao):
        # como conectar no meu banco
        # abrindo conexao
        conexao = sqlite3.connect("gestao_escolar.db")

        # utilizando o metodo cursor
        # para fazer alguma ação no bd
        cursor = conexao.cursor()

        sql = f"""
            UPDATE Cursos SET
            nome = '{nome}',
            classificacao = '{classificacao}',
            ativo = '{ativo}',
            descricao = '{descricao}'
            WHERE codigo = '{codigo}'
        """
        # executando a ação
        cursor.execute(sql)

        # salvando a alteração da tabela(confrima)
        conexao.commit()

        conexao.close()

    def __repr__(self):

        return f"Código: {self.__codigo}, Nome: {self.nome}, Classificação: {self.classificacao}, Descrição: {self.descricao}"


if __name__ == '__main__':

    # curso = Curso(
    #     nome='Curso de C#',
    #     classificacao='Programaçao',
    #     descricao='Curso completo de C#'
    # )

    print(Curso.listar())
