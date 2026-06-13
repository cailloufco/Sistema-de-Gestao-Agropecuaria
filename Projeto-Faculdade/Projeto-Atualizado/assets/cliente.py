from datetime import datetime
from assets import menus


def realizar_compra(cadastro: dict, usuario_logado: dict):
    menus.mostrar_cabecalho_tela("COMPRAR")
    print(f"O que você deseja comprar, {usuario_logado['nome']}?\n")
    print(" 1 - Comprar um animal")
    print(" 2 - Comprar um produto")
    print(" 0 - Sair")
    print("=" * 60)
    op = int(input("-> "))
    if op == 1:
        print("Digite o ID do animal que deseja comprar: ")
        id = input("-> ")
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
                if produto["status"] != "Indisponivel" and produto["quantidade"] != 0:
                    print(
                        f'ID: {produto["id"]} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]} | Status: {produto["status"]}'
                    )
                    print("Deseja confirmar a compra? (S/N)")
                    confirmacao = input("-> ").upper()
                    if confirmacao == "S":
                        quantidade_comprada = int(
                            input("Digite a quantidade que deseja comprar: ")
                        )
                        if quantidade_comprada <= 0:
                            print("Quantidade inválida. A compra foi cancelada.")
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
                    print("Produto não disponível para venda ou sem estoque.")
        else:
            print(f"Produto ID {id} não encontrado.")


def vizualizar_estoque(cadastro: dict, usuario_logado: dict):
    menus.mostrar_cabecalho_tela("ESTOQUE")
    print(f"O que você deseja ver, {usuario_logado['nome']}?\n")
    print(" 1 - Visualizar Estoque de Animais à Venda")
    print(" 2 - Visualizar Estoque de Produtos")
    print(" 0 - Sair")
    print("=" * 60)
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
                if produto["status"] != "Indisponivel" and produto["quantidade"] != 0:
                    print(
                        f'ID: {produto["id"]} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]} | Status: {produto["status"]}'
                    )
                    produto_disponivel = True
            if not produto_disponivel:
                print("Nenhum produto disponível para venda encontrado.")
        else:
            print("Nenhum produto cadastrado.")


def agendar_retirada(cadastro: dict, usuario_logado: dict, agendamento: dict):
    menus.mostrar_cabecalho_tela("AGENDAR RETIRADA")
    print(f"Agendar Retirada/Transporte, {usuario_logado['nome']}?\n")
    print(" 1 - Agendar Retirada de Animais")
    print(" 2 - Agendar Retirada de Produtos")
    print(" 0 - Sair")
    print("=" * 60)
    op = int(input("-> "))
    if op == 1:

        nome_cliente = usuario_logado["nome"]
        tipo = "Animal"
        item_id = input("Digite o ID do animal que deseja agendar a retirada: ")
        animal_encontrado = False

        for animal in cadastro["animais"]:
            if animal["id"] == item_id and animal["preco"]:
                print(
                    f'ID: {animal["id"]} | Nome: {animal["nome"]} | Raça: {animal["raça"]} | Tipo: {animal["tipo"]} | Preço: {animal["preco"]} | Status: {animal["status"]}'
                )
                animal_encontrado = True
                animal_nome = animal["nome"]
                break

        if not animal_encontrado:
            print(f"O animal com ID {item_id} não existe")
            return
        if animal_encontrado:
            print("Deseja confirmar o agendamento da retirada desse animal? (S/N)")
            confirmacao = input("-> ").upper()
            if confirmacao != "S":
                print("Agendamento cancelado.")
                return
            while True:

                print("Digite o dia da retirada do animal:")
                dia = int(input("-> "))

                print("Digite o mês da retirada do animal:")
                mes = int(input("-> "))

                if mes < 1 or mes > 12:
                    print("Mês inválido!")
                    print("Tente novamente!")
                    continue
                else:

                    print("Digite o ano da retirada do animal:")
                    ano = int(input("-> "))

                    if dia < 1 or dia > 31:
                        print("Dia inválido!")
                        print("Tente novamente!")
                        continue

                    elif ano < datetime.now().year:
                        print("Ano inválido!")
                        print("Tente novamente!")
                        continue

                    elif ano == datetime.now().year and mes < datetime.now().month:
                        print("Data inválida!")
                        print("Tente novamente!")
                        continue

                    elif (
                        ano == datetime.now().year
                        and mes == datetime.now().month
                        and dia < datetime.now().day
                    ):
                        print("Data inválida!")
                        print("Tente novamente!")
                        continue

                    hora_atual = datetime.now().hour
                    minuto_atual = datetime.now().minute

                    print("Digite o horário da retirada ( HH:MM ) : ")
                    partes = input("-> ").split(":")

                    if len(partes) != 2:
                        print("formato inválido")
                        continue
                    hora = int(partes[0])
                    minuto = int(partes[1])

                    if minuto_atual > minuto:
                        print("horario inválido")
                        print("Tente novamente!")
                        continue
                    if hora_atual > hora:
                        print("horario inválido")
                        print("Tente novamente!")
                        continue
                    if hora > 23 or hora < 0:
                        print("horario inválido")
                        print("Tente novamente!")
                        continue
                    if minuto > 59 or minuto < 0:
                        print("horario inválido")
                        print("Tente novamente!")
                        continue

                    data = f"{ano}-{mes}-{dia}"
                    hora_data = {hora} - {minuto}

                    break

            cadastro_agendamento = {
                "nome": animal_nome,
                "nome_cliente": nome_cliente,
                "tipo": tipo,
                "item_id": item_id,
                "data": data,
                "hora": hora_data,
                "status": "Agendado",
                "data_agendamento": [
                    datetime.now().strftime("%Y-%m-%d"),
                    datetime.now().strftime("%H:%M:%S"),
                ],
            }
            agendamento["animais"].append(cadastro_agendamento)
            print(
                f"Retirada do animal ID {item_id} agendada para {data} às {hora_data}."
            )

    elif op == 2:
        nome_cliente = usuario_logado["nome"]
        tipo = "Produto"
        item_id = input("Digite o ID do animal que deseja agendar a retirada: ")
        produto_encontrado = False
        produto_nome = ""
        for produto in cadastro["produtos"]:
            if produto["id"] == item_id and produto["preco"]:
                print(
                    f'ID: {produto["id"]} | Nome: {produto["nome"]} | Raça: {produto["quantidade"]} | Preço: {produto["preco"]} | Status: {produto["status"]}'
                )
                produto_nome = produto["nome"]
                produto_encontrado = True
                break
        print("Quantos Quilogramas ou Litros você deseja retirar? ")
        quantia = float(input("->"))
        produto_encontrado = False
        for produto in cadastro["produtos"]:
            if produto["id"] == item_id:
                if quantia > produto["quantidade"]:
                    print("Estoque insuficiente")
                    print(
                        f"Quantidade solicitada ({quantia}) excede o estoque disponível ({produto['quantidade']})."
                    )
                produto_encontrado = True
                break

        if not produto_encontrado:
            print(f"O produto com ID {item_id} não existe")
            return
        if produto_encontrado:
            print("Deseja confirmar o agendamento da retirada desse produto? (S/N)")
            confirmacao = input("-> ").upper()
            if confirmacao != "S":
                print("Agendamento cancelado.")
                return
            while True:

                dia = int(input("-> "))

                print("Digite o mês da retirada do produto:")
                mes = int(input("-> "))

                if mes < 1 or mes > 12:
                    print("Mês inválido!")
                    print("Tente novamente!")
                    continue
                else:

                    print("Digite o ano da retirada do produto:")
                    ano = int(input("-> "))

                    if dia < 1 or dia > 31:
                        print("Dia inválido!")
                        print("Tente novamente!")
                        continue

                    elif ano < datetime.now().year:
                        print("Ano inválido!")
                        print("Tente novamente!")
                        continue

                    elif ano == datetime.now().year and mes < datetime.now().month:
                        print("Data inválida!")
                        print("Tente novamente!")
                        continue

                    elif (
                        ano == datetime.now().year
                        and mes == datetime.now().month
                        and dia < datetime.now().day
                    ):
                        print("Data inválida!")
                        print("Tente novamente!")
                        continue

                    hora_atual = datetime.now().hour
                    minuto_atual = datetime.now().minute

                    print("Digite o horário da retirada ( HH:MM ) : ")
                    partes = input("-> ").split(":")

                    if len(partes) != 2:
                        print("formato inválido")
                        continue
                    hora = int(partes[0])
                    minuto = int(partes[1])

                    if minuto_atual > minuto:
                        print("horario inválido")
                        print("Tente novamente!")
                        continue
                    if hora_atual > hora:
                        print("horario inválido")
                        print("Tente novamente!")
                        continue
                    if hora > 23 or hora < 0:
                        print("horario inválido")
                        print("Tente novamente!")
                        continue
                    if minuto > 59 or minuto < 0:
                        print("horario inválido")
                        print("Tente novamente!")
                        continue

                    data = f"{ano}-{mes}-{dia}"
                    hora_data = {hora} - {minuto}

                    break

            cadastro_agendamento = {
                "nome": produto_nome,
                "nome_cliente": nome_cliente,
                "tipo": tipo,
                "item_id": item_id,
                "quantidade": quantia,
                "data": data,
                "hora": hora_data,
                "status": "Agendado",
                "data_agendamento": [
                    datetime.now().strftime("%Y-%m-%d"),
                    datetime.now().strftime("%H:%M:%S"),
                ],
            }
            agendamento["produtos"].append(cadastro_agendamento)
            print(
                f"Retirada do produto ID {item_id} agendada para {data} às {hora_data}."
            )


def ver_agendamento(usuario_logado: dict, cadastro: dict, agendamento: dict):
    while True:
        print(
            f"Olá , {usuario_logado['nome']} , Seus Agendamentos\n1 - Agendamento de Animais\n2 - Agendamento de Produtos\n0 - Sair"
        )
        op = int(input("-> "))
        encontrado = False
        if op == 1:
            """{
                "nome": nome_produto
                "nome_cliente": nome_cliente,
                "tipo": tipo,
                "item_id": item_id,
                "quantidade": quantia,
                "data": data,
                "hora": hora_data,
                "status": "Agendado",
                "data_agendamento": [
                    datetime.now().strftime("%Y-%m-%d"),
                    datetime.now().strftime("%H:%M:%S"),
                ]
            }"""
            for produto in agendamento["produto"]:
                if produto["nome_cliente"] == usuario_logado["nome"]:
                    print(
                        f'ID: {produto["item_id"]} | Tipo: {produto["tipo"]} | Nome: {produto["nome"]} | Quantidade: {produto["quantia"]} | Dia da Coleta: {produto['data']} | Status: {produto["status"]} | Criado : {produto["data_agendamento"][0]} , {produto["data_agendamento"][1]}'
                    )
                    encontrado = True
            if not encontrado:
                print(
                    f"{usuario_logado['nome']} , agendamento não encontrado ou não existente"
                )
        # so pra me localizar , tenho q fazer a busca de agendamentos pelos animais pq pelo produto ta feito

        if op == 2:
            for animal in agendamento["animais"]:
                if animal["nome_cliente"] == usuario_logado["nome"]:
                    print(
                        f'ID: {animal["item_id"]} | Tipo: {animal["tipo"]} | Nome: {animal["nome"]} | Quantidade: {animal["quantia"]} | Dia da Coleta: {animal['data']} | Status: {animal["status"]} | Criado : {animal["data_agendamento"][0]} , {animal["data_agendamento"][1]}'
                    )
                    encontrado = True
            if not encontrado:
                print(
                    f"{usuario_logado['nome']} , agendamento não encontrado ou não existente"
                )

def pedido_de_compra(
                pedido_de_compra: dict, usuario_logado: dict, cadastro: dict
            ):
                while True:
                    print(
                        f"Olá , {usuario_logado['nome']}! Deseja realizar um pedido de compra de um PRODUTO? ( S / N )"
                    )
                    op = input("->").upper()
                    if op == "S":
                        print("Digite o ID do PRODUTO que deseja realizar um pedido")
                        id = int(input("->"))
                        nome_produto = None
                        achado = False
                        for produto in cadastro["produtos"]:
                            if (
                                produto["id"] == id
                                and produto["status"] != "Indisponivel"
                            ):
                                print(
                                    f'ID: {produto["id"]} | Nome: {produto["nome"]} | Quantidade: {produto["quantidade"]} | Preço: {produto["preco"]} | Status: {produto["status"]}'
                                )
                                nome_produto = produto["nome"]
                                produto_id = produto["id"]
                                quantidade = produto["quantidade"]

                                achado = True
                                break
                        if not achado:
                            print("Produto não disponível para venda ou sem estoque.")
                            break
                        quando_criado = [
                            {
                                "ano": datetime.now().year,
                                "mes": datetime.now().month,
                                "dia": datetime.now().day,
                                "hora": datetime.now().hour,
                                "minuto": datetime.now().minute,
                            }
                        ]
                        pedido = {
                            "nome_cliente": usuario_logado["nome"],
                            "nome_produto": nome_produto,
                            "item_id": produto_id,
                            "status_pedido": "Aguardo",
                            "criado_em": quando_criado,
                            "quantidade": quantidade,
                        }
                        pedido_de_compra["pedidos"].append(pedido)
                    else:
                        print("Saindo...")
                        break

def exibir_pedidos(pedidos: dict, usuario_logado: dict):
                print(f"Olá , {usuario_logado['nome']} , Seus Pedidos:")
                achado = False
                for pedido in pedidos["pedidos"]:
                    if pedido["nome_cliente"] == usuario_logado["nome"]:
                        print(
                            f"ID : {pedido['item_id']}  | Produto Pedido: {pedido['nome_produto']} | Quantidade : {pedido['quantidade']}  | Status : {pedido['status_pedido']} | Criado em: {pedido['criado_em'][0]}/{pedido['criado_em'][1]}/{pedido['criado_em'][2]} , {pedido['criado_em'][3]}-{pedido['criado_em'][4]}"
                        )
                    achado = True
                if not achado:
                    print(f'{usuario_logado["nome"]} , Nenhum Pedido Realizado!')
                    return
