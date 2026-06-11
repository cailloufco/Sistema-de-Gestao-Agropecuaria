def cadastrar_produto(cadastro: dict):
    id = max(cadastro["produtos"]["id"]) + 1

    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    print("O produto está disponível para venda? (S/N): ")
    op = input("-> ").upper()
    if op == "S":
        preco = float(input("Preço: "))
    else:
        preco = "Indisponivel"
    status = input("Status: ")

    produto = {
        "id": id,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
        "status": status,
    }
    cadastro["produtos"].append(produto)
    print(f"Produto ID {id} cadastrado com sucesso!")


def buscar_produto(cadastro: dict, usuario_logado: dict):
    print(
        f'{"\n"*4}O que você deseja buscar, {usuario_logado["nome"]}? \n     *****MENU*****\n 1 - Busca por ID do produto\n 2 - Buscar por nome dos produtos\n 3 - Buscar por status\n 4 - Verificar produtos disponíveis para venda\n 0 - Sair da busca\n'
    )
    op = int(input("-> "))
    if op == 1:
        id = int(input("Digite o ID do produto que deseja buscar: "))
        for produto in cadastro["produtos"]:
            if produto["id"] == id:
                print(
                    f'ID: {produto["id"]} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]} | Status: {produto["status"]}'
                )
                break
        else:
            print(f"Produto ID {id} não encontrado.")

    elif op == 2:
        nome = input("Digite o nome do produto que deseja buscar: ")
        produto_encontrado = False
        for produto in cadastro["produtos"]:
            if produto["nome"] == nome:
                print(
                    f'ID: {produto["id"]} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]} | Status: {produto["status"]}'
                )
                produto_encontrado = True

        if not produto_encontrado:
            print(f"Produtos com nome {nome} não encontrados.")

    elif op == 3:
        status = input("Digite o status do produto que deseja buscar: ")
        produto_encontrado = False
        for produto in cadastro["produtos"]:
            if produto["status"] == status:
                print(
                    f'ID: {produto["id"]} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]} | Status: {produto["status"]}'
                )
                produto_encontrado = True
        if not produto_encontrado:
            print(f"Produtos com status {status} não encontrados.")

    elif op == 4:
        produtos_disponiveis = False
        for produto in cadastro["produtos"]:
            if produto["preco"] != "Indisponivel":
                print(
                    f'ID: {produto["id"]} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]} | Status: {produto["status"]}'
                )
                produtos_disponiveis = True

        if not produtos_disponiveis:
            print("Nenhum produto disponível para venda encontrado.")


def atualizar_produto(cadastro: dict):
    id = int(input("Digite o ID do produto que deseja atualizar: "))
    for produto in cadastro["produtos"]:
        if produto["id"] == id:
            print(
                f'ID: {produto["id"]} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]} | Status: {produto["status"]}'
            )
            print(
                "Digite os novos dados do produto (deixe em branco para manter o valor atual):"
            )
            nome = input("Nome do produto: ")
            quantidade = input("Quantidade: ")
            print("O produto está disponível para venda? (S/N): ")
            op = input("-> ").upper()

            if op == "S":
                preco = float(input("Preço: "))
            else:
                preco = "Indisponivel"
            status = input("Status: ")

            if nome:
                produto["nome"] = nome
            if quantidade:
                produto["quantidade"] = quantidade
            if status:
                produto["status"] = status
            produto["preco"] = preco

            print(f"Produto ID {id} atualizado com sucesso!")


def remover_produto(cadastro: dict):
    id = int(input("Digite o ID do produto que deseja remover: "))
    for produto in cadastro["produtos"]:
        if produto["id"] == id:
            print(
                f"Você tem certeza que deseja remover o produto ID {id} | Nome: {produto['nome']} | Quantidade: {produto['quantidade']} | Preço: {produto['preco']} | Status: {produto['status']} ? (S/N)"
            )
            confirmacao = input("-> ").upper()
            if confirmacao == "S":
                cadastro["produtos"].remove(produto)
                print(f"Produto ID {id} removido com sucesso!")
                break
            else:
                print("Remoção cancelada.")
                break
    else:
        print(f"Produto ID {id} não encontrado.")
