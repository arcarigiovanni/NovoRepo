import psycopg2

connection = psycopg2.connect(
    dbname = "playground",
    user = "postgres",
    password = "Pudim123!",
    host = "localhost",
    port = "5432"
)

def createTable():
    with connection.cursor() as cursor:
        cursor.execute('''CREATE TABLE IF NOT EXISTS School
                        (id SERIAL PRIMARY KEY,
                        nome TEXT NOT NULL,
                        idade INT NOT NULL);''')
    connection.commit()

def createAluno(nome, idade):
    sqlQuery = "INSERT INTO School(nome, idade) VALUES ('{}', {})".format(nome, idade)
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
    connection.commit()
    print(f"Aluno {nome} de idade {idade} cadastrado")

def listAluno():
    sqlQuery = "SELECT * from School"
    with connection.cursor() as cursor:
        cursor.execute(sqlQuery)
        alunos = cursor.fetchall()
        for aluno in alunos:
            print(aluno)


createTable()
createAluno("João", 20)
listAluno()

'''
import psycopg2

# Configurar a conexão com o banco de dados PostgreSQL
conexao = psycopg2.connect(
    host="seu_host",
    database="seu_banco_de_dados",
    user="seu_usuario",
    password="sua_senha"
)

# Criação da tabela
def criar_tabela():
    with conexao.cursor() as cursor:
        cursor.execute('''''')
    conexao.commit()

def cria_aluno(nome, idade):
    sqlQuery = "INSERT INTO aluno(nome, idade) VALUES (%s, %s)"
    with conexao.cursor() as cursor:
        cursor.execute(sqlQuery, (nome, idade))
    conexao.commit()
    print(f"Aluno {nome} de idade {idade} cadastrado")

def listar_alunos():
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM aluno")
        alunos = cursor.fetchall()
        for aluno in alunos:
            print(aluno)

def atualizar_aluno(id, novo_nome, nova_idade):
    sqlQuery = "UPDATE aluno SET nome = %s, idade = %s WHERE id = %s"
    with conexao.cursor() as cursor:
        cursor.execute(sqlQuery, (novo_nome, nova_idade, id))
    conexao.commit()
    print("Aluno atualizado")

def excluir_aluno(id):
    sqlQuery = "DELETE FROM aluno WHERE id = %s"
    with conexao.cursor() as cursor:
        cursor.execute(sqlQuery, (id,))
    conexao.commit()
    print("Aluno excluído com sucesso")

# Exemplo de uso
criar_tabela()
cria_aluno("João", 20)
cria_aluno("Maria", 22)
listar_alunos()
atualizar_aluno(1, "Joana", 21)
excluir_aluno(2)
'''