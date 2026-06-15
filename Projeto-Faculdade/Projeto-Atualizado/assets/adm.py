from datetime import datetime

from assets import menus

from time import sleep

from rich import print
from rich.table import Table
from rich.console import Console
from rich import box


def cadastrar_produto(
    cadastro: dict, registro_de_auditoria: list, usuario_logado: dict
):
    while True:
        ids_existentes = [produto["id"] for produto in cadastro["produtos"]]
        id = max(ids_existentes) + 1

        nome = input("Nome: ")
        quantidade = int(input("Quantidade: "))
        print("O produto está disponível para venda? (S/N): ")

        print("[bold blue]->[/]", end="")
        op = input(" ").upper()
        if op == "S":
            status = "Disponível"
            preco = float(input("Preço: "))
        else:
            preco = float(input("Preço: "))
            status = "Indisponivel"

        produto = {
            "id": id,
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco,
            "status": status,
        }
        cadastro["produtos"].append(produto)
        print(f"Produto ID [bold yellow]{id}[/] cadastrado com sucesso!")

        registro_de_auditoria.append(
            f"O produto {id} foi cadastrado por {usuario_logado["nome"]} {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
        )

        print("Deseja cadastrar outro produto? ( S - N )" "\n[bold blue]->[/]", end="")
        escolha = input(" ").upper()
        if escolha != "S":
            break


def buscar_produto(cadastro: dict, usuario_logado: dict, registro_de_auditoria: list):
    while True:
        menus.mostrar_cabecalho_tela("BUSCA DE PRODUTOS")
        print(f"O que você deseja buscar, {usuario_logado['nome']}?\n")
        print(" 1 - Busca por ID do produto")
        print(" 2 - Buscar por nome dos produtos")
        print(" 3 - Buscar por status")
        print(" 4 - Verificar produtos disponíveis para venda")
        print(" 5 - Exibir todos os produtos cadastrados")
        print(" 0 - Sair da busca")
        print("=" * 60)

        print("[bold blue]->[/]", end="")
        op = int(input(" "))
        if op == 1:
            id = int(input("Digite o ID do produto que deseja buscar: "))
            achou = False
            for produto in cadastro["produtos"]:
                if produto["id"] == id:
                    console = Console()
                    table = Table(
                        title="[bold italic]Remover Animal[/]", box=box.DOUBLE
                    )
                    table.add_column("ID")
                    table.add_column("NOME")
                    table.add_column("QUANTIDADE")
                    table.add_column("PREÇO")
                    table.add_column("STATUS")

                    table.add_row(
                        str(produto["id"]),
                        produto["nome"],
                        str(produto["quantidade"]),
                        str(produto["preco"]),
                        produto["status"],
                    )
                    console.print(table)
                    achou = True

                    registro_de_auditoria.append(
                        f"O usuário {usuario_logado["nome"]} buscou pelo produto ID {produto["id"]} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
                    )

                    break

            else:
                print(f"Produto ID [bold yellow]{id}[/][red]NÃO[/] encontrado.")

        elif op == 2:
            nome = input("Digite o nome do produto que deseja buscar: ")
            produto_encontrado = False
            for produto in cadastro["produtos"]:
                if produto["nome"] == nome:
                    console = Console()
                    table = Table(title="[bold italic]Remover Animal[/]")
                    table.add_column("ID")
                    table.add_column("NOME")
                    table.add_column("QUANTIDADE")
                    table.add_column("PREÇO")
                    table.add_column("STATUS")

                    table.add_row(
                        str(produto["id"]),
                        produto["nome"],
                        str(produto["quantidade"]),
                        str(produto["preco"]),
                        produto["status"],
                    )
                    console.print(table)
                    produto_encontrado = True
                    registro_de_auditoria.append(
                        f"O usuario {usuario_logado["nome"]} buscou pelo produto de nome {produto["nome"]} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
                    )
            if not produto_encontrado:
                print(
                    f"Produto com nome [bold yellow]{nome}[/] [red]NÃO[/] encontrados."
                )
                break
        elif op == 3:
            status = input("Digite o status do produto que deseja buscar: ")
            produto_encontrado = False
            console = Console()
            table = Table(title="[bold italic]Remover Animal[/]")
            table.add_column("ID")
            table.add_column("NOME")
            table.add_column("QUANTIDADE")
            table.add_column("PREÇO")
            table.add_column("STATUS")
            for produto in cadastro["produtos"]:

                if produto["status"] == status:

                    table.add_row(
                        str(produto["id"]),
                        produto["nome"],
                        str(produto["quantidade"]),
                        str(produto["preco"]),
                        produto["status"],
                    )

                    produto_encontrado = True
            if produto_encontrado:
                registro_de_auditoria.append(
                    f'O usuario {usuario_logado["nome"]} pesquisou pelo produto com status "{status}" , {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
                )
                console.print(table)

            if not produto_encontrado:
                print(
                    f"Produtos com status [bold yellow]{status}[/] [red]NÃO[/] encontrados."
                )
        elif op == 4:
            produtos_disponiveis = False
            for produto in cadastro["produtos"]:
                if produto["preco"] != "Indisponivel":
                    console = Console()
                    table = Table(title="[bold italic]Remover Animal[/]")
                    table.add_column("ID")
                    table.add_column("NOME")
                    table.add_column("QUANTIDADE")
                    table.add_column("PREÇO")
                    table.add_column("STATUS")

                    table.add_row(
                        str(produto["id"]),
                        produto["nome"],
                        str(produto["quantidade"]),
                        str(produto["preco"]),
                        produto["status"],
                    )
                    console.print(table)
                    produtos_disponiveis = True
            registro_de_auditoria.append(
                f'O usuario {usuario_logado["nome"]} buscou todos os produtos Indisponíveis , {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
            )
            if not produtos_disponiveis:
                print("[red]Nenhum[/] produto disponível para venda encontrado.")

        elif op == 5:
            achou = False
            console = Console()
            table = Table(title="[bold italic]Remover Animal[/]")
            table.add_column("ID")
            table.add_column("NOME")
            table.add_column("QUANTIDADE")
            table.add_column("PREÇO")
            table.add_column("STATUS")
            for produto in cadastro["produtos"]:
                table.add_row(
                    str(produto["id"]),
                    produto["nome"],
                    str(produto["quantidade"]),
                    str(produto["preco"]),
                    produto["status"],
                )
                achou = True
            if achou:
                console.print(table)
            else:
                print("nenhum produto cadastrado")
        elif op == 0:
            break
        else:
            print("[bold red]Opção inválida.[/]")


def atualizar_produto(
    cadastro: dict, usuario_logado: dict, registro_de_auditoria: list
):
    id = int(input("Digite o [bold]ID[/] do produto que deseja atualizar: "))
    for produto in cadastro["produtos"]:
        if produto["id"] == id:

            console = Console()
            table = Table(title="[bold italic]Remover Animal[/]")
            table.add_column("ID")
            table.add_column("NOME")
            table.add_column("QUANTIDADE")
            table.add_column("PREÇO")
            table.add_column("STATUS")

            table.add_row(
                str(produto["id"]),
                produto["nome"],
                str(produto["quantidade"]),
                str(produto["preco"]),
                produto["status"],
            )

            console.print(table)

            print(
                "Digite os novos dados do produto (deixe em branco para manter o valor atual):"
            )
            nome = input("Nome do produto: ")
            quantidade = input("Quantidade: ")
            print("O produto está disponível para venda? (S/N): ")

            print("[bold blue]->[/]", end="")
            op = input(" ").upper()
            if op == "S":
                preco = float(input("Preço: "))
            else:
                preco = "Indisponivel"

            status = input("Status: ")

            if nome:
                produto["nome"] = nome
            if quantidade:
                produto["quantidade"] = int(quantidade)
            if status:
                produto["status"] = status
            if preco:
                produto["preco"] = preco

            console = Console()
            table = Table(title="[bold italic]ATUALIZADO![/]")
            table.add_column("ID")
            table.add_column("NOME")
            table.add_column("QUANTIDADE")
            table.add_column("PREÇO")
            table.add_column("STATUS")

            table.add_row(
                str(produto["id"]),
                produto["nome"],
                str(produto["quantidade"]),
                str(produto["preco"]),
                produto["status"],
            )

            console.print(table)

            print(f"Produto ID [bold yellow]{id}[/] atualizado com sucesso!")
            registro_de_auditoria.append(
                f'O usuario {usuario_logado["nome"]} atualizou o produto ID {id} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
            )


def remover_produto(cadastro: dict, usuario_logado: dict, registro_de_auditoria: list):
    id = int(input("Digite o ID do produto que deseja [bold]remover[/]: "))
    for produto in cadastro["produtos"]:
        if produto["id"] == id:

            console = Console()
            table = Table(title="Remover Animal")
            table.add_column("ID")
            table.add_column("NOME")
            table.add_column("QUANTIDADE")
            table.add_column("PREÇO")
            table.add_column("STATUS")

            table.add_row(
                str(produto["id"]),
                produto["nome"],
                str(produto["quantidade"]),
                str(produto["preco"]),
                produto["status"],
            )

            console.print(table)

            print(
                f"\nVocê tem certeza que deseja remover o produto ID [bold yellow]{id}[/]"
            )

            print("[bold blue]->[/]", end="")
            confirmacao = input(" ").upper()
            if confirmacao == "S":

                cadastro["produtos"].remove(produto)
                print(
                    f"Produto ID [bold yellow]{id} [italic red]removido[/] com sucesso!"
                )
                registro_de_auditoria.append(
                    f'o usuario {usuario_logado["nome"]} removeu o produto ID {id} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
                )
                break

            else:
                print("[italic]Remoção cancelada[/].")
                break
    else:
        print(f"Produto ID [bold yellow]{id}[/] [red]NÃO[/] encontrado.")


def cadastrar_racao(cadastro: dict, usuario_logado: dict, registro_de_auditoria: list):
    while True:
        menus.mostrar_cabecalho_tela("GERENCIAR RAÇÃO")
        print(f"Gerenciar Ração, {usuario_logado['nome']}?\n")
        print(" 1 - Cadastrar uma ração")
        print(" 2 - Visualizar Estoque")
        print(" 3 - Atualizar estoque")
        print(" 0 - Sair")
        print("=" * 60)

        print("\n[bold blue]->[/]", end="")
        op = int(input(" "))
        if op > 3 or op < 0:
            print("Opção inválida. Tente novamente.\n")
            continue
        if op == 1:
            ids_existentes = [item["id"] for item in cadastro["racao"]]
            id = max(ids_existentes) + 1

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
            print(
                f"Ração ID [bold yellow]{id}[/] [italic green]cadastrada com sucesso!"
            )
            registro_de_auditoria.append(
                f'O usuario {usuario_logado["nome"]} cadastrou a ração de ID {id} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
            )

        elif op == 2:
            achou = False
            for racao in cadastro["racao"]:
                print(
                    f"ID: {racao['id']} | Nome: {racao['nome']} | Quantidade: {racao['quantidade']} | Limiar: {racao['limiar_de_estoque']} | Função: {racao['funcao']}"
                )
                achou = True
            registro_de_auditoria.append(
                f'O usuario {usuario_logado["nome"]} buscou por todas as rações cadastradas no estoque , {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
            )
            if not achou:
                print("Nenhuma ração cadastrada")
                sleep(1.6)
                continue

        elif op == 3:
            print(f"Digite o ID da Ração que deseja Atualizar")

            print("[bold blue]->[/]", end="")
            id = int(input(" "))
            for racao in cadastro["racao"]:
                console = Console()
                table = Table(title="[bold italic]Atualizar Ração[/]")
                table.add_column("ID")
                table.add_column("NOME")
                table.add_column("QUANTIDADE")
                table.add_column("LIMIAR")
                table.add_column("FUNÇÃO")
                if racao["id"] == id:

                    table.add_row(
                        str(racao["id"]),
                        racao["nome"],
                        str(racao["quantidade"]),
                        str(racao["limiar_de_estoque"]),
                        racao["funcao"],
                    )

                    print(
                        "Digite os novos dados do produto (deixe em branco para manter o valor atual):"
                    )
                    nome = input("Nome do produto: ")
                    quantidade = input("Quantidade: ")
                    limiar = input("Limiar: ")
                    funcao = input("Status: ")

                    if nome:
                        racao["nome"] = nome
                    if quantidade:
                        racao["quantidade"] = float(quantidade)
                    if funcao:
                        racao["funcao"] = funcao
                    if limiar:
                        racao["limiar_de_estoque"] = float(limiar)

                    print(f"Produto ID {id} atualizado com sucesso!")
                    registro_de_auditoria(
                        f'O usuario {usuario_logado["nome"]} atualizou a ração de ID {id} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
                    )
        elif op == 0:
            print("Encerrando...")
            break


def notificacoes(cadastro: dict, usuario_logado: dict, registro_de_auditoria: list):
    menus.mostrar_cabecalho_tela("NOTIFICAÇÕES")
    print(f"Notificações, {usuario_logado['nome']}?\n")
    print(" 1 - Animais doentes")
    print(" 2 - Estoque de ração abaixo do limiar")
    print(" 0 - Sair")
    print("=" * 60)

    print("\n[bold blue]->[/]", end="")
    op = int(input(" "))
    if op == 1:
        table = Table(title="[bold italic]Cadastrar Animal[/]")
        table.add_column("ID")
        table.add_column("NOME")
        table.add_column("IDADE")
        table.add_column("PESO")
        table.add_column("STATUS")
        table.add_column("GENERO")
        table.add_column("PREÇO")
        table.add_column("TIPO")
        animais_doentes = False
        console = Console()
        for animal in cadastro["animais"]:
            if animal["status"].lower() == "doente":

                table.add_row(
                    animal["id"],
                    animal["nome"],
                    str(animal["idade"]),
                    str(animal["peso"]),
                    animal["status"],
                    animal["genero"],
                    str(animal["preco"]),
                    animal["tipo"],
                )

                animais_doentes = True
        if animais_doentes:
            console.print(table)
            registro_de_auditoria.append(
                f'o usuario {usuario_logado["nome"]} entrou nas notificações , {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
            )
        if not animais_doentes:
            print("Nenhum animal doente encontrado.")
            registro_de_auditoria.append(
                f'o usuario {usuario_logado["nome"]} entrou nas notificações , {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
            )
    elif op == 2:
        racao_baixo_estoque = False
        console = Console()
        table = Table(title="[bold italic]Limiar das Rações[/]")
        table.add_column("ID")
        table.add_column("NOME")
        table.add_column("FUNÇÃO")
        table.add_column("QUANTIDADE")
        table.add_column("LIMIAR DO ESTOQUE")
        for racao in cadastro["racao"]:
            if racao["quantidade"] < racao["limiar_de_estoque"]:

                table.add_row(
                    str(racao["id"]),
                    racao["nome"],
                    racao["funcao"],
                    str(racao["quantidade"]),
                    str(racao["limiar_de_estoque"]),
                )

                racao_baixo_estoque = True
        if racao_baixo_estoque:
            console.print(table)
            registro_de_auditoria.append(
                f'o usuario {usuario_logado["nome"]} entrou nas notificações , {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
            )
        if not racao_baixo_estoque:
            print("Nenhuma ração com estoque abaixo do limiar encontrada.")
            registro_de_auditoria.append(
                f'o usuario {usuario_logado["nome"]} entrou nas notificações , {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
            )


def exibir_menu_de_gerenciar_rebanho():
    print(
        f'{"\n"*4}Gerenciar Rebanho\n 1 - Cadastrar Animal\n 2 - Visualizar Animais\n 3 - Editar Animal\n 4 - Excluir Animal\n 0 - Voltar ao Menu Anterior\n'
    )


def cadastrar_animal(cadastro: dict, usuario_logado: dict, registro_de_auditoria: list):

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
        registro_de_auditoria.append(
            f'o usuario {usuario_logado["nome"]} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}'
        )
        console = Console()

        table = Table(title="[bold italic]Cadastrar Animal[/]")
        table.add_column("ID")
        table.add_column("NOME")
        table.add_column("IDADE")
        table.add_column("PESO")
        table.add_column("STATUS")
        table.add_column("GENERO")
        table.add_column("PREÇO")
        table.add_column("TIPO")

        table.add_row(
            codigo,
            nome,
            str(datetime.now().year - int(ano)),
            str(peso),
            status,
            genero,
            str(preco) + "$",
            tipo,
        )

        console.print(table)

        continuar = input("\nCadastrar outro animal? (S/N): ").upper()

        if continuar != "S":
            break


def exibir_animais(cadastro: dict, usuario_logado: dict, registro_de_auditoria: list):
    while True:
        menus.mostrar_cabecalho_tela("VISUALIZAR ANIMAIS")
        print(f"Qual animal você deseja visualizar, {usuario_logado['nome']}?\n")
        print(" 1 - Busca por ID do animal")
        print(" 2 - Buscar por Tipo dos animais")
        print(" 3 - Buscar por status")
        print(" 4 - Verificar animais à venda")
        print(" 5 - Visualizar todos os animais")
        print(" 0 - Sair da busca")
        print("=" * 60)

        print("[bold blue]->[/]", end="")
        op = int(input(" "))
        if op == 1:
            id = input("Digite o ID do animal que deseja buscar: ")
            for animal in cadastro["animais"]:
                if animal["id"] == id:

                    console = Console()

                    table = Table(title="[bold italic]Animais Encontrados[/]")

                    table.add_column("ID")
                    table.add_column("Nome")
                    table.add_column("Raça")
                    table.add_column("Tipo")
                    table.add_column("Status")

                    table.add_row(
                        animal["id"],
                        animal["nome"],
                        animal["raça"],
                        animal["tipo"],
                        animal["status"],
                    )

                    console.print(table)
                    registro_de_auditoria.append(
                        f"o usuario {usuario_logado["nome"]} buscou pelo animal ID {id} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
                    )
                    break
            else:
                print(f"Animal ID {id} não encontrado.")
        elif op == 2:
            tipo = input("Digite o tipo do animal que deseja buscar: ")
            animal_encontrado = False
            console = Console()

            table = Table(title="Animais Encontrados")

            table.add_column("ID")
            table.add_column("Nome")
            table.add_column("Raça")
            table.add_column("Tipo")
            table.add_column("Status")

            for animal in cadastro["animais"]:
                if animal["tipo"] == tipo:
                    table.add_row(
                        animal["id"],
                        animal["nome"],
                        animal["raça"],
                        animal["tipo"],
                        animal["status"],
                    )
                    animal_encontrado = True

            if animal_encontrado:
                console.print(table)
                registro_de_auditoria.append(
                    f"o usuario {usuario_logado["nome"]} buscou pelo animal do tipo: {tipo} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
                )
            if not animal_encontrado:
                print(f"Animais do tipo {tipo} não encontrados.")
        elif op == 3:
            status = input("Digite o status do animal que deseja buscar: ")
            animal_encontrado = False
            console = Console()

            table = Table(title="Animais Encontrados")

            table.add_column("ID")
            table.add_column("Nome")
            table.add_column("Raça")
            table.add_column("Tipo")
            table.add_column("Status")

            for animal in cadastro["animais"]:
                if animal["status"] == status:
                    table.add_row(
                        animal["id"],
                        animal["nome"],
                        animal["raça"],
                        animal["tipo"],
                        animal["status"],
                    )
                    animal_encontrado = True

            if animal_encontrado:
                registro_de_auditoria.append(
                    f"o usuario {usuario_logado["nome"]} buscou pelo animal com o status: {status} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
                )
                console.print(table)
            if not animal_encontrado:
                print(f"Animais com status {status} não encontrados.")
        elif op == 4:
            console = Console()
            table = Table(title="Animais Encontrados")
            table.add_column("ID")
            table.add_column("Nome")
            table.add_column("Raça")
            table.add_column("Tipo")
            table.add_column("Status")
            animais_a_venda = False
            for animal in cadastro["animais"]:
                if animal["preco"] != "Indisponivel":

                    table.add_row(
                        animal["id"],
                        animal["nome"],
                        animal["raça"],
                        animal["tipo"],
                        animal["status"],
                    )

                    animais_a_venda = True
            if animais_a_venda:
                console.print(table)
                registro_de_auditoria.append(
                    f"o usuario {usuario_logado["nome"]} buscou pelos animais que estão a venda , {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
                )
            if not animais_a_venda:
                print("Nenhum animal disponível para venda encontrado.")
        elif op == 5:
            console = Console()
            table = Table(title="Animais Encontrados")
            table.add_column("ID")
            table.add_column("Nome")
            table.add_column("Raça")
            table.add_column("Tipo")
            table.add_column("Status")
            achou = False
            for animal in cadastro["animais"]:
                table.add_row(
                    animal["id"],
                    animal["nome"],
                    animal["raça"],
                    animal["tipo"],
                    animal["status"],
                )
                achou = True
            if achou:
                console.print(table)
                registro_de_auditoria.append(
                    f"o usuario {usuario_logado["nome"]} buscou por todos os animais cadastrados , {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
                )
            else:
                print("Nenhum animal cadastrado!")
        elif op == 0:
            print("Saindo da busca...")
            sleep(1.6)
            break
        else:
            print("Opção inválida!")
            sleep(1.6)
            continue


def editar_animal(cadastro: dict, usuario_logado: dict, registro_de_auditoria: list):
    id = input("Digite o ID do animal que deseja editar: ")
    for animal in cadastro["animais"]:
        if animal["id"] == id:
            console = Console()

            table = Table(title="Edição do Animal")

            table.add_column("ID")
            table.add_column("Nome")
            table.add_column("Raça")
            table.add_column("Tipo")
            table.add_column("Status")

            table.add_row(
                animal["id"],
                animal["nome"],
                animal["raça"],
                animal["tipo"],
                animal["status"],
            )
            console.print(table)

            print(
                "\n\nDigite os novos dados do animal (deixe em branco para manter o valor atual):"
            )
            nome = input("Nome: ")
            idade = input("Idade: ")
            raça = input("Raça: ")
            peso = input("Peso: ")
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
                animal["idade"] = int(idade)
            if raça:
                animal["raça"] = raça
            if peso:
                animal["peso"] = float(peso)
            if tipo:
                animal["tipo"] = tipo
            if genero:
                animal["genero"] = genero
            if status:
                animal["status"] = status
            animal["preco"] = preco

            console = Console()

            table = Table(title="Edição do Animal")

            table.add_column("ID")
            table.add_column("Nome")
            table.add_column("Raça")
            table.add_column("Tipo")
            table.add_column("Status")

            table.add_row(
                animal["id"],
                animal["nome"],
                animal["raça"],
                animal["tipo"],
                animal["status"],
            )
            console.print(table)

            print(f"Animal ID {id} atualizado com sucesso!")
            registro_de_auditoria.append(
                f"o usuario {usuario_logado["nome"]} editou o animal com ID {id} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
            )


def excluir_animal(cadastro: dict, usuario_logado: dict, registro_de_auditoria: list):
    id = input("Qual animal deseja excluir? (Digite o ID): ")
    for animal in cadastro["animais"]:
        if animal["id"] == id:
            print(f"Você tem certeza que deseja excluir o animal ID {id}? (S/N)")

            print("[bold blue]->[/]", end="")
            confirmacao = input(" ")
            if confirmacao == "S":
                cadastro["animais"].remove(animal)
                print(f"Animal ID {id} excluído com sucesso!")
                registro_de_auditoria.append(
                    f"o usuario {usuario_logado["nome"]} excluiu o animal com ID {id} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
                )
                break

            else:
                print("Exclusão cancelada.")
                break
    else:
        print(f"Animal ID {id} não encontrado.")


def permitir_pedidos(
    pedido_de_compra: dict, usuario_logado: dict, registro_de_auditoria: list
):
    while True:
        menus.mostrar_cabecalho_tela("PEDIDOS DE COMPRA")
        print(f"Que pedido deseja visualizar, {usuario_logado['nome']}?")
        print(
            "1 - Visualizar Pedidos em Aguardo\n"
            "2 - Visualizar Pedidos Confirmados\n"
            "3 - Visualizar Pedidos Recusados\n"
            "0 - Sair"
        )
        print("[bold blue]->[/]", end="")
        op = int(input(" "))
        if op > 3 or op < 0:
            print("Opção Inválida!")
            continue
        if op == 0:
            break

        elif op == 1:

            pedidos_aguardo = []
            console = Console()
            table = Table(title="[bold italic]Pedidos Encontrados[/]")
            table.add_column("ID")
            table.add_column("NOME")
            table.add_column("PRODUTO")
            table.add_column("QUANTIDADE")
            table.add_column("STATUS")
            table.add_column("CRIADO EM")

            for indice, pedido in enumerate(pedido_de_compra["pedidos"]):

                if pedido["status_pedido"] == "Aguardo":

                    pedidos_aguardo.append(indice)

                    data = pedido["criado_em"][0]

                    table.add_row(
                        str(indice),
                        pedido["nome_cliente"],
                        pedido["nome_produto"],
                        str(pedido["quantidade"]),
                        pedido["status_pedido"],
                        f"{str(data['ano']).zfill(2)}/{str(data['mes']).zfill(2)}/{str(data['dia']).zfill(2)}",
                    )

            if len(pedidos_aguardo) != 0:
                console.print(table)
            if len(pedidos_aguardo) == 0:
                print("Não há pedidos aguardando aprovação.")
                continue

            escolha = int(input("\nDigite o índice do pedido que deseja analisar: "))

            if escolha < 0 or escolha >= len(pedidos_aguardo):
                print("Pedido inválido!")
                continue

            indice_real = pedidos_aguardo[escolha]

            print("\n1 - Confirmar Pedido\n" "2 - Recusar Pedido\n" "0 - Cancelar")
            print("[bold blue]->[/]", end="")
            decisao = int(input(" "))

            if decisao == 1:
                pedido_de_compra["pedidos"][indice_real]["status_pedido"] = "Confirmado"
                print("Pedido confirmado com sucesso!")
                registro_de_auditoria.append(
                    f"o usuario {usuario_logado["nome"]} permitiu o pedido de {pedido['nome_cliente']} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
                )
                continue

            elif decisao == 2:
                pedido_de_compra["pedidos"][indice_real]["status_pedido"] = "Recusado"
                print("Pedido recusado com sucesso!")
                registro_de_auditoria.append(
                    f"o usuario {usuario_logado["nome"]} permitiu o recusou de {pedido['nome_cliente']} , {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
                )
                continue

            elif decisao == 0:
                break

            else:
                print("Opção inválida!")
                continue
        elif op == 2:
            console = Console()
            table = Table(title="[bold italic]Pedidos Confirmados[/]")
            table.add_column("ID")
            table.add_column("NOME")
            table.add_column("PRODUTO")
            table.add_column("QUANTIDADE")
            table.add_column("STATUS")
            table.add_column("CRIADO EM")
            achou = False
            for pedido in pedido_de_compra["pedidos"]:
                if pedido["status_pedido"] == "Confirmado":
                    data = pedido["criado_em"][0]
                    table.add_row(
                        str(pedido["item_id"]),
                        pedido["nome_cliente"],
                        pedido["nome_produto"],
                        str(pedido["quantidade"]),
                        pedido["status_pedido"],
                        f"{str(data['ano']).zfill(2)}/{str(data['mes']).zfill(2)}/{str(data['dia']).zfill(2)}",
                    )
                    achou = True
            if achou:
                registro_de_auditoria.append(
                    f"o usuario {usuario_logado["nome"]} visualizou os pedidos CONFIMADOS , {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
                )
                console.print(table)
            else:
                print("Pedido não achado ou inexistente")
        elif op == 3:
            console = Console()
            table = Table(title="[bold italic]Pedidos Recusados[/]")
            table.add_column("ID")
            table.add_column("NOME")
            table.add_column("PRODUTO")
            table.add_column("QUANTIDADE")
            table.add_column("STATUS")
            table.add_column("CRIADO EM")
            achou = False
            for pedido in pedido_de_compra["pedidos"]:
                if pedido["status_pedido"] == "Recusado":
                    data = pedido["criado_em"][0]

                    data = pedido["criado_em"][0]
                    table.add_row(
                        str(pedido["item_id"]),
                        pedido["nome_cliente"],
                        pedido["nome_produto"],
                        str(pedido["quantidade"]),
                        pedido["status_pedido"],
                        f"{str(data['ano']).zfill(2)}/{str(data['mes']).zfill(2)}/{str(data['dia']).zfill(2)}",
                    )
                    achou = True
            if achou:
                console.print(table)
                registro_de_auditoria.append(
                    f"o usuario {usuario_logado["nome"]} visualizou os pedidos RECUSADO , {datetime.now().strftime("%d/%m/%Y às %H:%M")}"
                )
            else:
                print("Pedido não achado ou inexistente")
