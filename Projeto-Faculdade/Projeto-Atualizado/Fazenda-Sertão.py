from time import sleep
from assets import acesso
from assets import menus
from assets import gerenciar_rebanho
from assets import gerencia_producaoEderivados

usuarios_cadastrados = {
    "nome": ["Caio"],
    "senha": ["Caio123"],
    "administrador": [False],
}
usuario_logado = {"nome": None, "administrador": None, "logado": False}
cadastro = {
    "animais": [
        {
            "id": "00126-A",
            "nome": "Belinha",
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
            "preco": 2.5,
            "status": "Disponível",
        }
    ],
    "racao": [
        {
            "id": 0,
            "funcao": "Alimentar os animais",
            "nome": "Ração para bovinos",
            "quantidade": 50,
            "limiar_de_estoque": 10,
        }
    ],
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
        print(usuarios_cadastrados)

    elif op == 0:
        print("Encerrando...")
        break
    while usuario_logado["logado"] and usuario_logado["administrador"] == True:
        menus.menu_adm(usuario_logado)
        op = int(input("-> "))

        if op > 5 or op < 0:
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
                    gerenciar_rebanho.cadastrar_animal(cadastro)

                elif op1 == 2:

                    gerenciar_rebanho.exibir_animais(cadastro, usuario_logado)

                elif op1 == 3:

                    gerenciar_rebanho.editar_animal(cadastro)

                elif op1 == 4:

                    gerenciar_rebanho.excluir_animal(cadastro)

        elif op == 2:
            print("""     *****MENU*****
1 - Cadastrar
2 - Buscar
3 - Atualizar Itens
4 - Remover Itens
0 - Voltar""")
            op1 = int(input("\n-> "))
            if op1 == 1:

                gerencia_producaoEderivados.cadastrar_produto(cadastro)

            elif op1 == 2:

                gerencia_producaoEderivados.buscar_produto(cadastro, usuario_logado)

            elif op1 == 3:

                gerencia_producaoEderivados.atualizar_produto(cadastro)

            elif op1 == 4:

                gerencia_producaoEderivados.remover_produto(cadastro)

        elif op == 3:
            print(
                f'{"\n"*4}Gerenciar Ração, {usuario_logado["nome"]}? \n     *****MENU*****\n 1 - Cadastrar uma ração\n 2 - Vizualizar Estoque\n 3 - Atulizar estoque\n 0 - Sair\n'
            )
            op1 = int(input("\n-> "))

            def cadastrar_racao(cadastro: dict):

                id = max(cadastro["racao"]["id"]) + 1

                funcao = input(
                    "Qual a finalidade da ração? ( ex: Engorda, Postura Inicial/Crescimento... ):\n"
                )

                nome = input(
                    "Qual o nome da ração? ( ex: Farelo de Milho, Nutron Ovos...):\n"
                )

                quantidade = float(
                    input("Quantos quilos de ração foram adquiridos: \n")
                )

                limiar_racao = float(
                    input("Qual o limite minimo do estoque para esta ração?: \n")
                )

                cadastro["racao"].append(
                    {
                        "id": id,
                        "funcao": funcao,
                        "nome": nome,
                        "quantidade": quantidade,
                        "limiar_de_estoque": limiar_racao,
                    }
                )
                print(f"Ração ID {id} cadastrada com sucesso!")

        elif op == 4:
            print("Em construção pq precisa fazer as funcionalidades de cliente")

        elif op == 5:

            def notificacoes(cadastro: dict):
                print(
                    f'{"\n"*4}Notificações, {usuario_logado["nome"]}? \n     *****MENU*****\n 1 - Animais doentes\n 2 - Estoque de ração abaixo do limiar\n 0 - Sair\n'
                )
                op = int(input("\n-> "))
                if op == 1:
                    animais_doentes = False
                    for animal in cadastro["animais"]:
                        if animal["status"].lower() == "doente":
                            print(
                                f'ID: {animal["id"]} | Nome: {animal["nome"]} | Idade: {animal["idade"]} | Raça: {animal["raça"]} | Peso: {animal["peso"]} | Tipo: {animal["tipo"]} | Gênero: {animal["genero"]} | Preço: {animal["preco"]} | Status: {animal["status"]}'
                            )
                            animais_doentes = True
                    if not animais_doentes:
                        print("Nenhum animal doente encontrado.")

                elif op == 2:
                    racao_baixo_estoque = False
                    for racao in cadastro["racao"]:
                        if racao["quantidade"] < racao["limiar_de_estoque"]:
                            print(
                                f'ID: {racao["id"]} | Função: {racao["funcao"]} | Nome: {racao["nome"]} | Quantidade: {racao["quantidade"]} | Limiar de Estoque: {racao["limiar_de_estoque"]}'
                            )
                            racao_baixo_estoque = True
                    if not racao_baixo_estoque:
                        print("Nenhuma ração com estoque abaixo do limiar encontrada.")

        elif op == 0:
            usuario_logado = {"nome": None, "administrador": None, "logado": False}
            print("Deslogando...")
            sleep(1.6)
            break

    while usuario_logado["logado"] and usuario_logado["administrador"] == False:

        menus.menu_cliente(usuario_logado)

        op = int(input("-> "))
        if op > 6 or op < 0:
            print(f'Opção inválida , tente novamente!{'\n'*3}')
            sleep(1)
            continue
        elif op == 1:

            def realizar_compra(cadastro: dict, usuario_logado: dict):
                print(
                    f'{"\n"*4}O que você deseja comprar, {usuario_logado["nome"]}? \n     *****MENU*****\n 1 - Comprar um animal\n 2 - Comprar um produto\n 0 - Sair\n'
                )
                op = int(input("-> "))
                if op == 1:
                    print("Digite o ID do animal que deseja comprar: ")
                    id = int(input("-> "))
                    for animal in cadastro["animais"]:
                        if animal["id"] == id:
                            if animal["preco"] != "Indisponivel":
                                print(
                                    f'ID: {animal["id"]} | Nome: {animal["nome"]} | Raça: {animal["raça"]} | Tipo: {animal["tipo"]} | Preço: {animal["preco"]} | Status: {animal["status"]}'
                                )
                                print("Deseja confirmar a compra? (S/N)")
                                confirmacao = input("-> ").upper()
                                if confirmacao == "S":
                                    cadastro["animais"].remove(animal)
                                    print(f"Compra do animal ID {id} confirmada!")
                                    break
                                else:
                                    print("Compra cancelada.")
                                    break
                            else:
                                print(f"Animal ID {id} não disponível para venda.")
                                break
                    else:
                        print(f"Animal ID {id} não encontrado.")

                elif op == 2:
                    print("Digite o ID do produto que deseja comprar: ")
                    id = int(input("-> "))
                    for produto in cadastro["produtos"]:
                        if produto["id"] == id:
                            if (
                                produto["status"] != "Indisponivel"
                                and produto["quantidade"] != 0
                            ):
                                print(
                                    f'ID: {produto["id"]} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]} | Status: {produto["status"]}'
                                )
                                print("Deseja confirmar a compra? (S/N)")
                                confirmacao = input("-> ").upper()
                                if confirmacao == "S":
                                    quantidade_comprada = int(
                                        input(
                                            "Digite a quantidade que deseja comprar: "
                                        )
                                    )
                                    if quantidade_comprada <= 0:
                                        print(
                                            "Quantidade inválida. A compra foi cancelada."
                                        )
                                        break

                                    elif quantidade_comprada > produto["quantidade"]:
                                        print(
                                            f"Quantidade solicitada ({quantidade_comprada}) excede o estoque disponível ({produto['quantidade']})."
                                        )
                                        print("A compra foi cancelada.")
                                        break

                                    else:
                                        produto["quantidade"] -= quantidade_comprada
                                        print(
                                            f"Compra de {quantidade_comprada} unidades do produto ID {id} confirmada!"
                                        )
                                        if produto["quantidade"] == 0:
                                            produto["status"] = "Indisponivel"
                                        break
                                else:
                                    print("Compra cancelada.")
                                    break
                            else:
                                print(
                                    "Produto não disponível para venda ou sem estoque."
                                )
                    else:
                        print(f"Produto ID {id} não encontrado.")

        elif op == 2:
            def vizualizar_estoque(cadastro: dict , usuario_logado: dict):
                print(
                    f'{"\n"*4}O que você deseja comprar, {usuario_logado["nome"]}? \n     *****MENU*****\n 1 - Visualizar Estoque de Animais à Venda\n 2 - Visualizar Estoque de Produtos\n 0 - Sair\n'
                )
                op = int(input("-> "))
                if op == 1:
                    animal_a_venda = False
                    if cadastro["animais"]:

                        for animal in cadastro["animais"]:
                            if animal["preco"] != "Indisponivel":
                                print(
                                    f'ID: {animal["id"]} | Nome: {animal["nome"]} | Raça: {animal["raça"]} | Tipo: {animal["tipo"]} | Preço: {animal["preco"]} | Status: {animal["status"]}'
                                )
                                animal_a_venda = True
                        if not animal_a_venda:
                            print("Nenhum animal disponível para venda encontrado.")

                    else:
                        print("Nenhum animal cadastrado.")
                elif op == 2:
                    produto_disponivel = False
                    if cadastro["produtos"]:
                        for produto in cadastro["produtos"]:
                            if (
                                produto["status"] != "Indisponivel"
                                and produto["quantidade"] != 0
                            ):
                                print(
                                    f'ID: {produto["id"]} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]} | Status: {produto["status"]}'
                                )
                                produto_disponivel = True
                        if not produto_disponivel:
                            print("Nenhum produto disponível para venda encontrado.")
                    else:
                        print("Nenhum produto cadastrado.")

        elif op == 0:
            print("Deslogando...")
            sleep(1.6)
            usuario_logado = {"nome": None, "administrador": None, "logado": False}
            break
