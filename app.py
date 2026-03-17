import sqlite3

print("Sistema iniciado")

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")

conexao.commit()

def cadastrar():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")

    cursor.execute(
        "INSERT INTO clientes (nome, email) VALUES (?, ?)",
        (nome, email)
    )
    conexao.commit()

    print("Cliente cadastrado com sucesso!")

def listar():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    print("\nLista de clientes:")
    for cliente in clientes:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")

def atualizar():
    id_cliente = input("Digite o ID do cliente que deseja atualizar: ")
    novo_nome = input("Digite o novo nome: ")
    novo_email = input("Digite o novo email: ")

    cursor.execute(
        "UPDATE clientes SET nome = ?, email = ? WHERE id = ?",
        (novo_nome, novo_email, id_cliente)
    )
    conexao.commit()

    print("Cliente atualizado com sucesso!")

def deletar():
    id_cliente = input("Digite o ID do cliente que deseja deletar: ")

    cursor.execute(
        "DELETE FROM clientes WHERE id = ?",
        (id_cliente,)
    )
    conexao.commit()

    print("Cliente deletado com sucesso!")

cadastrar()
listar()
atualizar()
listar()
deletar()
listar()

conexao.close()