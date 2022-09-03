import sqlite3

class Turma:

    def __init__(self, periodo, data_inicio, data_fim, codigo_curso, matricula_professor, alunos):

        self.__codigo = 0

        self.periodo = periodo

        self.data_inicio = data_inicio

        self.data_fim = data_fim

        self.codigo_curso = codigo_curso

        self.matricula_professor = matricula_professor

        self.alunos = alunos

        self.salvar()

    @property
    def codigo(self):

        return self.__codigo

    def salvar(self):

        # self.verificaPeriodo()

        conexao = sqlite3.connect("gestao_escolar.db")

        cursor = conexao.cursor()

        sql = f"""
            INSERT INTO
            Turmas (
                periodo,
                data_inicio,
                data_fim,
                codigo_curso,
                matricula_professor
            )
            VALUES (
                '{self.periodo}',
                '{self.data_inicio}',
                '{self.data_fim}',
                '{self.codigo_curso}',
                '{self.matricula_professor}'
            )
        """

        cursor.execute(sql)

        self.__codigo = cursor.lastrowid

        conexao.commit()

        # Laço que faz a vinculação da turma com os alunos
        for aluno in self.alunos:

            sql = f"""
                INSERT INTO
                Turmas_Alunos (
                    codigo_turma,
                    matricula_aluno
                )
                VALUES (
                    '{self.__codigo}',
                    '{aluno}'
                )
            """

            cursor.execute(sql)

            conexao.commit()

        conexao.close()

    def verificaPeriodo(self):

        conexao = connect("gestao_escolar.db")

        cursor = conexao.cursor()
        # Nesse SELECT ESTOU VERIFICANDO SE TEM INTERVALO ENTRE AS DATAS
        # SE A DATA_INICIO e DATA_FIM ESTIVER NO INTERVELAO ENTRE AS DATAS QUE ESTÃO NO BANCO DE DADOS
        # E SE TIVEREM NO MESMO PERIODO E PROFESSOR
        # A TURMA NÃO É CRIADA
        sql = f"""
                SELECT codigo FROM Turmas
                WHERE data_inicio AND data_fim
                BETWEEN '{self.data_inicio}'
                AND '{self.data_fim}'
                AND matricula_professor = '{self.matricula_professor}'
                AND periodo = '{self.periodo}'

            """

        cursor.execute(sql)

        codigo = cursor.fetchall()

        if codigo != []:
            raise ValueError('Professor já está em uma turma nesse periodo')

        conexao.close()
    
    @classmethod
    def listar(cls):

        # abrindo conexao
        conexao = sqlite3.connect("gestao_escolar.db")

        # utilizando o metodo cursor
        # para fazer alguma ação no bd
        cursor = conexao.cursor()

        sql = f"""
            SELECT tm.codigo, tm.periodo, tm.data_inicio,
            tm.data_fim, tm.codigo_curso, cs.nome, tm.matricula_professor, pf.nome
            FROM Turmas AS tm
            INNER JOIN Cursos AS cs ON tm.codigo_curso = cs.codigo
            INNER JOIN Professores AS pf ON tm.matricula_professor = pf.matricula
        """
        # executando a ação
        cursor.execute(sql)

        # lista de alunos recuperados do bd
        listaTurmas = cursor.fetchall()

        conexao.close()

        return listaTurmas

    @classmethod
    def listarAlunos(cls, codigo_turma):

        # abrindo conexao
        conexao = sqlite3.connect("gestao_escolar.db")

        # utilizando o metodo cursor
        # para fazer alguma ação no bd
        cursor = conexao.cursor()

        sql = f"""
            SELECT an.matricula, an.nome, an.cpf, an.telefone, an.email 
            FROM Alunos AS an
            INNER JOIN Turmas_Alunos AS tm_an ON an.matricula = tm_an.matricula_aluno
            WHERE tm_an.codigo_turma = '{codigo_turma}'
        """
        # executando a ação
        cursor.execute(sql)

        # lista de alunos recuperados do bd
        listaAlunos = cursor.fetchall()

        conexao.close()

        return listaAlunos

    def __repr__(self):

        return f"Código: {self.codigo}, Periodo: {self.periodo}, Data Inicio: {self.data_inicio}, Data Fim: {self.data_fim}, Código_curso: {self.codigo_curso}, Matricula_professor: {self.matricula_professor}"


if __name__ == '__main__':

    python_caldeira = Turma(
        periodo='Tarde',
        data_inicio='2022-07-01',
        data_fim='2022-07-31',
        codigo_curso='1',
        matricula_professor='6'
    )

    print(python_caldeira)
