from time import sleep
from datetime import datetime


from assets import acesso
from assets import menus
from assets import adm, cliente

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
agendamento = {"produto": [], "animais": []}
pedido_de_compra = {
    "pedidos": [
        {
            "nome_cliente": "Carlos",
            "nome_produto": "Leite",
            "item_id":0,
            "status_pedido": "Aguardo",
            "criado_em": [{'ano':2026
                           ,'mes':06
                           ,'dia':16
                           ,'hora':17
                           ,'minuto':13}],
            "quantidade": 120
        }
    ]
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
                adm.exibir_menu_de_gerenciar_rebanho()

                op1 = int(input("-> "))

                if op1 > 4 or op1 < 0:
                    print(f'Opção inválida , tente novamente!{'\n'*3}')
                    sleep(1)
                    continue
                elif op1 == 0:
                    break
                elif op1 == 1:
                    adm.cadastrar_animal(cadastro)

                elif op1 == 2:

                    adm.exibir_animais(cadastro, usuario_logado)

                elif op1 == 3:

                    adm.editar_animal(cadastro)

                elif op1 == 4:

                    adm.excluir_animal(cadastro)

        elif op == 2:
            print("""     *****MENU*****
1 - Cadastrar
2 - Buscar
3 - Atualizar Itens
4 - Remover Itens
0 - Voltar""")
            op1 = int(input("\n-> "))
            if op1 == 1:
                adm.cadastrar_produto(cadastro)

            elif op1 == 2:
                adm.buscar_produto(cadastro, usuario_logado)

            elif op1 == 3:
                adm.atualizar_produto(cadastro)

            elif op1 == 4:
                adm.remover_produto(cadastro)

        elif op == 3:

            adm.cadastrar_racao(cadastro, usuario_logado)

        elif op == 4:
            def permitir_pedidos(pedido_de_compra: dict , usuario_logado: dict):
                print(f'Que pedido deseja visualizar, {usuario_logado['nome']}?')
                print('1 - Visualizar Pedidos em Aguardo\n2 - Visualizar Pedidos Confirmados\n3 - Visualizar Pedidos Recusados\n0 - Sair')
                op = int(input('->'))
                if op > 3 or op < 0:
                    print('Opção inválida!')
                    return

                elif op == 1:
                    contador = 0
                    for pedido in pedido_de_compra['pedidos']:
                        if pedido['status'] == 'Aguardo':
                            print(f'{contador}')


        elif op == 5:
            adm.notificacoes(cadastro, usuario_logado)

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
            cliente.realizar_compra(cadastro, usuario_logado)

        elif op == 2:
            cliente.vizualizar_estoque(cadastro, usuario_logado)

        elif op == 3:
            cliente.agendar_retirada(cadastro, usuario_logado, agendamento)

        elif op == 4:

            def ver_agendamento(
                usuario_logado: dict, cadastro: dict, agendamento: dict
            ):
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

        elif op == 5:

            def pedido_de_compra(pedido_de_compra: dict , usuario_logado:dict , cadastro: dict):
                while True:
                    print(f"Olá , {usuario_logado['nome']}! Deseja realizar um pedido de compra de um PRODUTO? ( S / N )")
                    op = input("->").upper()
                    if op == 'S':
                        print("Digite o ID do PRODUTO que deseja realizar um pedido")
                        id = int(input('->'))
                        nome_produto = None
                        achado = False                    
                        for produto in cadastro['produtos']:
                            if produto['id'] == id and produto["status"] != "Indisponivel":
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
                        quando_criado = [{'ano':datetime.now().year
                                        ,'mes':datetime.now().month
                                        ,'dia':datetime.now().day
                                        ,'hora':datetime.now().hour
                                        ,'minuto':datetime.now().minute
                                        }]
                        pedido = {
                "nome_cliente": usuario_logado["nome"],
                "nome_produto": nome_produto,
                "item_id":produto_id,
                "status_pedido": "Aguardo",
                "criado_em": quando_criado,
                "quantidade": quantidade
            }
                        pedido_de_compra["pedidos"].append(pedido)
                    else:
                        print('Saindo...')
                        break
        elif op == 6:
            def exibir_pedidos(pedidos: dict , usuario_logado: dict): 
                print(
                            f"Olá , {usuario_logado['nome']} , Seus Pedidos:"
                        )
                achado = False
                for pedido in pedidos['pedidos']:
                    if pedido["nome_cliente"] == usuario_logado["nome"]:
                        print(f"ID : {pedido['item_id']}  | Produto Pedido: {pedido['nome_produto']} | Quantidade : {pedido['quantidade']}  | Status : {pedido['status_pedido']} | Criado em: {pedido['criado_em'][0]}/{pedido['criado_em'][1]}/{pedido['criado_em'][2]} , {pedido['criado_em'][3]}-{pedido['criado_em'][4]}")
                    achado = True
                if not achado:
                    print(f'{usuario_logado["nome"]} , Nenhum Pedido Realizado!')
                    return

             
        elif op == 0:
            print("Deslogando...")
            sleep(1.6)
            usuario_logado = {"nome": None, "administrador": None, "logado": False}
