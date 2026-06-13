from datetime import datetime
from assets import menus


def cadastrar_produto(cadastro: dict):
    ids_existentes = [produto["id"] for produto in cadastro["produtos"]]
    id = max(ids_existentes, default=-1) + 1

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
    menus.mostrar_cabecalho_tela("BUSCA DE PRODUTOS")
    print(f"O que você deseja buscar, {usuario_logado['nome']}?\n")
    print(" 1 - Busca por ID do produto")
    print(" 2 - Buscar por nome dos produtos")
    print(" 3 - Buscar por status")
    print(" 4 - Verificar produtos disponíveis para venda")
    print(" 0 - Sair da busca")
    print("=" * 60)

    while True:
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

        elif op == 0:
            break

        else:
            print("Opção inválida.")


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


def cadastrar_racao(cadastro: dict, usuario_logado: dict):
    while True:
        menus.mostrar_cabecalho_tela("GERENCIAR RAÇÃO")
        print(f"Gerenciar Ração, {usuario_logado['nome']}?\n")
        print(" 1 - Cadastrar uma ração")
        print(" 2 - Visualizar Estoque")
        print(" 3 - Atualizar estoque")
        print(" 0 - Sair")
        print("=" * 60)
        op = int(input("\n-> "))
        if op > 3 or op < 0:
            print("Opção inválida. Tente novamente.\n")
            continue
        if op == 1:
            ids_existentes = [item["id"] for item in cadastro["racao"]]
            id = max(ids_existentes, default=-1) + 1

            funcao = input(
                "Qual a finalidade da ração? ( ex: Engorda, Postura Inicial/Crescimento... ):\n"
            )

            nome = input(
                "Qual o nome da ração? ( ex: Farelo de Milho, Nutron Ovos...):\n"
            )

            quantidade = float(input("Quantos quilos de ração foram adquiridos: \n"))

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

        elif op == 2:
            achou = False
            for racao in cadastro["racao"]:
                print(
                    f"ID: {racao['id']} | Nome: {racao['nome']} | Quantidade: {racao['quantidade']} | Limiar: {racao['limiar_de_estoque']} | Função: {'funcao'}"
                )
                achou = True
            if not achou:
                print("Nenhuma ração cadastrada")
                sleep(1.6)
                continue

        elif op == 3:
            print(f"Digite o ID da Ração que deseja Atualizar")
            id = int(input("-> "))
            for racao in cadastro["racao"]:
                if racao["id"] == id:
                    print(
                        f"ID: {racao['id']} | Nome: {racao['nome']} | Quantidade: {racao['quantidade']} | Limiar: {racao['limiar_de_estoque']} | Função: {racao['funcao']}"
                    )
                    print(
                        "Digite os novos dados do produto (deixe em branco para manter o valor atual):"
                    )
                    nome = input("Nome do produto: ")
                    quantidade = input("Quantidade: ")
                    limiar = float(input("Limiar: "))
                    funcao = input("Status: ")

                    if nome:
                        racao["nome"] = nome
                    if quantidade:
                        racao["quantidade"] = quantidade
                    if funcao:
                        racao["funcao"] = funcao
                    if limiar:
                        racao["limiar_de_estoque"] = limiar

                    print(f"Produto ID {id} atualizado com sucesso!")
        elif op == 0:
            print("Encerrando...")
            break


def notificacoes(cadastro: dict, usuario_logado: dict):
    menus.mostrar_cabecalho_tela("NOTIFICAÇÕES")
    print(f"Notificações, {usuario_logado['nome']}?\n")
    print(" 1 - Animais doentes")
    print(" 2 - Estoque de ração abaixo do limiar")
    print(" 0 - Sair")
    print("=" * 60)
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


from time import sleep


def exibir_menu_de_gerenciar_rebanho():
    print(
        f'{"\n"*4}Gerenciar Rebanho\n 1 - Cadastrar Animal\n 2 - Visualizar Animais\n 3 - Editar Animal\n 4 - Excluir Animal\n 0 - Voltar ao Menu Anterior\n'
    )


def cadastrar_animal(cadastro: dict):

    while True:

        ano = input("Digite o ano de nascimento: ")
        lote = input("Digite o lote do animal: ").upper()

        contador = 0

        for animal in cadastro["animais"]:
            if "ano" in animal and "lote" in animal:
                if animal["ano"] == ano and animal["lote"] == lote:
                    animal_numero = int(animal["id"][:3])
                    if animal_numero > contador:
                        contador = animal_numero

        numero = str(contador + 1).zfill(3)
        ano_formatado = ano[-2:]
        codigo = f"{numero}{ano_formatado}-{lote}"

        nome = input("Digite o nome do animal: ")
        raça = input("Digite a raça do animal: ")
        peso = float(input("Digite o peso do animal: "))
        tipo = input("Digite o tipo do animal: ")
        genero = input("Digite o gênero do animal:  ( M - F )").upper()
        if genero != "F" and genero != "M":
            print("Genero inválido! Tente novamente....\n\n\n\n")
            sleep(1.6)
            continue
        status = input("Digite o status do animal: ")

        op = input("O animal está disponível para venda? (S/N): ").upper()

        if op == "S":
            preco = float(input("Digite o preço do animal: "))
        else:
            preco = "Indisponível"

        cadastro["animais"].append(
            {
                "id": codigo,
                "nome": nome,
                "idade": datetime.now().year - int(ano),
                "raça": raça,
                "peso": peso,
                "tipo": tipo,
                "genero": genero,
                "preco": preco,
                "status": status,
                "ano": ano,
                "lote": lote,
            }
        )

        print("\nAnimal cadastrado com sucesso!")
        print(f"Nome: {nome}")
        print(f"Código: {codigo}")

        continuar = input("\nCadastrar outro animal? (S/N): ").upper()

        if continuar != "S":
            break


def exibir_animais(cadastro: dict, usuario_logado: dict):
    menus.mostrar_cabecalho_tela("VISUALIZAR ANIMAIS")
    print(f"Qual animal você deseja visualizar, {usuario_logado['nome']}?\n")
    print(" 1 - Busca por ID do animal")
    print(" 2 - Buscar por Tipo dos animais")
    print(" 3 - Buscar por status")
    print(" 4 - Verificar animais à venda")
    print(" 0 - Sair da busca")
    print("=" * 60)
    op = int(input("-> "))
    if op == 1:
        id = input("Digite o ID do animal que deseja buscar: ")
        for animal in cadastro["animais"]:
            if animal["id"] == id:
                print(
                    f'ID: {animal["id"]} | Nome: {animal["nome"]} | Raça: {animal["raça"]} | Tipo: {animal["tipo"]} | Preço: {animal["preco"]} | Status: {animal["status"]}'
                )
                break
        else:
            print(f"Animal ID {id} não encontrado.")
    elif op == 2:
        tipo = input("Digite o tipo do animal que deseja buscar: ")
        animal_encontrado = False
        for animal in cadastro["animais"]:
            if animal["tipo"] == tipo:
                print(
                    f'ID: {animal["id"]} | Nome: {animal["nome"]} | Raça: {animal["raça"]} | Tipo: {animal["tipo"]} | Preço: {animal["preco"]} | Status: {animal["status"]}'
                )
                animal_encontrado = True
        if not animal_encontrado:
            print(f"Animais do tipo {tipo} não encontrados.")
    elif op == 3:
        status = input("Digite o status do animal que deseja buscar: ")
        animal_encontrado = False
        for animal in cadastro["animais"]:
            if animal["status"] == status:
                print(
                    f'ID: {animal["id"]} | Nome: {animal["nome"]} | Raça: {animal["raça"]} | Tipo: {animal["tipo"]} | Preço: {animal["preco"]} | Status: {animal["status"]}'
                )
                animal_encontrado = True
        if not animal_encontrado:
            print(f"Animais com status {status} não encontrados.")
    elif op == 4:
        animais_a_venda = False
        for animal in cadastro["animais"]:
            if animal["preco"] != "Indisponivel":
                print(
                    f'ID: {animal["id"]} | Nome: {animal["nome"]} | Raça: {animal["raça"]} | Gênero: {animal["genero"]} | Tipo: {animal["tipo"]} | Preço: {animal["preco"]} | Status: {animal["status"]} | '
                )
                animais_a_venda = True
        if not animais_a_venda:
            print("Nenhum animal disponível para venda encontrado.")
    elif op == 0:
        print("Saindo da busca...")
        sleep(1.6)
    else:
        print("Opção inválida! Saindo da busca...")
        sleep(1.6)


def editar_animal(cadastro: dict):
    id = input("Digite o ID do animal que deseja editar: ")
    for animal in cadastro["animais"]:
        if animal["id"] == id:
            print(
                f'ID: {animal["id"]} | Nome: {animal["nome"]} | Raça: {animal["raça"]} | Tipo: {animal["tipo"]} | Preço: {animal["preco"]} | Status: {animal["status"]}'
            )
            print(
                "Digite os novos dados do animal (deixe em branco para manter o valor atual):"
            )
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            raça = input("Raça: ")
            peso = float(input("Peso: "))
            tipo = input("Tipo: ")
            genero = input("Gênero: ")
            status = input("Status: ")

            op = input("O animal está disponível para venda? (S/N): ").upper()
            if op == "S":
                preco = float(input("Digite o preço do animal: "))
            else:
                preco = "Indisponivel"

            if nome:
                animal["nome"] = nome
            if idade:
                animal["idade"] = idade
            if raça:
                animal["raça"] = raça
            if peso:
                animal["peso"] = peso
            if tipo:
                animal["tipo"] = tipo
            if genero:
                animal["genero"] = genero
            if status:
                animal["status"] = status
            animal["preco"] = preco

            print(f"Animal ID {id} atualizado com sucesso!")


def excluir_animal(cadastro: dict):
    id = input("Qual animal deseja excluir? (Digite o ID): ")
    for animal in cadastro["animais"]:
        if animal["id"] == id:
            print(f"Você tem certeza que deseja excluir o animal ID {id}? (S/N)")
            confirmacao = input("-> ").upper()
            if confirmacao == "S":
                cadastro["animais"].remove(animal)
                print(f"Animal ID {id} excluído com sucesso!")
                break
            else:
                print("Exclusão cancelada.")
                break
    else:
        print(f"Animal ID {id} não encontrado.")

def permitir_pedidos(pedido_de_compra: dict, usuario_logado: dict):
                while True:
                    menus.mostrar_cabecalho_tela('PEDIDOS DE COMPRA')
                    print(f"Que pedido deseja visualizar, {usuario_logado['nome']}?")
                    print(
                        "1 - Visualizar Pedidos em Aguardo\n"
                        "2 - Visualizar Pedidos Confirmados\n"
                        "3 - Visualizar Pedidos Recusados\n"
                        "0 - Sair"
                    )

                    op = int(input("-> "))
                    if op > 3 or op < 0:
                        print("Opção Inválida!")
                        continue
                    if op == 0:
                        break

                    elif op == 1:

                        pedidos_aguardo = []

                        for indice, pedido in enumerate(pedido_de_compra["pedidos"]):

                            if pedido["status_pedido"] == "Aguardo":

                                pedidos_aguardo.append(indice)

                                data = pedido["criado_em"][0]

                                print(
                                    f"[{len(pedidos_aguardo)-1}] "
                                    f"NOME: {pedido['nome_cliente']} | "
                                    f"PRODUTO: {pedido['nome_produto']} | "
                                    f"ID PRODUTO: {pedido['item_id']} | "
                                    f"QUANTIDADE: {pedido['quantidade']} | "
                                    f"STATUS: {pedido['status_pedido']} | "
                                    f"CRIADO EM: "
                                    f"{data['ano']}/{str(data['mes']).zfill(2)}/{str(data['dia']).zfill(2)} "
                                    f"{str(data['hora']).zfill(2)}:{str(data['minuto']).zfill(2)}"
                                )

                        if len(pedidos_aguardo) == 0:
                            print("Não há pedidos aguardando aprovação.")
                            continue

                        escolha = int(input("\nDigite o índice do pedido que deseja analisar: "))

                        if escolha < 0 or escolha >= len(pedidos_aguardo):
                            print("Pedido inválido!")
                            continue

                        indice_real = pedidos_aguardo[escolha]

                        print("\n1 - Confirmar Pedido\n" "2 - Recusar Pedido\n" "0 - Cancelar")

                        decisao = int(input("-> "))

                        if decisao == 1:
                            pedido_de_compra["pedidos"][indice_real]["status_pedido"] = "Confirmado"
                            print("Pedido confirmado com sucesso!")
                            continue

                        elif decisao == 2:
                            pedido_de_compra["pedidos"][indice_real]["status_pedido"] = "Recusado"
                            print("Pedido recusado com sucesso!")
                            continue

                        elif decisao == 0:
                            break

                        else:
                            print("Opção inválida!")
                            continue
                    elif op == 2:
                        for pedido in pedido_de_compra["pedidos"]:
                            if pedido["status_pedido"] == "Confirmado":
                                print(
                                    f"NOME: {pedido['nome_cliente']} | "
                                    f"PRODUTO: {pedido['nome_produto']} | "
                                    f"ID PRODUTO: {pedido['item_id']} | "
                                    f"QUANTIDADE: {pedido['quantidade']} | "
                                    f"STATUS: {pedido['status_pedido']} | "
                                    f"CRIADO EM: "
                                    f"{data['ano']}/{str(data['mes']).zfill(2)}/{str(data['dia']).zfill(2)} "
                                    f"{str(data['hora']).zfill(2)}:{str(data['minuto']).zfill(2)}"
                                )
                    elif op == 3:
                        for pedido in pedido_de_compra["pedidos"]:
                            if pedido["status_pedido"] == "Recusado":
                                print(
                                    f"NOME: {pedido['nome_cliente']} | "
                                    f"PRODUTO: {pedido['nome_produto']} | "
                                    f"ID PRODUTO: {pedido['item_id']} | "
                                    f"QUANTIDADE: {pedido['quantidade']} | "
                                    f"STATUS: {pedido['status_pedido']} | "
                                    f"CRIADO EM: {data['ano']}/{str(data['mes']).zfill(2)}/{str(data['dia']).zfill(2)} {str(data['hora']).zfill(2)}:{str(data['minuto']).zfill(2)}"
                                    
                                    
                                )
