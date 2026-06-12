from assets import adm, cliente
from datetime import datetime

# lista = {'nome':['caio','jose','nycole']}

# for nome in lista['nome']:
#     if nome == 'nycole':
#         print('teste')
#     print(nome)

# nome = input("Digite seu nome: ")


# if nome :
#     print("Nome digitado:", nome)
# else:
#     print("Nenhum nome foi digitado.")

# print ("print colorida \033[31m vermelho \033[0m")
# print ("print colorida \033[32m verde \033[0m")
# print ("print colorida \033[33m amarelo \033[0m")
# print ("print colorida \033[34m azul \033[0m")


# usuarios_cadastrados = {
#     'usuario':[{'nome':'Caio',
#                 'senha':'Caio123',
#                 'idade':18}]
# }

## dava pra ter usado isso daqui pra nao usar o zip

# while True:
#     op = int(input('criar usuario: 1 cria , 2 exibe:'))
#     if op == 1:
#         nome = input('digite seu nome: ')
#         senha = input('digite sua senha: ')
#         idade = int(input('digite sua idade: '))
#         usuarios_cadastrados['usuario'].append(
#             {
#                 'nome':nome,
#                 'senha':senha,
#                 'idade':idade
#             }
#         )
#     if op == 2:
#         for nome in usuarios_cadastrados['usuario']:
#             print(nome['nome'])


# dict_teste = {
#     "nome": []
#     }

# if dict_teste["nome"]:
#     print("cai aqui quando a lista nome tiver itens")
# else:
#     print("cai aqui quando a lista 'nome' estiver vazia")


usuarios_cadastrados = {
    "nome": ["Caio"],
    "senha": ["Caio123"],
    "administrador": [False],
}
usuario_logado = {"nome": "Caio", "administrador": False, "logado": True}
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
agendamento = {
    "produto": [
        {
            "nome_cliente": "Caio",
            "tipo": "Animal",
            "item_id": 0,
            "quantidade": 400,
            "data": "2008-06-04",
            "hora": "15:30",
            "status": "Agendado",
            "data_agendamento": [
                datetime.now().strftime("%Y-%m-%d"),
                datetime.now().strftime("%H:%M:%S"),
            ],
        }
    ],
    "animais": [],
}


def ver_agendamento(usuario_logado: dict, cadastro: dict, agendamento: dict):
    while True:
        print(
            f"Olá , {usuario_logado['nome']} , Seus Agendamentos\n1 - Agendamento de Animais\n2 - Agendamento de Produtos"
        )
        op = int(input("-> "))
        achou = False
        if op == 1:
            """{
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
            for item in agendamento["produto"]:
                if item["nome_cliente"] == usuario_logado["nome"]:
                    f'ID: {item["id"]} | Função: {item["funcao"]} | Nome: {item["nome"]} | Quantidade: {item["quantidade"]} | Limiar de Estoque: {item["limiar_de_estoque"]}'
                    achou = True
            if achou:
                print("tá funcionando")


ver_agendamento(usuario_logado, cadastro, agendamento)
