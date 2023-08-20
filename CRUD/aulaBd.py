import sqlite3

conexao = sqlite3.connect("aula.db")

conexao.execute(''' CREATE TABLE IF NOT EXISTS aluno
                ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INT NOT NULL);''')

def cria_aluno(nome, idade):
    sqlQuery = "INSERT INTO aluno(nome, idade) VALUES ('{}', {})".format(nome, idade) #se for string é melhor usar as aspas simples antes das chaves
    conexao.execute(sqlQuery)
    conexao.commit()
    print(f"Aluno {nome} de idade {idade} cadastrado")

def listar_alunos():
    listar_alunos = conexao.execute("SELECT * FROM aluno")
    for aluno in listar_alunos:
        print(aluno)

def atualizar_aluno(id, novo_nome, nova_idade):
    sqlQuery = "UPDATE aluno SET nome = '{}', idade = {} where id = {}".format(novo_nome, nova_idade, id)
    print(sqlQuery)
    conexao.execute(sqlQuery)
    conexao.commit()
    print("Aluno aualizado")
    #"UPDATE aluno SET nome=?, idade=? WHERE id =(?)", (novo_nome, nova_idade, id)

def excluir_aluno(id):
    sqlquery = "DELETE FROM aluno WHERE id = {};".format(id)
    # conexao.execute("DELETE FROM aluno WHERE id = ?;",(id))
    conexao.execute(sqlquery)
    conexao.commit()
    print("aluno excluído com sucesso") 

#cria_aluno("Giovanni Arcari P", 30)
#atualizar_aluno(1, "Isabella", 25)
listar_alunos()

