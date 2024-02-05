import sqlite3

class Nota:
    def __init__(self, id, titulo, descricao):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao

def conectar_bd():
    return sqlite3.connect('notas.db')

def criar_tabela_notas(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            descricao TEXT
        )
    ''')
    conexao.commit()

def listar_notas(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM notas')
    notas = cursor.fetchall()
    if not notas:
        print("Nenhuma nota encontrada.")
    else:
        for nota in notas:
            print(f"ID: {nota[0]} | Título: {nota[1]} | Descrição: {nota[2]}")

def adicionar_nota(conexao):
    titulo = input("Digite o título da nota: ")
    descricao = input("Digite a descrição da nota: ")
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO notas (titulo, descricao) VALUES (?, ?)', (titulo, descricao))
    conexao.commit()
    print("Nota adicionada com sucesso!")

def atualizar_nota(conexao):
    id = int(input("Digite o ID da nota que deseja atualizar: "))
    titulo = input("Digite o novo título da nota: ")
    descricao = input("Digite a nova descrição da nota: ")
    cursor = conexao.cursor()
    cursor.execute('UPDATE notas SET titulo=?, descricao=? WHERE id=?', (titulo, descricao, id))
    if cursor.rowcount == 0:
        print("Nota não encontrada.")
    else:
        conexao.commit()
        print("Nota atualizada com sucesso!")

def deletar_nota(conexao):
    id = int(input("Digite o ID da nota que deseja deletar: "))
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM notas WHERE id=?', (id,))
    if cursor.rowcount == 0:
        print("Nota não encontrada.")
    else:
        conexao.commit()
        print("Nota deletada com sucesso!")

def main():
    conexao = conectar_bd()
    criar_tabela_notas(conexao)

    while True:
        print("\n===== MENU =====")
        print("1. Listar notas")
        print("2. Adicionar nota")
        print("3. Atualizar nota")
        print("4. Deletar nota")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_notas(conexao)
        elif escolha == "2":
            adicionar_nota(conexao)
        elif escolha == "3":
            atualizar_nota(conexao)
        elif escolha == "4":
            deletar_nota(conexao)
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    conexao.close()

if __name__ == "__main__":
    main()