from time import sleep
from assets import acesso
from assets import menus
from assets import gerenciar_rebanho

usuarios_cadastrados = {
    "nome": ["Caio"],
    "senha": ["Caio123"],
    "administrador": [False],
}
usuario_logado = {"nome": None, "administrador": None, "logado": False}
cadatro = {
    "animais": [
        {
            "id": 0,
            "nome": "Bela",
            "idade": 3,
            "raça": "Holandesa",
            "peso": 500,
            "tipo": "Vaca",
            "genero": "Fêmea",
            "preco": 1500,
            "status": "Doente",
        }
    ],
    "produtos": [
        {
            "id": 0,
            "nome": "Leite",
            "quantidade": 100,
            "preço": 2.5,
            "status": "Disponível",
        }
    ],
}
racao = {
    "id": 0,
    "função": "Alimentar os animais",
    "nome": "Ração para bovinos",
    "quantidade": 50,
    "limiar_de_estoque": 10,
}


while True:
    print("""1 - Logar
2 - Cadastrar
0 - Encerrar
""")
    sleep(1)
    op = int(input("Escolha a opção desejada: "))
    if op > 2 or op < 0:
        print(f'Opção inválida , tente novamente!{'\n'*3}')
        sleep(1.6)
        continue

    if op == 1:
        print("=" * 5, " LOGAR ", "=" * 5)
        nome_de_usuario = input("Digite seu nome: ")
        senha_do_usuario = input("Digite sua senha: ")

        usuario_logado = acesso.logar(
            nome_de_usuario, senha_do_usuario, usuarios_cadastrados
        )
        if not usuario_logado:
            print("NOME ou SENHA incorreta ou inválida!!!\nTente Novamente...")
            print(usuario_logado)
            continue
        else:
            print("meu fi ta logado")
            print(usuario_logado)

    elif op == 2:
        print("=" * 5, " CADASTRO ", "=" * 5)
        nome_de_usuario = input("Digite seu nome: ")
        senha_do_usuario = input("Digite sua senha: ")
        print("\nO novo usuario é um CLIENTE ou ADM? : \n1 - ADM\n2 - CLIENTE")
        adm_ou_cliente = int(input("-> "))
        if adm_ou_cliente == 1:
            adm_ou_cliente = True
        elif adm_ou_cliente == 2:
            adm_ou_cliente = False
        elif adm_ou_cliente != 1 or adm_ou_cliente != 2:
            print("Opção inválida!")

        print(
            acesso.cadastrar_usuario(
                nome_de_usuario, senha_do_usuario, adm_ou_cliente, usuarios_cadastrados
            )
        )

    elif op == 0:
        print("Encerrando...")
        break
    while usuario_logado["logado"] and usuario_logado["administrador"] == True:
        menus.menu_adm(usuario_logado)
        op = int(input("-> "))

        if op > 4 or op < 0:
            print(f'Opção inválida , tente novamente!{'\n'*3}')
            sleep(1)
            continue

        elif op == 1:
            while True:
                gerenciar_rebanho.exibir_menu_de_gerenciar_rebanho()
                op1 = int(input("-> "))
                if op1 > 4 or op1 < 0:
                    print(f'Opção inválida , tente novamente!{'\n'*3}')
                    sleep(1)
                    continue
                elif op1 == 0:
                    break
                elif op1 == 1:
                    gerenciar_rebanho.cadastrar_animal(cadatro)

                elif op1 == 2:

                    gerenciar_rebanho.exibir_animais(cadatro, usuario_logado)

                elif op1 == 3:

                    gerenciar_rebanho.editar_animal(cadatro)

                elif op1 == 4:

                    gerenciar_rebanho.remover_animal(cadatro)

        elif op == 2:
            print("""     *****MENU*****
1 - Cadastrar
2 - Buscar
3 - Atualizar Itens
4 - Remover Itens
0 - Voltar""")
            op1 = int(input("\n-> "))
            if op1 == 1:

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

            elif op1 == 2:

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

            elif op1 == 3:

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

            elif op1 == 4:

                def remover_produto(cadastro: dict):
                    id = int(input("Digite o ID do produto que deseja remover: "))
                    for produto in cadastro["produtos"]:
                        if produto["id"] == id:
                            print(
                                f"Você tem certeza que deseja remover o produto ID {id}? (S/N)"
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

        elif op == 3:
            print("Em construção...")

        elif op == 0:
            usuario_logado = {"nome": None, "administrador": None, "logado": False}
            print("Deslogando...")
            sleep(1.6)
            break

    while usuario_logado["logado"] and usuario_logado["administrador"] == False:
        menus.menu_cliente(usuario_logado)
        op = int(input("-> "))
        if op > 2 or op < 0:
            print(f'Opção inválida , tente novamente!{'\n'*3}')
            sleep(1)
            continue
        elif op == 1:
            print("Em construção...")
        elif op == 0:
            print("Deslogando...")
            sleep(1.6)
            usuario_logado = {"nome": None, "administrador": None, "logado": False}
            break
