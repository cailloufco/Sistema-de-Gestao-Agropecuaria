from time import sleep
from datetime import datetime

from rich import print
from rich.panel import Panel
from rich import box
import time
from rich.progress import track


import os

from assets import acesso
from assets import menus
from assets import adm, cliente, relatorio

print(
    Panel.fit(
        "Bem-Vindo ao Sistema Fazenda Sertão!",
        title="[italic green]Fazenda Sertão[/]",
        padding=(1),
        title_align="left",
    )
)

for i in track(range(10), description="Carregando..."):
    time.sleep(0.3)

sleep(1)
os.system("cls" if os.name == "nt" else "clear")


usuarios_cadastrados = {
    "nome": ["Caio", "Higor"],
    "senha": ["Caio123", "Higor123"],
    "administrador": [False, True],
}
usuario_logado = {"nome": None, "administrador": None, "logado": False}
cadastro = {
    "animais": [
        {
            "id": "00123-A",
            "nome": "Belinha",
            "idade": 3,
            "raça": "Nelore",
            "peso": 324,
            "tipo": "Bovino",
            "genero": "F",
            "preco": 3.370,
            "status": "Doente",
            "ano": "2023",
            "lote": "A",
        },
        {
            "id": "00223-A",
            "nome": "Francisca",
            "idade": 3,
            "raça": "Nelore",
            "peso": 361,
            "tipo": "Bovino",
            "genero": "F",
            "preco": 3.550,
            "status": "Engorda",
            "ano": "2023",
            "lote": "A",
        },
    ],
    "produtos": [
        {
            "id": 0,
            "nome": "Leite",
            "quantidade": 100,
            "preco": 2.5,
            "status": "Disponível",
        },
        {
            "id": 1,
            "nome": "Queijo",
            "quantidade": 52,
            "preco": 5.99,
            "status": "Disponível",
        },
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
            "item_id": 0,
            "status_pedido": "Aguardo",
            "criado_em": [{"ano": 2026, "mes": 6, "dia": 16, "hora": 17, "minuto": 13}],
            "quantidade": 120,
        }
    ]
}
registro_de_auditoria = []


while True:
    menus.mostrar_menu_inicial()
    sleep(1)
    op = int(input("Escolha a opção desejada: "))
    if op > 2 or op < 0:
        print("Opção inválida. Tente novamente.\n")
        sleep(1.6)
        continue

    if op == 1:
        menus.mostrar_cabecalho_tela("LOGIN")
        nome_de_usuario = input("Digite seu nome: ")
        senha_do_usuario = input("Digite sua senha: ")

        usuario_logado = acesso.logar(
            nome_de_usuario, senha_do_usuario, usuarios_cadastrados
        )
        if not usuario_logado:
            print("NOME ou SENHA incorreta ou inválida!!!\nTente Novamente...")
            print(usuario_logado)
            continue

    elif op == 2:
        menus.mostrar_cabecalho_tela("CADASTRO")
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

        if op > 6 or op < 0:
            print("Opção inválida. Tente novamente.\n")
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
                    adm.cadastrar_animal(cadastro , registro_de_auditoria)

                elif op1 == 2:

                    adm.exibir_animais(cadastro, usuario_logado , registro_de_auditoria)

                elif op1 == 3:

                    adm.editar_animal(cadastro , registro_de_auditoria)

                elif op1 == 4:

                    adm.excluir_animal(cadastro , registro_de_auditoria)

        elif op == 2:
            menus.mostrar_cabecalho_tela("PRODUÇÃO E DERIVADOS")
            print(" 1 - Cadastrar")
            print(" 2 - Buscar")
            print(" 3 - Atualizar Itens")
            print(" 4 - Remover Itens")
            print(" 0 - Voltar")
            print("=" * 60)
            op1 = int(input("\n-> "))
            if op1 == 1:
                adm.cadastrar_produto(cadastro , registro_de_auditoria)

            elif op1 == 2:
                adm.buscar_produto(cadastro, usuario_logado , registro_de_auditoria)

            elif op1 == 3:
                adm.atualizar_produto(cadastro , registro_de_auditoria)

            elif op1 == 4:
                adm.remover_produto(cadastro , registro_de_auditoria)

        elif op == 3:

            adm.cadastrar_racao(cadastro, usuario_logado , registro_de_auditoria)

        elif op == 4:

            adm.permitir_pedidos(pedido_de_compra, usuario_logado , registro_de_auditoria)

        elif op == 5:
            adm.notificacoes(cadastro, usuario_logado , registro_de_auditoria)

        elif op == 6:
            while True:
                print(
                    "1 - Relatorio de Animais\n"
                    "2 - Relatorio de Produtos\n"
                    "3 - Registro de Auditoria\n"
                    "0 - Sair"
                )
                print("[bold blue]->[/]", end="")
                op = int(input(" "))
                if op == 1:
                    relatorio.gerar_relatorios_animais(cadastro)
                elif op == 2:
                    relatorio.gerar_relatorios_produtos(cadastro)
                elif op == 3:
                    print("")
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
            cliente.realizar_compra(cadastro, usuario_logado , registro_de_auditoria)

        elif op == 2:
            cliente.vizualizar_estoque(cadastro, usuario_logado , registro_de_auditoria)

        elif op == 3:
            cliente.agendar_retirada(cadastro, usuario_logado, agendamento , registro_de_auditoria)

        elif op == 4:
            cliente.ver_agendamento(usuario_logado, agendamento , registro_de_auditoria)

        elif op == 5:
            cliente.pedido_de_compra(pedido_de_compra, usuario_logado, cadastro , registro_de_auditoria)

        elif op == 6:

            cliente.exibir_pedidos(pedido_de_compra, usuario_logado , registro_de_auditoria)

        elif op == 0:
            print("Deslogando...")
            sleep(1.6)
            usuario_logado = {"nome": None, "administrador": None, "logado": False}
