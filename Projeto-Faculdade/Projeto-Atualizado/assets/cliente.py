from datetime import datetime
from assets import menus

from rich import print
from rich.table import Table
from rich.console import Console
from rich import box


def realizar_compra(cadastro: dict, usuario_logado: dict, registro_de_auditoria: list):
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
        console = Console()
        table = Table(title="Compra de Animal")
        table.add_column("ID")
        table.add_column("NOME")
        table.add_column("RAÇA")
        table.add_column("TIPO")
        table.add_column("PREÇO")
        table.add_column("STATUS")
        for animal in cadastro["animais"]:
            if animal["id"] == id:
                if animal["preco"] != "Indisponivel":
                    table.add_row(
                        str(animal["id"]),
                        animal["nome"],
                        animal["raça"],
                        animal["tipo"],
                        str(animal["preco"]),
                        animal["status"],
                    )
                    console.print(table)

                    print("Deseja confirmar a compra? (S/N)")
                    confirmacao = input("-> ").upper()
                    if confirmacao == "S":
                        cadastro["animais"].remove(animal)
                        print(f"Compra do animal ID [bold yellow]{id}[/] confirmada!")
                        registro_de_auditoria(
                            f'O cliente {usuario_logado["nome"]} , comprou o animal ID {id} ,  {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
                        )
                        break
                    else:
                        print("Compra cancelada.")
                        break
                else:
                    print(f"Animal ID [bold yellow]{id}[/] não disponível para venda.")
                    break
        else:
            print(f"Animal ID [bold yellow]{id}[/] não encontrado.")

    elif op == 2:
        print("Digite o ID do produto que deseja comprar: ")
        id = int(input("-> "))

        console = Console()
        table = Table(title="Compra de Produto")
        table.add_column("ID")
        table.add_column("NOME")
        table.add_column("QUANTIDADE")
        table.add_column("PREÇO")
        table.add_column("STATUS")

        for produto in cadastro["produtos"]:
            if produto["id"] == id:
                if produto["status"] != "Indisponivel" and produto["quantidade"] != 0:
                    table.add_row(
                        str(produto["id"]),
                        produto["nome"],
                        str(produto["quantidade"]),
                        str(produto["preco"]),
                        produto["status"],
                    )
                    console.print(table)
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
                                f"Compra de {quantidade_comprada} unidades do produto ID [bold yellow]{id}[/] confirmada!"
                            )
                            registro_de_auditoria(
                                f'O cliente {usuario_logado["nome"]} , comprou o produto ID: {id} - Quantia: {quantidade_comprada} ,  {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
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
            print(f"Produto ID [bold yellow]{id}[/] não encontrado.")


def vizualizar_estoque(
    cadastro: dict, usuario_logado: dict, registro_de_auditoria: list
):
    menus.mostrar_cabecalho_tela("ESTOQUE")
    print(f"O que você deseja ver, {usuario_logado['nome']}?\n")
    print(" 1 - Visualizar Estoque de Animais à Venda")
    print(" 2 - Visualizar Estoque de Produtos")
    print(" 0 - Sair")
    print("=" * 60)
    op = int(input("-> "))
    if op == 1:
        achou = False
        if cadastro["animais"]:
            console = Console()
            table = Table(title="Retirada de Animal")
            table.add_column("ID")
            table.add_column("NOME")
            table.add_column("RAÇA")
            table.add_column("TIPO")
            table.add_column("PREÇO")
            table.add_column("STATUS")
            for animal in cadastro["animais"]:
                if animal["preco"] != "Indisponivel":

                    table.add_row(
                        str(animal["id"]),
                        animal["nome"],
                        animal["raça"],
                        animal["tipo"],
                        str(animal["preco"]),
                        animal["status"],
                    )

                    achou = True
            if achou:
                console.print(table)
                registro_de_auditoria(
                    f'O cliente {usuario_logado["nome"]} , visualizou todos os animais a venda ,  {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
                )
            if not achou:
                print("Nenhum animal disponível para venda encontrado.")

        else:
            print("Nenhum animal cadastrado.")

    elif op == 2:
        console = Console()
        table = Table(title="Retirada de Animal")
        table.add_column("ID")
        table.add_column("NOME")
        table.add_column("QUANTIDADE")
        table.add_column("PREÇO")
        table.add_column("STATUS")
        produto_disponivel = False
        if cadastro["produtos"]:
            for produto in cadastro["produtos"]:
                if produto["status"] != "Indisponivel" and produto["quantidade"] != 0:
                    table.add_row(
                        str(produto["id"]),
                        produto["nome"],
                        str(produto["quantidade"]),
                        str(produto["preco"]),
                        produto["status"],
                    )

                    produto_disponivel = True
            if produto_disponivel:
                console.print(table)
                registro_de_auditoria(
                    f'O cliente {usuario_logado["nome"]} , visualizou todos os produtos a venda ,  {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
                )
            if not produto_disponivel:
                print("Nenhum produto disponível para venda encontrado.")
        else:
            print("Nenhum produto cadastrado.")


def agendar_retirada(
    cadastro: dict, usuario_logado: dict, agendamento: dict, registro_de_auditoria: list
):
    while True:
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
            console = Console()
            table = Table(title="Retirada de Animal")
            table.add_column("ID")
            table.add_column("NOME")
            table.add_column("RAÇA")
            table.add_column("PESO")
            table.add_column("PREÇO")
            table.add_column("STATUS")

            for animal in cadastro["animais"]:
                if animal["id"] == item_id and animal["preco"]:

                    table.add_row(
                        str(animal["id"]),
                        animal["nome"],
                        animal["raça"],
                        str(animal["peso"]),
                        str(animal["preco"]),
                        animal["status"],
                    )

                    animal_encontrado = True
                    animal_nome = animal["nome"]
                    break

            if not animal_encontrado:
                print(f"O animal com ID {item_id} não existe")
                continue
            if animal_encontrado:
                console.print(table)
                print("Deseja confirmar o agendamento da retirada desse animal? (S/N)")
                confirmacao = input("-> ").upper()
                if confirmacao != "S":
                    print("Agendamento cancelado.")
                    continue
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
                        hora_data = f"{hora}:{minuto}"

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
                registro_de_auditoria.append(
                    f'o cliente {usuario_logado["nome"]} agendou retirada às {datetime.now().strftime("%d/%m/%Y às %H:%M")} do animal {animal_nome}'
                )
        elif op == 2:
            nome_cliente = usuario_logado["nome"]
            tipo = "Produto"
            item_id = int(
                input("Digite o ID do produto que deseja agendar a retirada: ")
            )
            produto_encontrado = False
            produto_nome = ""

            console = Console()
            table = Table(title="Retirada de Produto")
            table.add_column("ID")
            table.add_column("NOME")
            table.add_column("QUANTIDADE")
            table.add_column("PREÇO")
            table.add_column("STATUS")

            for produto in cadastro["produtos"]:
                if produto["id"] == item_id and produto["preco"]:

                    table.add_row(
                        str(produto["id"]),
                        produto["nome"],
                        str(produto["quantidade"]),
                        str(produto["preco"]),
                        produto["status"],
                    )

                    produto_nome = produto["nome"]
                    produto_encontrado = True
                    break
            if not produto_encontrado:
                print("Produto [bold red]NÃO[/] encontrado")
            if produto_encontrado:
                print("Quantos Quilogramas ou Litros você deseja retirar? ")
                quantia = float(input("->"))
                produto_encontrado = False
                nome_produto = ""
                for produto in cadastro["produtos"]:
                    if produto["id"] == item_id:
                        if quantia > produto["quantidade"]:
                            print("Estoque insuficiente")
                            print(
                                f"Quantidade solicitada ({quantia}) excede o estoque disponível ({produto['quantidade']})."
                            )
                        produto_encontrado = True
                        nome_produto = produto["nome"]
                        break

                if not produto_encontrado:
                    print(f"O produto com ID {item_id} não existe")
                    return
                if produto_encontrado:
                    print(
                        "Deseja confirmar o agendamento da retirada desse produto? (S/N)"
                    )
                    confirmacao = input("-> ").upper()
                    if confirmacao != "S":
                        print("Agendamento cancelado.")
                        continue

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
                        hora_data = f"{hora}:{minuto}"

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
                agendamento["produto"].append(cadastro_agendamento)
                print(
                    f"Retirada do produto ID {item_id} agendada para {data} às {hora_data}."
                )
                registro_de_auditoria.append(
                    f'o cliente {usuario_logado["nome"]} agendou retirada às {datetime.now().strftime("%d/%m/%Y às %H:%M")} do produto {nome_produto}'
                )


def ver_agendamento(
    usuario_logado: dict, agendamento: dict, registro_de_auditoria: list
):
    while True:
        print(
            f"Olá , {usuario_logado['nome']} , Seus Agendamentos\n1 - Agendamento de Animais\n2 - Agendamento de Produtos\n0 - Sair"
        )
        op = int(input("-> "))
        encontrado = False
        if op == 0:
            break
        if op == 1:
            console = Console()
            table = Table(title="[bold italic]Ver Agendamento[/]")
            table.add_column("ID")
            table.add_column("NOME")
            table.add_column("TIPO")
            table.add_column("HORA")
            table.add_column("DIA DA COLETA")
            table.add_column("STATUS")
            table.add_column("CRIADO EM")
            for animal in agendamento["animais"]:
                if animal["nome_cliente"] == usuario_logado["nome"]:

                    table.add_row(
                        str(animal["item_id"]),
                        animal["nome"],
                        animal["tipo"],
                        animal["hora"],
                        animal["data"],
                        animal["status"],
                        animal["data_agendamento"][0]
                        + " "
                        + animal["data_agendamento"][1],
                    )

                    encontrado = True
            if encontrado:
                console.print(table)
                registro_de_auditoria.append(
                    f'o cliente {usuario_logado["nome"]} procurou por seus agendamentos às {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
                )
            if not encontrado:
                print(
                    f"{usuario_logado['nome']} , agendamento não encontrado ou não existente"
                )
        # so pra me localizar , tenho q fazer a busca de agendamentos pelos animais pq pelo produto ta feito

        if op == 2:
            console = Console()
            table = Table(title="[bold italic]Agendamento de Produtos[/]")
            table.add_column("ID")
            table.add_column("NOME")
            table.add_column("TIPO")
            table.add_column("QUANTIDADE")
            table.add_column("DIA DA COLETA")
            table.add_column("STATUS")
            table.add_column("CRIADO EM")
            for produto in agendamento["produto"]:
                if produto["nome_cliente"] == usuario_logado["nome"]:

                    table.add_row(
                        str(produto["item_id"]),
                        produto["nome"],
                        produto["tipo"],
                        str(produto["quantidade"]),
                        produto["data"],
                        produto["status"],
                        produto["data_agendamento"][0]
                        + " "
                        + produto["data_agendamento"][1],
                    )

                    encontrado = True
            if encontrado:
                console.print(table)
                registro_de_auditoria.append(
                    f'o cliente {usuario_logado["nome"]} procurou por seus agendamentos às {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
                )
            if not encontrado:
                print(
                    f"{usuario_logado['nome']} , agendamento não encontrado ou não existente"
                )


def pedido_de_compra(
    pedido_de_compra: dict,
    usuario_logado: dict,
    cadastro: dict,
    registro_de_auditoria: list,
):
    while True:
        print(
            f"Olá , {usuario_logado['nome']}! Deseja realizar um pedido de compra de um PRODUTO? ( S / N )"
        )
        op = input("->").upper()
        if op == "S":
            print("Digite o ID do PRODUTO que deseja realizar um pedido")

            print("[bold blue]->[/]", end="")
            id = int(input(" "))

            nome_produto = None
            produto_id = None
            quantidade = None

            achado = False
            console = Console()
            table = Table(title="[bold italic]Produtos Encontrados[/]")
            table.add_column("ID")
            table.add_column("PRODUTO")
            table.add_column("QUANTIDADE")
            table.add_column("PREÇO")
            table.add_column("STATUS")

            for produto in cadastro["produtos"]:
                if produto["id"] == id and produto["status"] != "Indisponivel":

                    table.add_row(
                        str(produto["id"]),
                        produto["nome"],
                        str(produto["quantidade"]),
                        str(produto["preco"]),
                        produto["status"],
                    )

                    nome_produto = produto["nome"]
                    produto_id = produto["id"]
                    quantidade = produto["quantidade"]

                    achado = True
                    break

            if not achado:
                print("Produto não disponível para venda ou sem estoque.")
                break
            if achado:

                console.print(table)

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

                registro_de_auditoria.append(
                    f'o cliente {usuario_logado["nome"]} criou um pedido de compra às {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
                )

        else:
            print("Saindo...")
            break


def exibir_pedidos(pedidos: dict, usuario_logado: dict, registro_de_auditoria):
    print(f"Olá , {usuario_logado['nome']} , Seus Pedidos:")

    achado = False

    console = Console()
    table = Table(title="[bold italic]Seus Pedidos[/]")
    table.add_column("ID")
    table.add_column("NOME")
    table.add_column("QUANTIDADE")
    table.add_column("STATUS")
    table.add_column("CRIADO EM")
    for pedido in pedidos["pedidos"]:

        if pedido["nome_cliente"] == usuario_logado["nome"]:
            data = pedido["criado_em"][0]
            table.add_row(
                str(pedido["item_id"]),
                pedido["nome_produto"],
                str(pedido["quantidade"]),
                pedido["status_pedido"],
                f"{data['ano']}/{data['mes']}/{data['dia']}",
            )

            achado = True

    if achado:
        console.print(table)
        registro_de_auditoria.append(
            f'o cliente {usuario_logado["nome"]}exibiu seus pedidos de compra às {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
        )
    if not achado:
        print("Nenhum Pedido Encontrado!")
