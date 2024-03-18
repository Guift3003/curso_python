import os

produtos = [
    {
        "codigo": 100,
        "nome": "Mouse",
        "valor": 50.00,
        "fabricante": "Microsoft",
        "ativo": False

    },
    {
        "codigo": 200,
        "nome": "Teclado",
        "valor": 68.99,
        "fabricante": "Logitech",
        "ativo": False
    },
    {
        "codigo": 300,
        "nome": "Monitor LED 17P",
        "valor": 499.99,
        "fabricante": "LG",
        "ativo": False
    }]


def criar_menu():
    os.system("cls")
    print("""🅴🆂🆃🅾🆀🆄🅴 🅰🅿🅿""")
    print("1. Cadastrar produto")
    print("2. Listar Produtos")
    print("3. Ativar/Desativar produtos")
    print("4. Excluir produto")
    print("5. Sair")


def voltar_ao_menu_principal():
    input("Pressione Enter para voltar ao menu principal....")
    main()


def criar_titulo(titulo):
    os.system("cls")
    print(f"**** {titulo} ****\n")

def cadastrar_produto():
    criar_titulo("CADASTRO DE PRODUTOS")

    codigo = int(input("Codigo do produto: "))
    nome = input("Nome do produto: ")
    valor = float(input("Valor do produto: "))
    fabricante = input("Fabricante do produto")
    ativo = False

    produtos.append(
        {
            "codigo": codigo,
            "nome": nome,
            "valor": valor,
            "fabricante": fabricante,
            "ativo": ativo
        }
    )

    print()
    print(f"Produto {nome.upper()}, cadastrado com sucesso!\n")
    voltar_ao_menu_principal()


def exibir_produtos():
    criar_titulo("LISTAR PRODUTOS")

    tamanho_vetor = len(produtos)

    print(f"Total de produtos cadastrados: {tamanho_vetor}")
    print()
    print(f"")
    print("-------------------------------------------------------------------------")
    for produto in produtos:
        codigo = produto["codigo"]
        nome = produto["nome"]
        valor = produto["valor"]
        if produto["ativo"]:
            status = "ATIVO"
        else:
            status = "INATIVO"
        print(f"{codigo:<10}  {nome:<30}  R$ {valor:>6} {status:>}")
        print("-------------------------------------------------------------------------")

    print()
    voltar_ao_menu_principal()


def excluir_produto():
    criar_titulo("Excluir Produto.")

    # indice = int(input("Qual o índice do produto que será removido? "))

    nome_produto = input("Qual o nome do produto? ")

    produtos.remove(nome_produto)

    # confirmacao = input(f"Você confirma a exclusão do produto {produtos[indice]} (s/n)?")
    #
    # if confirmacao == "s":
    #     excluido = produtos.pop(indice)
    #     print(f"O produto {excluido} foi excluído com sucesso!")
    # else:
    #     print("Operação de exclusão cancelada.")
    #     voltar_ao_menu_principal()

    voltar_ao_menu_principal()

def status_produto():

    codigo_status_novo = int(input("Digite o código do produto que você deseja alterar o status: "))

    for produto in produtos:
        if produto["codigo"] == codigo_status_novo:
            acao = int(input("Digite 0 se você deseja ATIVAR o produto.\nDigite 1 se você deseja DESATIVAR o produto\n"))
            if acao == 0:
                produto["ativo"] = True
                print("O status do produto foi alterado")
                voltar_ao_menu_principal()
            else:
                produto["ativo"] = False
                print("O status do produto foi alterado")
                voltar_ao_menu_principal()
    print("Produto não encontrado")
    voltar_ao_menu_principal()








def escolher_opcao():

    try:
        opcao = int(input("\nEscolha uma opção(1 a 5): "))

        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            exibir_produtos()
        elif opcao == 3:
            status_produto()
        elif opcao == 4:
            excluir_produto()
        elif opcao == 5:
            exit()
        else:
            tratar_erro()

    except:
        tratar_erro()


def tratar_erro():
    input("Valor inválido! Pressione Enter para voltar ao menu principal...")
    main()


def main():
    criar_menu()
    escolher_opcao()


if __name__ == "__main__":
    main()











